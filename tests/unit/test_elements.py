"""Unit tests for Thingery elements module"""
import unittest
from thingery.elements import ELEMENTS, Element


class TestElements(unittest.TestCase):
    """Test cases for elements module"""
    
    def test_elements_exist(self):
        """Test that core elements exist"""
        self.assertIn("H", ELEMENTS)
        self.assertIn("He", ELEMENTS)
        self.assertIn("C", ELEMENTS)
        self.assertIn("N", ELEMENTS)
        self.assertIn("O", ELEMENTS)
    
    def test_hydrogen_properties(self):
        """Test hydrogen element properties"""
        h = ELEMENTS["H"]
        self.assertEqual(h.name, "Hydrogen")
        self.assertEqual(h.number, 1)
        self.assertIsNotNone(h.atomic_mass)
    
    def test_carbon_properties(self):
        """Test carbon element properties"""
        c = ELEMENTS["C"]
        self.assertEqual(c.name, "Carbon")
        self.assertEqual(c.number, 6)
    
    def test_all_elements_have_symbol(self):
        """Test all elements have valid symbol"""
        for symbol, element in ELEMENTS.items():
            self.assertTrue(len(symbol) in (1, 2, 3))
            self.assertIsNotNone(element.name)
            self.assertIsNotNone(element.number)


class TestElement(unittest.TestCase):
    """Test cases for Element dataclass"""
    
    def test_element_creation(self):
        """Test creating an Element"""
        el = Element(
            name="Testium",
            symbol="Te",
            number=123,
            atomic_mass=123.45
        )
        self.assertEqual(el.name, "Testium")
        self.assertEqual(el.symbol, "Te")
        self.assertEqual(el.number, 123)


if __name__ == "__main__":
    unittest.main()
