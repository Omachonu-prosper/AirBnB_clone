#!/usr/bin/python3

"""Entry point of the command interpreter
"""

import cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    def __init__(self):
        """Initialize the console with required properties
        """
        super().__init__()
        self.prompt = '(hbnb) '
        self.class_names = [
            'BaseModel',
            'User',
            'Place',
            'State',
            'City',
            'Amenity',
            'Review'
        ]

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
        elif arg not in self.class_names:
            print("** class doesn't exist **")
        else:
            obj = eval(f"{arg}()")
            obj.save()
            print(obj.id)

    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id.
        Ex:
        $(hbnb) show BaseModel <id>
        """
        if not arg:
            print("** class name missing **")
        elif arg.split()[0] not in self.class_names:
            print("** class doesn't exist **")
        elif len(arg.split()) < 2:
            print("** instance id missing **")
        elif not storage.show(f"{arg.split()[0]}.{arg.split()[1]}"):
            print("** no instance found **")
        else:
            obj = storage.show(f"{arg.split()[0]}.{arg.split()[1]}")
            print(obj)

    def do_all(self, arg):
        """Prints all string representation of all instances
        based or not on the class name.
        Ex:
        $(hbnb) all BaseModel
        or
        $(hbnb) all
        """
        all_objs = []
        if arg and arg not in self.class_names:
            print("** class doesn't exist **")
        else:
            for obj in storage.all().values():
                if arg:
                    if arg == obj.__class__.__name__:
                        all_objs.append(str(obj))
                else:
                    all_objs.append(str(obj))
            print(all_objs)

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file).
        Ex:
        $(hbnb) destroy BaseModel 1234-1234-1234
        """
        if not arg:
            print("** class name missing **")
        elif arg.split()[0] not in self.class_names:
            print("** class doesn't exist **")
        elif len(arg.split()) < 2:
            print("** instance id missing **")
        elif not storage.show(f"{arg.split()[0]}.{arg.split()[1]}"):
            print("** no instance found **")
        else:
            obj = storage.show(f"{arg.split()[0]}.{arg.split()[1]}")
            obj.destroy()

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file).
        Ex:
        $(hbnb) update BaseModel 1234-1234-1234 email "aibnb@mail.com"
        """
        if not arg:
            print("** class name missing **")
        elif shlex.split(arg)[0] not in self.class_names:
            print("** class doesn't exist **")
        elif len(shlex.split(arg)) < 2:
            print("** instance id missing **")
        elif not storage.show(f"{shlex.split(arg)[0]}.{shlex.split(arg)[1]}"):
            print("** no instance found **")
        elif len(shlex.split(arg)) < 3:
            print("** attribute name missing **")
        elif len(shlex.split(arg)) < 4:
            print("** value missing **")
        else:
            class_name = shlex.split(arg)[0]
            id = shlex.split(arg)[1]
            attr_name = shlex.split(arg)[2]
            attr_value = shlex.split(arg)[3]
            obj = storage.show(f"{class_name}.{id}")
            setattr(obj, attr_name, attr_value)
            obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
