from sys import argv
from codewriter_push_pop import CodeWriterPushPop
import global_variables


class CodeWriteSubroutines:
    """This class take care of the subroutines code translation"""

    def __init__(self, filename):
        """Initialize templates"""
        
        self.filename = filename
        self.writer_push_pop = CodeWriterPushPop(filename)

        # Template for a function initialization in assembly

        # Function initiation
        self.result_function = "({0})\n"


        # Template for a function call in assembly

        # Push return address to stack
        self.result_call = "    @{0}\n"
        self.result_call += "    D=A\n"
        self.result_call += "    @SP\n"
        self.result_call += "    A=M\n"
        self.result_call += "    M=D\n"
        self.result_call += "    @SP\n"
        self.result_call += "    M=M+1\n"

        # Push LCL, ARG, THIS, THAT
        self.result_call += self._push_symbol('LCL')
        self.result_call += self._push_symbol('ARG')
        self.result_call += self._push_symbol('THIS')
        self.result_call += self._push_symbol('THAT')

        # ARG = SP - (n + 5) <==> ARG = SP - n - 5
        self.result_call += "    @5\n"
        self.result_call += "    D=A\n"
        self.result_call += "    @{1}\n"
        self.result_call += "    D=A+D\n"
        self.result_call += "    @SP\n"
        self.result_call += "    A=M\n"
        self.result_call += "    D=A-D\n"
        self.result_call += "    @ARG\n"
        self.result_call += "    M=D\n"

        # LCL = SP
        self.result_call += "    @SP\n"
        self.result_call += "    D=M\n"
        self.result_call += "    @LCL\n"
        self.result_call += "    M=D\n"

        # goto function
        self.result_call += "    @{2}\n"
        self.result_call += "    0;JMP\n"

        # return-address label
        self.result_call += "  ({0})\n"


        # Template for a function return in assembly

        # frame = LCL
        self.result_return = "    @LCL\n"
        self.result_return += "    D=M\n"
        self.result_return += "    @{0}\n"
        self.result_return += "    M=D\n"

        # ret = *(frame - 5)
        self.result_return += "    @{0}\n"
        self.result_return += "    D=M\n"
        self.result_return += "    @5\n"
        self.result_return += "    D=D-A\n"
        self.result_return += "    A=D\n"
        self.result_return += "    D=M\n"
        self.result_return += "    @{1}\n"
        self.result_return += "    M=D\n"

        # *ARG = pop()
        self.result_return += "    @SP\n"
        self.result_return += "    M=M-1\n"
        self.result_return += "    @SP\n"
        self.result_return += "    A=M\n"
        self.result_return += "    D=M\n"
        self.result_return += "    @ARG\n"
        self.result_return += "    A=M\n"
        self.result_return += "    M=D\n"

        # SP = ARG + 1
        self.result_return += "    @ARG\n"
        self.result_return += "    D=M\n"
        self.result_return += "    @SP\n"
        self.result_return += "    M=D+1\n"

        # THAT = *(frame - 1)
        self.result_return += "    @{0}\n"
        self.result_return += "    D=M\n"
        self.result_return += "    @1\n"
        self.result_return += "    D=D-A\n"
        self.result_return += "    A=D\n"
        self.result_return += "    D=M\n"
        self.result_return += "    @THAT\n"
        self.result_return += "    M=D\n"

        # THIS = *(frame - 2)
        self.result_return += "    @{0}\n"
        self.result_return += "    D=M\n"
        self.result_return += "    @2\n"
        self.result_return += "    D=D-A\n"
        self.result_return += "    A=D\n"
        self.result_return += "    D=M\n"
        self.result_return += "    @THIS\n"
        self.result_return += "    M=D\n"

        # ARG = *(frame - 3)
        self.result_return += "    @{0}\n"
        self.result_return += "    D=M\n"
        self.result_return += "    @3\n"
        self.result_return += "    D=D-A\n"
        self.result_return += "    A=D\n"
        self.result_return += "    D=M\n"
        self.result_return += "    @ARG\n"
        self.result_return += "    M=D\n"

        # LCL = *(frame - 4)
        self.result_return += "    @{0}\n"
        self.result_return += "    D=M\n"
        self.result_return += "    @4\n"
        self.result_return += "    D=D-A\n"
        self.result_return += "    A=D\n"
        self.result_return += "    D=M\n"
        self.result_return += "    @LCL\n"
        self.result_return += "    M=D\n"

        # goto RET
        self.result_return += "    @{1}\n"
        self.result_return += "    A=M\n"
        self.result_return += "    0;JMP\n"


    

    def write_function(self, command_args):
        """Write a function initialization into the assembly file
           parameter command_args should look like this ['function', 'function_name', 'number_of_args']
        """ 

        # Add function to the top of the function list (to express that this is the current function for coming operations)
        global_variables.function_list.append(command_args[1])

        # Retrieve essentials parameters
        f_name = command_args[1]
        function_local_arg = int(command_args[2])

        for _ in range(function_local_arg):
            self.result_function += self.writer_push_pop.push('constant', '0')

        return self.result_function.format(f_name)
        

    def write_call(self, command_args):
        """Write a function call into the assembly file
           parameter command_args should look like this ['call', 'function_name', 'number_of_args']
        """

        global_variables.count_for_call += 1
        c1 = str(global_variables.count_for_call)
        f_name = global_variables.function_list[-1]
        return self.result_call.format((f_name + "$" + "RET" + c1), command_args[2], command_args[1])
    

    def write_return(self):
        """Write a return from a function into the assembly file"""

        # Temporary variables
        frame = 'R13'
        ret = 'R14'
        return self.result_return.format(frame, ret)


    def _push_symbol(self, symbol):
        """Push constant value to stack or symbol value
           parameter symbol should be any of ('THIS', 'THAT', 'ARG', 'LCL', etc...)
        """

        # Get value from the memory_segment into register D
        result = "    @{}\n"
        result += "    D=M\n"

        # *SP = symbol
        result += "    @SP\n"
        result += "    A=M\n"
        result += "    M=D\n"

        # SP++
        result += "    @SP\n"
        result += "    M=M+1\n"

        return result.format(symbol)
