import os
from sys import argv, exit
from helper import translate_file, add_bootstrap_code
from parser import Parser
from codewriter import CodeWriter

def main():
    input_filename = ""
    output_filename = ""

    # Get the name of the file or directory
    if len(argv) != 2:
        print("Please, provide a vmcode file or directory")
        print("Usage: python3 vm_translator.py filename")
        exit(1)
    else:
        # 
        if argv[1].endswith('/'):
            input_filename = argv[1][:-1]
        else:
            input_filename = argv[1]


    # Determine if file is a directory or not, and act accordingly
    if os.path.isdir(input_filename):
        # Init file for the assembly program in case of a directory
        init_file = "Sys.vm"

        # Setup output filename
        output_filename = input_filename + "/" + os.path.basename(input_filename) + ".asm"

        # Initiate output file
        initiator = open(output_filename, 'w')
        initiator.close()

        # Filepath for each vm file in directory
        filepath = ""

         # collect names of all the vm files
        vm_files = [f for f in os.listdir(input_filename) if f.endswith('.vm')]

        # if init_file exist, start with it translation
        if init_file in vm_files:
            
            # Add bootstrap code at the beginning of file
            add_bootstrap_code(output_filename, input_filename)

            # Construct file path
            filepath = os.path.join(input_filename, init_file)

            # Handle the whole translation to the output file
            translate_file(filepath, output_filename)

            #Init file is processed, now we can get rid of it
            vm_files.remove(init_file)

            # Translate the remaining vm files if they are some
            for another_file in vm_files:
                # Construct file path
                filepath = os.path.join(input_filename, another_file)

                # Handle the whole translation to the output file
                translate_file(filepath, output_filename)


        # If init_file is not in the directory
        else:
            # Then we should have only one file to translate 
            if len(vm_files) != 1:
                print("There has to be only one vm file in the directory")
                print("An init file should be in the directory if there's more than one file")
                print("Translator exiting...")
                exit(1)

            else:
                # Construct file path
                filepath = os.path.join(input_filename, vm_files[0])

                # Handle the whole translation to the output file   
                translate_file(filepath, output_filename)  
        
        
    else:
        output_filename = input_filename[-2] + 'asm'

        # Initiate output file
        initiator = open(output_filename, 'w')
        initiator.close()
        
        # Handle the whole translation to the output file
        translate_file(input_filename, output_filename)




if __name__ == "__main__":
    main()