import unittest
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def test_init_without_args(self):
        # Test initialization without arguments
        model = BaseModel()
        self.assertTrue(hasattr(model, 'id'))
        self.assertTrue(hasattr(model, 'created_at'))
        self.assertTrue(hasattr(model, 'updated_at'))
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_init_with_args(self):
        # Test initialization with arguments
        created_at = '2024-01-01T12:00:00.000000'
        updated_at = '2024-01-02T12:00:00.000000'
        model = BaseModel(created_at=created_at, updated_at=updated_at)
        self.assertEqual(model.created_at, datetime.strptime(created_at, '%Y-%m-%dT%H:%M:%S.%f'))
        self.assertEqual(model.updated_at, datetime.strptime(updated_at, '%Y-%m-%dT%H:%M:%S.%f'))

    def test_str_representation(self):
        # Test string representation
        model = BaseModel()
        expected_str = f"[BaseModel] ({model.id}) {model.__dict__}"
        self.assertEqual(str(model), expected_str)

    def test_save_method(self):
        # Test save method
        model = BaseModel()
        initial_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(model.updated_at, initial_updated_at)

    def test_to_dict_method(self):
        # Test to_dict method
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertIn('__class__', model_dict)
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertIsInstance(model_dict['id'], str)
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)
        self.assertEqual(model_dict['id'], model.id)
        self.assertEqual(model_dict['created_at'], model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], model.updated_at.isoformat())

if __name__ == '__main__':
    unittest.main()

