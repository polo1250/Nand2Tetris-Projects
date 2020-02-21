from codewriter_arithmetic import CodeWriterArithmetic
from codewriter_push_pop import CodeWriterPushPop
from codewriter_flow_control import CodeWriterFlowControl
from codewriter_subroutines import CodeWriteSubroutines


class CodeWriter:
    """This class take care of the code translation"""


    def __init__(self, filename):
        """Initialize the common templates"""

        self.filename = filename
        self.arithmetic_two_operands = ['add', 'sub', 'and', 'or']
        self.arithmetic_one_operands = ['neg', 'not']
        self.arithmetic_booleans = ['eq', 'gt', 'lt']

    def write_init(self):
        """Return the init code for the assembly file if needed"""

        writer = CodeWriteSubroutines(self.filename)

        bootstrap_code = "    @256\n"
        bootstrap_code += "    D=A\n"
        bootstrap_code += "    @SP\n"
        bootstrap_code += "    M=D\n"

        bootstrap_code += writer.write_call(['call', 'Sys.init', '0'])

        return bootstrap_code

    def write_arithmetic(self, command):
        """This function return the assembly code for arithmetic commands"""
        
        writer = CodeWriterArithmetic()

        # if the command requiers two operands
        if command in self.arithmetic_two_operands:

            if command == "add":
                return writer.add()
            elif command == "sub":
                return writer.sub() 
            elif command == "and":
                return writer.bitwise_and()
            elif command == "or":
                return writer.bitwise_or()

        # if the command requiers one operand
        elif command in self.arithmetic_one_operands:

            if command == "neg":    
                return writer.neg()
            elif command == "not":
                return writer.bitwise_not()

        elif command in self.arithmetic_booleans:

            if command == "eq":
                return writer.eq()
            elif command == "gt":
                return writer.gt()
            elif command == "lt":
                return writer.lt()


    def write_push_pop(self, command_args):
        """This function return the assembly code for push/pop commands"""

        writer = CodeWriterPushPop(self.filename)

        if command_args[0] == "push":
            return writer.push(command_args[1], command_args[2])
        elif command_args[0] == "pop":
            return writer.pop(command_args[1], command_args[2])


    def write_control_flow(self, command_args):
        """This function return the assembly code for control flow commands"""

        writer = CodeWriterFlowControl()
        if command_args[0] == "label":
            return writer.write_label(command_args[1])
        elif command_args[0] == "goto":
            return writer.write_goto(command_args[1])
        elif command_args[0] == "if-goto":
            return writer.write_if(command_args[1])


    def write_subroutines(self, command_args):
        """This function return the assembly code for subroutines commands"""

        writer = CodeWriteSubroutines(self.filename)

        if len(command_args) == 1:
            return writer.write_return()

        else:
            if command_args[0] == "call":
                return writer.write_call(command_args)
            
            elif command_args[0] == "function":
                return writer.write_function(command_args)