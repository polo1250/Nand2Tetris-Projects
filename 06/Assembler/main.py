from symbol_table import SymbolTable
from mnemonics_code import Code
from parser import Parser
from helper import *
from sys import argv

def main():
    symbol_table = SymbolTable() # initiate symbol table object to contain symbol table
    parser = Parser()

    # add all symbols to symbol table
    handle_symbols(symbol_table, parser, argv[1])


    # Third pass through the file, to parse each command and build its 
    # binary value and the binary output file
    mnemonics_code = Code()
    with open(argv[1], "r") as assembly_file:
        binary_file = open((argv[1][:-3] + "hack"), "w") # The output binary file

        for line in assembly_file:
            proper_line = parser.clean_line(line) # line without newline special character

            # if line is not an instruction
            if (is_blank(proper_line) or is_label_declaration(proper_line)):
                pass

            # if line is an instruction 
            else:
                instruction_type = parser.command_type(proper_line)
                if (instruction_type == "C_COMMAND"):
                    binary_c_instruction = parser.parse_c_instruction(proper_line, mnemonics_code)  
                    binary_file.write(binary_c_instruction)
                else: # If it is an a-instruction
                    binary_a_instruction = parser.parse_a_instruction(proper_line, symbol_table)  
                    binary_file.write(binary_a_instruction)
        
        binary_file.close()
            



if __name__ == "__main__":
    main()
                    