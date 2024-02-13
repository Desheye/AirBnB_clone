import json
from models.base_model import BaseModel
from models.user import User

class FileStorage:
    __file_path = "file.json"
    __objects = {}
    classes = {
        "BaseModel": BaseModel,
        "User": User
    }

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as file:
            json.dump(obj_dict, file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as file:
                file_content = file.read()
                if file_content.strip() == "":
                    # File is empty, initialize __objects to an empty dictionary
                    self.__objects = {}
                else:
                    obj_dict = json.loads(file_content)
                    for key, value in obj_dict.items():
                        class_name, obj_id = key.split('.')
                        module = __import__('models.' + class_name.lower(), fromlist=[class_name])
                        class_ = getattr(module, class_name)
                        self.__objects[key] = class_(**value)
        except FileNotFoundError:
            pass

