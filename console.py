#!/usr/bin/env python3
import cmd

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def help_quit(self):
        print("Quit command to exit the program")

    def do_EOF(self, arg):
        """Exit the program by sending EOF (Ctrl+D)"""
        print()  # Print a newline before exiting
        return True

    def emptyline(self):
        """Do nothing on empty input"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()

