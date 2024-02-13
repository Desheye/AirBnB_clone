import unittest
from models.state import State
from datetime import datetime

class TestState(unittest.TestCase):
    """Test cases for State class"""

    def setUp(self):
        self.state = State()

    def test_attributes(self):
        """Test the attributes of the State class"""
        self.assertTrue(hasattr(self.state, 'name'))
        self.assertEqual(self.state.name, "")

    def test_instance_type(self):
        """Test the instance type of State"""
        self.assertIsInstance(self.state, State)
        self.assertIsInstance(self.state.created_at, datetime)
        self.assertIsInstance(self.state.updated_at, datetime)

    def test_str_representation(self):
        """Test the __str__ method of State"""
        expected_str = "[State] ({}) {}".format(self.state.id, self.state.__dict__)
        self.assertEqual(str(self.state), expected_str)

    def test_to_dict_method(self):
        """Test the to_dict method of State"""
        state_dict = self.state.to_dict()
        self.assertEqual(state_dict['__class__'], 'State')
        self.assertIsInstance(state_dict['created_at'], str)
        self.assertIsInstance(state_dict['updated_at'], str)

if __name__ == '__main__':
    unittest.main()

