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
        cont = 0
        objects = models.storage.all()
        new = {}
        for elem in objects:
            new[elem] = objects[elem].to_dict()
        for elem in new:
            if (args == new[elem]['__class__']):
                cont = cont + 1
        print(cont)

def default(self, args):
        """ Handle alternative command representations """
        first = args.split('.')
        if len(first) > 1:
            class_name = first[0]
            methods = first[1]
            first[1] = first[1].replace('(', '&(')
            second = first[1].split('&')
            comando = class_name

            if methods == "all()":
                self.do_all(comando)
            elif methods == "count()":
                self.do_count(comando)
            else:
                methods = second[0]
                elems = second[1]
                elems = elems.replace('(', '')
                elems = elems.replace(')', '')
                elems = elems.replace('{', '"{')
                elems = elems.replace('}', '}"')
                third = shlex.split(elems)
                if not third:
                    id = ' '
                    third.append(id)
                else:
                    for i in range(len(third)):
                        third[i] = third[i].replace(',', ' ')
                        third[i] = third[i].strip()
                    id = third[0]
                comando = comando + ' ' + id
                comando = comando.replace('\"', '')
                if methods == "show" and len(third) == 1:
                    self.do_show(comando)
                elif methods == "destroy" and len(third) == 1:
                    self.do_destroy(comando)
                elif methods == "update":
                    x = len(third)
                    if x > 1 and third[1][0] == '{' and third[1][-1] == '}':
                        third[1] = third[1].replace('{', '')
                        third[1] = third[1].replace('}', '')
                        third[1] = third[1].replace(': ', ':')
                        sub = shlex.split(third[1], ', ')
                        new = []
                        for ele in sub:
                            sub2 = ele.split(':')
                            if len(sub2) < 2:
                                sub2.append('')
                            new.append(tuple(sub2))
                        dicti = dict(new)
                        print(dicti)
                        for key in dicti:
                            new_comand = comando + ' '
                            new_comand += str(key)
                            new_comand = new_comand.replace('\"', '')
                            new_comand = new_comand.replace('\'', '')
                            new_comand += ' \"' + str(dicti[key]) + '\"'
                            self.do_update(new_comand)
                    else:
                        for i in range(1, len(third)):
                            if i == 1:
                                comando = comando + ' ' + third[i]
                            if i == 2:
                                comando = comando + ' '
                                comando += '\"' + third[i] + '\"'
                        self.do_update(comando)
                else:
                    return cmd.Cmd.default(self, args)
        else:
            return cmd.Cmd.default(self, args)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
