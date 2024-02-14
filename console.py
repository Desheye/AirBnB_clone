import cmd
from models import storage
from models.base_model import BaseModel
from datetime import datetime
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_all(self, arg):
        if not arg:
            print("** class name missing **")
            return
        
        class_name = arg.split()[0]
        if class_name not in ["BaseModel", "State", "City", "Place", "Amenity", "Review"]:
            print("** class doesn't exist **")
            return
        
        all_instances = storage.all(class_name)
        print(all_instances)
                
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
    
    def do_count(self, arg):
        if not arg:
            print("** class name missing **")
            return
        class_name = arg.split()[0]
        if class_name not in ["BaseModel", "State", "City", "Place", "Amenity", "Review", "User"]:
            print("** class doesn't exist **")
            return
        
        all_instances = storage.all(class_name)
        count = len(all_instances)
        print(count)

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
