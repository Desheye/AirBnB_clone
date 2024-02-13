import unittest
from models.amenity import Amenity
from datetime import datetime

class TestAmenity(unittest.TestCase):
    """Test cases for Amenity class"""

    def setUp(self):
        self.amenity = Amenity()

    def test_attributes(self):
        """Test the attributes of the Amenity class"""
        self.assertTrue(hasattr(self.amenity, 'name'))
        self.assertEqual(self.amenity.name, "")

    def test_instance_type(self):
        """Test the instance type of Amenity"""
        self.assertIsInstance(self.amenity, Amenity)
        self.assertIsInstance(self.amenity.created_at, datetime)
        self.assertIsInstance(self.amenity.updated_at, datetime)

    def test_str_representation(self):
        """Test the __str__ method of Amenity"""
        expected_str = "[Amenity] ({}) {}".format(self.amenity.id, self.amenity.__dict__)
        self.assertEqual(str(self.amenity), expected_str)

    def test_to_dict_method(self):
        """Test the to_dict method of Amenity"""
        amenity_dict = self.amenity.to_dict()
        self.assertEqual(amenity_dict['__class__'], 'Amenity')
        self.assertIsInstance(amenity_dict['created_at'], str)
        self.assertIsInstance(amenity_dict['updated_at'], str)

if __name__ == '__main__':
    unittest.main()

