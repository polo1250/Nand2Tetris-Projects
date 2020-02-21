import global_variables


class CodeWriterFlowControl:
    """This class take care of the flow control code translation"""

    def __init__(self):
        """Initialize templates"""

        # Template for a label initialization in assembly
        self.label_result = "  ({})\n"


        # Template for an inconditional jump  in assembly
        self.goto_result = "    @{}\n"
        self.goto_result += "    0;JMP\n"


        # Template for a conditional jump  in assembly

        # Decrement SP position on the stack
        self.if_goto_result = "    @SP\n"
        self.if_goto_result += "    M=M-1\n"

        # Get truth value from the top of the stack into register D
        self.if_goto_result += "    @SP\n"
        self.if_goto_result += "    A=M\n"
        self.if_goto_result += "    D=M\n"

        # Verify truth value and jump accordingly
        self.if_goto_result += "    @{}\n"
        self.if_goto_result += "    D;JNE\n"


    def write_label(self, label):
        """Write a label initialization into the assembly file""" 
        
        # global_variables.count_for_bool += 1
        #if label == global_variables.list_if_goto[-1]:
        #    c1 = str(global_variables.count_for_if)
        #    global_variables.list_if_goto.pop()
        #
        #elif label == global_variables.list_goto_f[-1]:
        #    c1 = str(global_variables.count_for_goto_f)
        #    global_variables.list_goto_false.pop()

        c_name = global_variables.function_list[-1]
        return self.label_result.format(c_name + "$" + label)


    def write_goto(self, label):
        """Write an inconditional jump to the specified label into the assembly file"""

        #global_variables.count_for_bool += 1
        #c1 = str(global_variables.count_for_bool)
        c_name = global_variables.function_list[-1]
        return self.goto_result.format(c_name + "$" + label)


    def write_if(self, label):
        """Write a conditional jump to the specified label into the assembly file"""

        #global_variables.count_for_if += 1
        #c1 = str(global_variables.count_for_if)
        c_name = global_variables.function_list[-1]
        #global_variables.list_if_goto.append(label)
        return self.if_goto_result.format(c_name + "$" + label)