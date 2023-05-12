#!/usr/bin/python3

"""Entry point of the command interpreter
"""

import cmd
import shlex
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    def __init__(self):
        """Initialize the console with required properties
        """
        super().__init__()
        self.prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the console
        """
        exit()

    def do_EOF(self, arg):
        """Quit command to exit the console
        """
        print()
        exit()

    def emptyline(self):
        """Do nothing if an empty line is entered."""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id.
        Ex:
        $(hbnb) create BaseModel
        """
        if not arg:
            print("** class name missing **")
        elif arg != 'BaseModel':
            print("** class doesn't exist **")
        else:
            model = BaseModel()
            model.save()
            print(model.id)

    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id.
        Ex:
        $(hbnb) show BaseModel <id>
        """
        if not arg:
            print("** class name missing **")
        elif arg.split()[0] != 'BaseModel':
            print("** class doesn't exist **")
        elif len(arg.split()) < 2:
            print("** instance id missing **")
        elif not storage.show(f"BaseModel.{arg.split()[1]}"):
            print("** no instance found **")
        else:
            model = storage.show(f"BaseModel.{arg.split()[1]}")
            print(model)

    def do_all(self, arg):
        """Prints all string representation of all instances
        based or not on the class name.
        Ex:
        $(hbnb) all BaseModel
        or
        $(hbnb) all
        """
        all_models = []
        if arg and arg != 'BaseModel':
            print("** class doesn't exist **")
        else:
            for model in storage.all().values():
                all_models.append(str(model))
            print(all_models)

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file).
        Ex:
        $(hbnb) destroy BaseModel 1234-1234-1234
        """
        if not arg:
            print("** class name missing **")
        elif arg.split()[0] != 'BaseModel':
            print("** class doesn't exist **")
        elif len(arg.split()) < 2:
            print("** instance id missing **")
        elif not storage.show(f"BaseModel.{arg.split()[1]}"):
            print("** no instance found **")
        else:
            model = storage.show(f"BaseModel.{arg.split()[1]}")
            model.destroy()

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file).
        Ex:
        $(hbnb) update BaseModel 1234-1234-1234 email "aibnb@mail.com"
        """
        if not arg:
            print("** class name missing **")
        elif shlex.split(arg)[0] != 'BaseModel':
            print("** class doesn't exist **")
        elif len(shlex.split(arg)) < 2:
            print("** instance id missing **")
        elif not storage.show(f"BaseModel.{shlex.split(arg)[1]}"):
            print("** no instance found **")
        elif len(shlex.split(arg)) < 3:
            print("** attribute name missing **")
        elif len(shlex.split(arg)) < 4:
            print("** value missing **")
        else:
            id = shlex.split(arg)[1]
            attr_name = shlex.split(arg)[2]
            attr_value = shlex.split(arg)[3]
            model = storage.show(f"BaseModel.{id}")
            setattr(model, attr_name, attr_value)
            model.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
