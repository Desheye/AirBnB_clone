import unittest
from models.city import City
from datetime import datetime

class TestCity(unittest.TestCase):
    """Test cases for City class"""

    def setUp(self):
        self.city = City()

    def test_attributes(self):
        """Test the attributes of the City class"""
        self.assertTrue(hasattr(self.city, 'state_id'))
        self.assertEqual(self.city.state_id, "")
        self.assertTrue(hasattr(self.city, 'name'))
        self.assertEqual(self.city.name, "")

    def test_instance_type(self):
        """Test the instance type of City"""
        self.assertIsInstance(self.city, City)
        self.assertIsInstance(self.city.created_at, datetime)
        self.assertIsInstance(self.city.updated_at, datetime)

    def test_str_representation(self):
        """Test the __str__ method of City"""
        expected_str = "[City] ({}) {}".format(self.city.id, self.city.__dict__)
        self.assertEqual(str(self.city), expected_str)

    def test_to_dict_method(self):
        """Test the to_dict method of City"""
        city_dict = self.city.to_dict()
        self.assertEqual(city_dict['__class__'], 'City')
        self.assertIsInstance(city_dict['created_at'], str)
        self.assertIsInstance(city_dict['updated_at'], str)

if __name__ == '__main__':
    unittest.main()

