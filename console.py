#!/usr/bin/python3
""" ALX  AirBnB Console """
import cmd
import sys
import json
import os
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ General Class for HBNBCommand """
    prompt = '(hbnb) '
    classes = {'BaseModel': BaseModel, 'User': User, 'City': City,
               'Place': Place, 'Amenity': Amenity, 'Review': Review,
               'State': State}

    def do_quit(self, arg):
        """ Exit method for quit typing """
        exit()

    def do_EOF(self, arg):
        """ Exit method for EOF """
        print('')
        exit()

    def emptyline(self):
        """ Method to pass when emptyline entered """
        pass

    def do_create(self, arg):
        """ Create a new instance """
        if len(arg) == 0:
            print('** class name missing **')
            return
        new = None
        if arg:
            arg_list = arg.split()
            if len(arg_list) == 1:
                if arg in self.classes.keys():
                    new = self.classes[arg]()
                    new.save()
                    print(new.id)
                else:
                    print("** class doesn't exist **")

    def do_show(self, arg):
        """ Method to print instance """
        if len(arg) == 0:
            print('** class name missing **')
            return
        elif arg.split()[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(arg.split()) > 1:
            key = arg.split()[0] + '.' + arg.split()[1]
            if key in storage.all():
                i = storage.all()
                print(i[key])
            else:
                print('** no instance found **')
        else:
            print('** instance id missing **')

    def do_destroy(self, arg):
        """ Method to delete instance with class and id """
        if len(arg) == 0:
            print("** class name missing **")
            return
        arg_list = arg.split()
        try:
            obj = eval(arg_list[0])
        except Exception:
            print("** class doesn't exist **")
            return
        if len(arg_list) == 1:
            print('** instance id missing **')
            return
        if len(arg_list) > 1:
            key = arg_list[0] + '.' + arg_list[1]
            if key in storage.all():
                storage.all().pop(key)
                storage.save()
            else:
                print('** no instance found **')
                return

    def do_all(self, arg):
        """ Method to print all instances """
        if len(arg) == 0:
            print([str(a) for a in storage.all().values()])
        elif arg not in self.classes:
            print("** class doesn't exist **")
        else:
            print([str(a) for b, a in storage.all().items() if arg in b])

    def do_update(self, arg):
        """ Method to update JSON file"""
        arg_list = check_args(argv)
        if arg_list:
            if len(arg_list) == 1:
                print("** instance id missing **")
            else:
                instance_id = "{}.{}".format(arg_list[0], arg_list[1])
                if instance_id in self.storage.all():
                    if len(arg_list) == 2:
                        print("** attribute name missing **")
                    elif len(arg_list) == 3:
                        print("** value missing **")
                    else:
                        obj = self.storage.all()[instance_id]
                        if arg_list[2] in type(obj).__dict__:
                            v_type = type(obj.__class__.__dict__[arg_list[2]])
                            setattr(obj, arg_list[2], v_type(arg_list[3]))
                        else:
                            setattr(obj, arg_list[2], arg_list[3])
                else:
                    print("** no instance found **")

            self.storage.save()

    def do_count(self, arg):
        """Retrieve the number of instances of a class"""
        arg1 = parse(arg)
        count = 0
        for obj in models.storage.all().values():
            if arg1[0] == type(obj).__name__:
                count += 1
        print(count)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
