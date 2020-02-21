import global_variables


class CodeWriterArithmetic:
    """This class take care of the arithmetic code translation"""

    def __init__(self):
        """Initialize templates"""

        # Initialize two operands template

        # Decrement SP position on the stack
        self.result_arithmetic_two_operands = "    @SP\n"
        self.result_arithmetic_two_operands += "    M=M-1\n"

        # Get second element from the top of the stack into register D
        self.result_arithmetic_two_operands += "    @SP\n"
        self.result_arithmetic_two_operands += "    A=M\n"
        self.result_arithmetic_two_operands += "    D=M\n"

        # Decrement SP position on the stack
        self.result_arithmetic_two_operands += "    @SP\n"
        self.result_arithmetic_two_operands += "    M=M-1\n"

        # Access the first element from the stack and apply operation
        self.result_arithmetic_two_operands += "    @SP\n"
        self.result_arithmetic_two_operands += "    A=M\n"
        self.result_arithmetic_two_operands += "{}"

        # Put the result back on the stack
        #self.result_arithmetic_two_operands += "    @SP\n"
        #self.result_arithmetic_two_operands += "    A=M\n"
        self.result_arithmetic_two_operands += "    M=D\n"

        #Increment SP
        self.result_arithmetic_two_operands += "    @SP\n"
        self.result_arithmetic_two_operands += "    M=M+1\n"


        # Initialize one operand template

        # Decrement SP position on the stack
        self.result_arithmetic_one_operand = "    @SP\n"
        self.result_arithmetic_one_operand += "    M=M-1\n"

        # Get the element from the top of the stack, 
        # negate it and put it into register D
        self.result_arithmetic_one_operand += "    @SP\n"
        self.result_arithmetic_one_operand += "    A=M\n"
        self.result_arithmetic_one_operand += "{}"

        # Put the result back on the stack
        #self.result_arithmetic_one_operand += "    @SP\n"
        #self.result_arithmetic_one_operand += "    A=M\n"
        self.result_arithmetic_one_operand += "    M=D\n"

        #Increment SP
        self.result_arithmetic_one_operand += "    @SP\n"
        self.result_arithmetic_one_operand += "    M=M+1\n"


        # Initialize booleans template

        # Decrement SP position on the stack
        self.result_arithmetic_boolean = "    @SP\n"
        self.result_arithmetic_boolean += "    M=M-1\n"

        # Get second element from the top of the stack into register D
        self.result_arithmetic_boolean += "    @SP\n"
        self.result_arithmetic_boolean += "    A=M\n"
        self.result_arithmetic_boolean += "    D=M\n"

        # Decrement SP position on the stack
        self.result_arithmetic_boolean += "    @SP\n"
        self.result_arithmetic_boolean += "    M=M-1\n"

        # Access the first element from the stack and 
        # substract first element from it
        self.result_arithmetic_boolean += "    @SP\n"
        self.result_arithmetic_boolean += "    A=M\n"
        self.result_arithmetic_boolean += "    D=M-D\n"
        self.result_arithmetic_boolean += "{0}"
        self.result_arithmetic_boolean += "{1}"
            
        # to be executed if condition is false
        self.result_arithmetic_boolean += "    @SP\n"
        self.result_arithmetic_boolean += "    A=M\n"
        self.result_arithmetic_boolean += "    M=0\n"
        self.result_arithmetic_boolean += "{2}"
        self.result_arithmetic_boolean += "    0;JMP\n"

        # to be executed if condition is true
        self.result_arithmetic_boolean += "{3}"
        self.result_arithmetic_boolean += "    @SP\n"
        self.result_arithmetic_boolean += "    A=M\n"
        self.result_arithmetic_boolean += "    M=-1\n"
        self.result_arithmetic_boolean += "{2}"
        self.result_arithmetic_boolean += "    0;JMP\n"

        #Increment SP
        self.result_arithmetic_boolean += "{4}"
        self.result_arithmetic_boolean += "    @SP\n"
        self.result_arithmetic_boolean += "    M=M+1\n"


    def add(self):
        """Add values popped from the stack"""

        return self.result_arithmetic_two_operands.format("    D=D+M\n")
        
        
    def sub(self):
        """Sub values popped from the stack""" 

        return self.result_arithmetic_two_operands.format("    D=M-D\n")


    def bitwise_and(self):
        """Bitwise-and values popped from the stack"""

        return self.result_arithmetic_two_operands.format("    D=D&M\n")


    def bitwise_or(self):
        """Bitwise-or values popped from the stack"""

        return self.result_arithmetic_two_operands.format("    D=D|M\n")    


    def neg(self):
        """Bitwise-negate value popped from the stack"""

        return self.result_arithmetic_one_operand.format("    D=-M\n")


    def bitwise_not(self):
        """Bitwise-not value popped from the stack"""

        return self.result_arithmetic_one_operand.format("    D=!M\n")


    def eq(self):
        """Bitwise-eq values popped from the stack"""

        global_variables.count_for_bool += 1
        c1 = str(global_variables.count_for_bool)
        c_name = global_variables.function_list[-1] # current name in list
        return self.result_arithmetic_boolean.format(f"    @{c_name}$RIGHTEQ{c1}\n",
                                                     "    D;JEQ\n",
                                                     f"    @{c_name}$WHATEVEREQ{c1}\n",
                                                     f"  ({c_name}$RIGHTEQ{c1})\n",
                                                     f"  ({c_name}$WHATEVEREQ{c1})\n")


    def gt(self):
        """Bitwise-gt values popped from the stack"""

        global_variables.count_for_bool += 1
        c1 = str(global_variables.count_for_bool)
        c_name = global_variables.function_list[-1] # current name in list
        return self.result_arithmetic_boolean.format(f"    @{c_name}$RIGHTGT{c1}\n",
                                                     "    D;JGT\n",
                                                     f"    @{c_name}$WHATEVERGT{c1}\n",
                                                     f"  ({c_name}$RIGHTGT{c1})\n",
                                                     f"  ({c_name}$WHATEVERGT{c1})\n")


    def lt(self):
        """Bitwise-gt values popped from the stack"""

        global_variables.count_for_bool += 1
        c1 = str(global_variables.count_for_bool)
        c_name = global_variables.function_list[-1] # current name in list
        return self.result_arithmetic_boolean.format(f"    @{c_name}$RIGHTLT{c1}\n",
                                                     "    D;JLT\n",
                                                     f"    @{c_name}$WHATEVERLT{c1}\n",
                                                     f"  ({c_name}$RIGHTLT{c1})\n",
                                                     f"  ({c_name}$WHATEVERLT{c1})\n")

    