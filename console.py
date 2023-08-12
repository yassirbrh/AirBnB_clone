#!/usr/bin/env python3
'''
    Modules Importation
'''
import cmd


class HBNBCommand(cmd.Cmd):
    '''
        Definition of the class HBNBCommand inheriting from cmd.Cmd
    '''
    prompt = '(hbnb) '

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
