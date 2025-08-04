# test_managerpackage.py
"""
Tests for ManagerPackage module.
"""

import unittest
from managerpackage import ManagerPackage

class TestManagerPackage(unittest.TestCase):
    """Test cases for ManagerPackage class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ManagerPackage()
        self.assertIsInstance(instance, ManagerPackage)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ManagerPackage()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
