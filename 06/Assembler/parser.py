class Parser:
    """This class parse provided assembly command into its underlying field"""

    def __init__(self):
        """Initialize instance variables"""

        self.opcode_a = "0"
        self.opcode_c = "111"

    
    def command_type(self, command):
        """Provide the command type"""

        if (command[0] == "@"):
            return "A_COMMAND"
        else:
            return "C_COMMAND"


    def clean_line(self, line):
        """Get rid of newline keys, spaces, comments, whitelines in any line and return it"""

        line = (line[:-1]).strip().replace(" ", "")
        if "//" in line:
            line = line[:line.index("//")]
        
        return line

    
    def parse_a_instruction(self, command, symbol_table):
        """Return the constructed binary pattern of the command"""

        if (not(command[1:].isdigit()) and symbol_table):
            command = "@" + str(symbol_table.get_address(command[1:]))

        # Get the constant, convert it to binary, fill it with zeros to 
        # fill the 15-bits requirements
        constant = command[1:]
        binary_constant = bin(int(constant))[2:]
        binary_constant_complement = "0" * (15 - len(binary_constant))

        return self.opcode_a + binary_constant_complement + binary_constant + "\n"


    def parse_c_instruction(self, command, mnemonics_code):
        """Return the constructed binary pattern of the command"""
        self.dest = ""
        self.comp = ""
        self.jump = ""

        # if dest is part of the command, get dest
        if "=" in command: 
            equal_index = command.index("=")
            self.dest = command[:equal_index]
            command = command[equal_index + 1:]
        else:
            self.dest = "null"

        # if jump is part of the command, get jump and set comp
        if ";" in command:
            semicolon_index = command.index(";")
            self.comp = command[:semicolon_index]
            self.jump = command[semicolon_index + 1:]
        else:
            self.comp = command
            self.jump = "null"


        dest_binary = mnemonics_code.get_binary_value(self.dest, "dest")   
        comp_binary = mnemonics_code.get_binary_value(self.comp, "comp") 
        jump_binary = mnemonics_code.get_binary_value(self.jump, "jump")

        return self.opcode_c + comp_binary + dest_binary + jump_binary + "\n"

