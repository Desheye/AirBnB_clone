import uuid
from datetime import datetime
from collections import OrderedDict

class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        obj_dict = OrderedDict()
        obj_dict['__class__'] = self.__class__.__name__  # Add __class__ attribute
        obj_dict['id'] = (type(self.id).__name__, self.id)
        obj_dict['created_at'] = (type(self.created_at).__name__, self.created_at.isoformat())
        obj_dict['updated_at'] = (type(self.updated_at).__name__, self.updated_at.isoformat())
        return obj_dict

class MyModel(BaseModel):
    def __init__(self, my_number, name):
        super().__init__()
        self.my_number = my_number
        self.name = name

    def to_dict(self):
        obj_dict = super().to_dict()
        obj_dict['my_number'] = (type(self.my_number).__name__, self.my_number)
        obj_dict['name'] = (type(self.name).__name__, self.name)
        return obj_dict

