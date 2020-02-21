from sys import argv
from global_variables import function_list


class CodeWriterPushPop:
    """This class take care of the memory access code translation"""

    def __init__(self, filename):
        """Initialize templates"""

        self.filename = filename
        self.memory_mapping = {'local':'LCL', 'argument':'ARG', 'this':'THIS', 'that':'THAT',\
                               'pointer':'3', 'temp':'5', \
                               'static':filename}

        # Initialize push templates

        # Push for memory_segments: local, argument, this, that
        # Compute and store address of the target memory_segment
        self.result_push_1 = "    @{0}\n"
        self.result_push_1 += "    D=A\n"
        self.result_push_1 += "    @{1}\n"
        self.result_push_1 += "    A=M\n"
        self.result_push_1 += "    D=D+A\n"
        self.result_push_1 += "    @addr\n"
        self.result_push_1 += "    M=D\n"

        # Get value from addr and store it on top of the stack
        self.result_push_1 += "    @addr\n"
        self.result_push_1 += "    A=M\n"
        self.result_push_1 += "    D=M\n"
        self.result_push_1 += "    @SP\n"
        self.result_push_1 += "    A=M\n"
        self.result_push_1 += "    M=D\n"

        # Increment SP
        self.result_push_1 += "    @SP\n"
        self.result_push_1 += "    M=M+1\n"

        # Push for memory segment: static, pointer
        # Get value from the memory_segment
        self.result_push_2 = "    @{}\n"
        self.result_push_2 += "    D=M\n"

        # Put value on top of the stack
        self.result_push_2 += "    @SP\n"
        self.result_push_2 += "    A=M\n"
        self.result_push_2 += "    M=D\n"

        # Increment SP
        self.result_push_2 += "    @SP\n"
        self.result_push_2 += "    M=M+1\n"

        # Push for memory_segments: temp
        # Compute and store address of the target memory_segment
        self.result_push_3 = "    @{0}\n"
        self.result_push_3 += "    D=A\n"
        self.result_push_3 += "    @{1}\n"
        self.result_push_3 += "    D=D+A\n"
        self.result_push_3 += "    @addr\n"
        self.result_push_3 += "    M=D\n"

        # Get value from addr and store it on top of the stack
        self.result_push_3 += "    @addr\n"
        self.result_push_3 += "    A=M\n"
        self.result_push_3 += "    D=M\n"
        self.result_push_3 += "    @SP\n"
        self.result_push_3 += "    A=M\n"
        self.result_push_3 += "    M=D\n"

        # Increment SP
        self.result_push_3 += "    @SP\n"
        self.result_push_3 += "    M=M+1\n"


        # Initialize pop template

        # Pop for memory segments: local, argument, this, that
        # Compute and store address of the target memory_segment
        self.result_pop_1 = "    @{0}\n"
        self.result_pop_1 += "    D=A\n"
        self.result_pop_1 += "    @{1}\n"
        self.result_pop_1 += "    A=M\n"
        self.result_pop_1 += "    D=D+A\n"
        self.result_pop_1 += "    @addr\n"
        self.result_pop_1 += "    M=D\n"

        # Decrement SP
        self.result_pop_1 += "    @SP\n"
        self.result_pop_1 += "    M=M-1\n"

        # Get value from stack top and store it in the address held by addr
        self.result_pop_1 += "    @SP\n"
        self.result_pop_1 += "    A=M\n"
        self.result_pop_1 += "    D=M\n"
        self.result_pop_1 += "    @addr\n"
        self.result_pop_1 += "    A=M\n"
        self.result_pop_1 += "    M=D\n"

        # Pop for memory segment: static, pointer
        # Decrement SP
        self.result_pop_2 = "    @SP\n"
        self.result_pop_2 += "    M=M-1\n"

        # Get value from stack top and store it in the address held by addr
        self.result_pop_2 += "    @SP\n"
        self.result_pop_2 += "    A=M\n"
        self.result_pop_2 += "    D=M\n"
        self.result_pop_2 += "    @{}\n"
        self.result_pop_2 += "    M=D\n"

        # Pop for memory segments: temp
        # Compute and store address of the target memory_segment
        self.result_pop_3 = "    @{0}\n"
        self.result_pop_3 += "    D=A\n"
        self.result_pop_3 += "    @{1}\n"
        self.result_pop_3 += "    D=D+A\n"
        self.result_pop_3 += "    @addr\n"
        self.result_pop_3 += "    M=D\n"

        # Decrement SP
        self.result_pop_3 += "    @SP\n"
        self.result_pop_3 += "    M=M-1\n"

        # Get value from stack top and store it in the address held by addr
        self.result_pop_3 += "    @SP\n"
        self.result_pop_3 += "    A=M\n"
        self.result_pop_3 += "    D=M\n"
        self.result_pop_3 += "    @addr\n"
        self.result_pop_3 += "    A=M\n"
        self.result_pop_3 += "    M=D\n"

    
    def push(self, memory_segment, i):
        """Push value from memory segment to stack"""

        if memory_segment == 'constant':
            return self._push_constant(i)

        if memory_segment == 'static':
            return self.result_push_2.format((self.memory_mapping[memory_segment] + i))

        if memory_segment == 'temp':
            return self.result_push_3.format(self.memory_mapping[memory_segment], i)

        if memory_segment == 'pointer':
            if i == '0':
                return self.result_push_2.format(self.memory_mapping['this'])
            elif i == '1':
                return self.result_push_2.format(self.memory_mapping['that'])

        return self.result_push_1.format(i, self.memory_mapping[memory_segment])


    def pop(self, memory_segment, i):
        """Pop value from stack to memory segment"""

        if memory_segment == 'static':
            return self.result_pop_2.format((self.memory_mapping[memory_segment] + i))

        if memory_segment == 'temp':
            return self.result_pop_3.format(self.memory_mapping[memory_segment], i)

        if memory_segment == 'pointer':
            if i == '0':
                return self.result_pop_2.format(self.memory_mapping['this'])
            elif i == '1':
                return self.result_pop_2.format(self.memory_mapping['that'])

        return self.result_pop_1.format(i, self.memory_mapping[memory_segment])


    def _push_constant(self, i):
        """Push constant value to stack"""

        # copy the constant in register D
        result = "    @{}\n"
        result += "    D=A\n"

        # *SP = i
        result += "    @SP\n"
        result += "    A=M\n"
        result += "    M=D\n"

        # SP++
        result += "    @SP\n"
        result += "    M=M+1\n"

        return result.format(i)