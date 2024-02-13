import unittest
from models.review import Review
from datetime import datetime

class TestReview(unittest.TestCase):
    """Test cases for Review class"""

    def setUp(self):
        self.review = Review()

    def test_attributes(self):
        """Test the attributes of the Review class"""
        self.assertTrue(hasattr(self.review, 'place_id'))
        self.assertTrue(hasattr(self.review, 'user_id'))
        self.assertTrue(hasattr(self.review, 'text'))
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

    def test_instance_type(self):
        """Test the instance type of Review"""
        self.assertIsInstance(self.review, Review)
        self.assertIsInstance(self.review.created_at, datetime)
        self.assertIsInstance(self.review.updated_at, datetime)

    def test_str_representation(self):
        """Test the __str__ method of Review"""
        expected_str = "[Review] ({}) {}".format(self.review.id, self.review.__dict__)
        self.assertEqual(str(self.review), expected_str)

    def test_to_dict_method(self):
        """Test the to_dict method of Review"""
        review_dict = self.review.to_dict()
        self.assertEqual(review_dict['__class__'], 'Review')
        self.assertIsInstance(review_dict['created_at'], str)
        self.assertIsInstance(review_dict['updated_at'], str)

if __name__ == '__main__':
    unittest.main()

