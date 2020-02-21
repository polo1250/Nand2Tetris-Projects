class Parser:
    """This class parse provided virtual machine command into its underlying field"""

    def __init__(self):
        """Nothing to initialize"""
        pass


    def clean_line(self, line):
        """Get rid of newline keys, comments, whitelines in any line and return it"""
        
        if "//" in line:
            line = line[:line.index("//")]

        line = (line[:-1]).strip()
        return line


    def command_type(self, command):
        """Provide the command type"""

        command = command.split()
        if len(command) == 1:
            if command[0] == "return":
                return "C_RETURN"
            else:
                return "C_ARITHMETIC"
        elif len(command) == 2:
            if command[0] == "push":
                return "C_PUSH"
            elif command[0] == "pop":
                return "C_POP"
            elif command[0] == "label":
                return "C_LABEL"
            elif command[0] == "goto":
                return "C_GOTO"
            elif command[0] == "if-goto":
                return "C_IF"
        elif len(command) == 3:
            if command[0] == "function":
                return "C_FUNCTION"
            elif command[0] == "call":
                return "C_CALL"
    

    def command_args(self, command):
        """Return the command args"""

        return command.split()