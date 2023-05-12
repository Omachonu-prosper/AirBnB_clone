#!/usr/bin/python3

"""Entry point of the command interpreter
"""

import cmd


class HBNBCommand(cmd.Cmd):
    def __init__(self):
        """Initialize the console with required properties
        """
        super().__init__(self)
        self.prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the console
        """
        exit()

    def do_EOF(self, arg):
        """Quit command to exit the console
        """
        exit()

    def emptyline(self):
        """Do nothing if an empty line is entered."""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
