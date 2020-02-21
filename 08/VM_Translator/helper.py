# All the helper functions needed in the main file
import os
from parser import Parser
from codewriter import CodeWriter
import global_variables


def is_blank_or_is_comment(line):
    """This function answer wether the line is a comment or a blank line or neither"""
    
    line = line.strip()
    return (line[0:2] == "//") or (line == "")


def translate_file(vm_file, asmfile):

    current_file_name = os.path.basename(vm_file)[:-3]
    # Initiate list of functions/files names and variables and append current file
    global_variables.function_list.append(current_file_name)

    with open(vm_file, 'r') as vmfile:
        # Create assembly file to receive translated code
        assembly_file = open(asmfile, 'a')

        parser = Parser()
        assembly_code = ""
        code_writer = CodeWriter(current_file_name)
        
        for line in vmfile:
            if is_blank_or_is_comment(line):
                pass
            else:
                command = parser.clean_line(line)
                command_type = parser.command_type(command)

                if command_type == "C_ARITHMETIC":
                    assembly_code = code_writer.write_arithmetic(command)

                elif command_type in ["C_LABEL", "C_GOTO", "C_IF"]:
                    command_args = parser.command_args(command)
                    assembly_code = code_writer.write_control_flow(command_args)

                elif command_type in ["C_CALL", "C_RETURN", "C_FUNCTION"]:
                    command_args = parser.command_args(command)
                    assembly_code = code_writer.write_subroutines(command_args)

                else:
                    command_args = parser.command_args(command)
                    assembly_code = code_writer.write_push_pop(command_args)
                
                assembly_file.write(assembly_code)
        
        assembly_file.close()

    # Reset list of functions processed in the current file
    global_variables.function_list.clear()


def add_bootstrap_code(asmfile, filename):
    """Provide the bootstrap code in assembly"""

    global_variables.function_list.append('Sys')
    # Open assembly file to receive init code
    assembly_file = open(asmfile, 'a')

    # Get basename of the file in provided filepath
    input_file_basename = os.path.basename(filename)

    code_writer = CodeWriter(input_file_basename)
    bootstrap_code = code_writer.write_init()
    

    assembly_file.write(bootstrap_code)

    assembly_file.close()