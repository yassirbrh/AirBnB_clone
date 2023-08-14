#!/usr/bin/env python3
'''
    Modules Importation
'''
import cmd
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.state import State
from models.city import City
from models.review import Review
import models


class HBNBCommand(cmd.Cmd):
    '''
        Definition of the class HBNBCommand inheriting from cmd.Cmd
    '''
    prompt = '(hbnb) '
    __classes = ['BaseModel', 'User', 'Amenity', 'Place', 'State', 'City']
    __classes.append('Review')

    def do_quit(self, arg):
        '''Quit command to exit the program
        '''
        return True

    def do_EOF(self, arg):
        '''EOF signal to exit the program
        '''
        return True

    def emptyline(self):
        '''Function to do nothing if no command is entered in the console
        '''
        pass

    def do_create(self, arg):
        '''Create command to create a new instance of the specified class
        '''
        if len(arg) == 0:
            print("** class name missing **")
        else:
            if arg in HBNBCommand.__classes:
                cls_init = globals()[arg]
                new_obj = cls_init()
                models.storage.save()
                print(new_obj.id)
            else:
                print("** class doesn't exist **")

    def do_show(self, line):
        '''Show command to show an instance
        '''
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        else:
            if args[0] in HBNBCommand.__classes:
                if len(args) < 2:
                    print("** instance id missing **")
                else:
                    objects = models.storage.all()
                    the_obj = None
                    for obj in objects.keys():
                        if objects[obj].id == args[1]:
                            the_obj = objects[obj]
                            break
                    if the_obj:
                        print(the_obj)
                    else:
                        print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def do_destroy(self, line):
        '''Destroy command to delete an instance of a class
        '''
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        else:
            if args[0] in HBNBCommand.__classes:
                if len(args) < 2:
                    print("** instance id missing **")
                else:
                    objects = models.storage.all()
                    the_obj = None
                    for obj in objects.keys():
                        if objects[obj].id == args[1]:
                            the_obj = objects[obj]
                            objects.pop(obj)
                            break
                    if the_obj:
                        del the_obj
                        models.storage.save()
                    else:
                        print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def do_all(self, line):
        '''Prints all the instances created for all classes or for some class
        '''
        args = line.split()
        if len(args) == 0:
            objects = models.storage.all()
            arr = []
            for obj in objects:
                arr.append(str(objects[obj]))
            print(arr)
        elif len(args) > 0:
            if args[0] in HBNBCommand.__classes:
                objects = models.storage.all()
                arr = []
                for obj in objects:
                    if objects[obj].to_dict()['__class__'] == args[0]:
                        arr.append(str(objects[obj]))
                print(arr)
            else:
                print("** class doesn't exist **")

    def do_update(self, line):
        '''Update some attributes of specific instances passed as arguments
        '''
        args = line.split()
        length = len(args)
        for i in range(length):
            if i >= len(args):
                break
            if args[i][0] == "\"" and args[i][len(args[i]) - 1] != "\"":
                j = i + 1
                indexes = []
                while args[j][len(args[j]) - 1] != "\"" and j < len(args):
                    args[i] += " "
                    args[i] += args[j]
                    indexes.append(j)
                    j = j + 1
                args[i] += " "
                args[i] += args[j]
                indexes.append(j)
                idx = 0
                for index in indexes:
                    args.pop(index - idx)
                    idx = idx + 1
                    i = i + 1
        for i in range(len(args)):
            args[i] = args[i].replace("\"", "")
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(args) < 2:
            print("** instance id missing **")
            return False
        objects = models.storage.all()
        the_obj = None
        for obj in objects.keys():
            if objects[obj].id == args[1]:
                the_obj = objects[obj]
                break
        if not the_obj:
            print("** no instance found **")
            return False
        if len(args) < 3:
            print("** attribute name missing **")
            return False
        if len(args) < 4:
            print("** value missing **")
            return False
        setattr(the_obj, args[2], args[3])
        models.storage.save()

    def default(self, line):
        '''Set default to catch other non-defined commands
        '''
        args = line.split(".")
        if args[0] in HBNBCommand.__classes:
            if args[1] == 'all()':
                self.do_all(args[0])
                return False
            if args[1] == 'count()':
                instances = models.storage.all()
                count = 0
                for instance in instances:
                    if instance.split(".")[0] == args[0]:
                        count += 1
                print(count)
                return False
            if args[1].split("(")[0] == 'show' and len(args[1]) > 4:
                if args[1].count("\"") != 2:
                    return False
                if args[1].split("(")[1][0] == '"':
                    length = len(args[1].split("(")[1]) - 1
                    if args[1].split("(")[1][length] == ')':
                        obj_id = args[1].replace("\"", "")
                        obj_id = obj_id.replace("show(", "")
                        obj_id = obj_id.replace(")", "")
                        self.do_show(args[0] + " " + obj_id)
                        return False
                elif args[1].split("(")[1][0] == ')':
                    self.do_show(args[0])
                    return False
                return False
            if args[1].split("(")[0] == 'destroy' and len(args[1]) > 7:
                if args[1].count("\"") != 2:
                    return False
                if args[1].split("(")[1][0] == '"':
                    length = len(args[1].split("(")[1]) - 1
                    if args[1].split("(")[1][length] == ')':
                        obj_id = args[1].replace("\"", "")
                        obj_id = obj_id.replace("destroy(", "")
                        obj_id = obj_id.replace(")", "")
                        self.do_destroy(args[0] + " " + obj_id)
                        return False
                elif args[1].split("(")[1][0] == ')':
                    self.do_destroy(args[0])
                    return False
                return False
            if args[1].split("(")[0] == 'update' and len(args[1]) > 6:
                ins = args[1].split("(")[1]
                inps = ins.split(", ")
                for i in range(len(inps)):
                    inps[i] = inps[i].replace(")", "")
                    inps[i] = inps[i].replace("\"", "")
                a = " "
                line = args[0] + a + inps[0] + a + inps[1] + a + inps[2]
                self.do_update(line)
                return False
        print(f"*** Unknown syntax: {line}")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
