import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    """Tests the module employee."""

    def setUp(self):
        """Create a made-up employee for testing purposes."""
        self.felipe = Employee('felipe', 'sebben', 65_000)

    def test_give_default_raise(self):
        """Test that the default salary raise works properly."""
        self.felipe.give_raise()
        self.assertEqual(self.felipe.salary, 70000)

    def test_give_custom_raise(self):
        """Test that custom raise works properly."""
        self.felipe.give_raise(10000)
        self.assertEqual(self.felipe.salary, 75000)


if __name__ == '__main__':
    unittest.main()
