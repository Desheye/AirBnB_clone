import cmd
from models import storage
from models.base_model import BaseModel
from datetime import datetime


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_all(self, arg):
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in storage.classes.keys():
            print("** class doesn't exist **")
            return

        objects = storage.all()
        class_objects = [str(obj) for obj in objects.values()
                         if obj.__class__.__name__ == class_name]
        print(class_objects)

    def do_show(self, arg):
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in storage.classes.keys():
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
            return
        print(objects[key])

    def do_create(self, arg):
        if not arg:
            print("** class name missing **")
            return
        if arg not in storage.classes:
            print("** class doesn't exist **")
            return

        new_obj = storage.classes[arg]()
        new_obj.save()
        print(new_obj.id)

    def do_destroy(self, arg):
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in storage.classes.keys():
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
            return
        del objects[key]
        storage.save()

    def do_update(self, arg):
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in storage.classes.keys():
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        setattr(objects[key], args[2], args[3])
        objects[key].save()

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
