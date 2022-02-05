import subprocess
import os
## file-search ##
# https://github.com/gg-cyber172/OS_shell
#Main function where we will define the user input
def main():
    while True:
        #prefix of command
        command = input("$ ")
        if command == "exit":
            break
        elif command == "help":
            print("psh: This is a simple shell program")
        else:
            execute_commands(command)

    # Take the input file name from user
    filename = input("Enter the file name\n")
    #Check if the file exists
    try:
        file = open(filename, 'r')
        #Reading all the lines
        while True:
            line = file.readline()
            if line[-1:] == "\n":
                line = line[:-1]
            #End of line
            if not line:
             break
            #close file
            file.close()
    #If file not found
    except IOError:
     print("FIle not available")

def execute_commands(command):
    try:
        subprocess.run(command.split())
        #Making an execption so the program doesn't crash when a unkown input is entered 
    except Exception:
        print("psh: command not found: {}".format(command))
