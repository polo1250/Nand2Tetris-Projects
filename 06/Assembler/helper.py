# All the helper functions needed in the main file

# Part I

def is_blank(line):
    """This function answer wether the line is a comment or a blank line or neither"""

    return (line[0:2] == "//") or (line == "")


def is_label_declaration(line):
    """This function answer wether the line is a label declaration or not"""

    return (line[0] == "(") and (line[-1] == ")")


def get_label(line):
    """This function return label contained in label declaration line"""

    return line[1:-1]


def contain_variable(line):
    """This function answer if line contains a variable"""

    return (line[0] == "@") and not(line[1:].isdigit()) and line[1:].islower()


def get_variable(line):
    """This function return variable contained in line"""

    return (line[1:])


def handle_symbols(symbol_table, parser, filename):
    """This function capture symbols in assembly file and add them to symbol_table"""

    # Read through the file in the first pass, and add every label and 
    # to the symbol table 
    with open(filename,"r") as assembly_file:
        instruction_address = -1

        for line in assembly_file:
            proper_line = parser.clean_line(line) # line without newline special character

            # if line is blank or is a comment
            if (is_blank(proper_line)): 
                pass

            elif (is_label_declaration(proper_line)):
                label = get_label(proper_line)
                if not(symbol_table.contains(label)):
                    symbol_table.add_entry(label, instruction_address+1)

            # if line is a simple c-instruction
            else:
                instruction_address += 1


    # Read through the file in the second pass, and add every variable and 
    # to the symbol table
    with open(filename,"r") as assembly_file:
        variable_address = 16

        for line in assembly_file:
            proper_line = parser.clean_line(line) # line without newline special character

            # if line is blank or is a comment
            if (is_blank(proper_line)): 
                pass

            # if line contains a variable
            elif (contain_variable(proper_line)):
                variable = get_variable(proper_line)
                if not(symbol_table.contains(variable)):
                    symbol_table.add_entry(variable, variable_address)
                    variable_address += 1
                instruction_address += 1

            # if line is a simple c-instruction
            else:
                instruction_address += 1


