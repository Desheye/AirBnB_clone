import unittest
from datetime import datetime
from models.base_model import BaseModel, MyModel

class TestBaseModel(unittest.TestCase):
    def test_attributes_initialized(self):
        my_model = MyModel(89, "My First Model")
        self.assertTrue(hasattr(my_model, 'id'))
        self.assertTrue(hasattr(my_model, 'created_at'))
        self.assertTrue(hasattr(my_model, 'updated_at'))
        self.assertTrue(hasattr(my_model, 'my_number'))
        self.assertTrue(hasattr(my_model, 'name'))

    def test_to_dict(self):
        my_model = MyModel(89, "My First Model")
        my_model_dict = my_model.to_dict()

        self.assertIsInstance(my_model_dict, dict)
        self.assertIn('my_number', my_model_dict)
        self.assertIn('name', my_model_dict)
        self.assertIn('__class__', my_model_dict)
        self.assertIn('updated_at', my_model_dict)
        self.assertIn('id', my_model_dict)
        self.assertIn('created_at', my_model_dict)

        # Check if __class__ is a string
        self.assertIsInstance(my_model_dict['__class__'], str)

        # Check other attributes
        self.assertIsInstance(my_model_dict['my_number'], tuple)
        self.assertIsInstance(my_model_dict['name'], tuple)
        self.assertIsInstance(my_model_dict['updated_at'], tuple)
        self.assertIsInstance(my_model_dict['id'], tuple)
        self.assertIsInstance(my_model_dict['created_at'], tuple)

        # Check if datetime strings can be parsed
        parsed_created_at = datetime.strptime(my_model_dict['created_at'][1], '%Y-%m-%dT%H:%M:%S.%f')
        parsed_updated_at = datetime.strptime(my_model_dict['updated_at'][1], '%Y-%m-%dT%H:%M:%S.%f')
        self.assertIsInstance(parsed_created_at, datetime)
        self.assertIsInstance(parsed_updated_at, datetime)

if __name__ == '__main__':
    unittest.main()

