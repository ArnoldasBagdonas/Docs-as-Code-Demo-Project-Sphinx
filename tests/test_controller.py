# tests/test_my_module.py
import sys
import os

# Add the src/ directory relative to this test file
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import unittest
from quadled.controller import LEDController

class TestLEDController(unittest.TestCase):

    def test_initial_power_levels(self):
        # Arrange
        ctrl = LEDController()

        # Act
        # No actions, testing initial state

        # Assert
        self.assertEqual(ctrl.get_power(0), 0)
        self.assertEqual(ctrl.channels, 4)

    def test_set_power_valid(self):
        # Arrange
        ctrl = LEDController()

        # Act
        ctrl.set_power(2, 75)

        # Assert
        self.assertEqual(ctrl.get_power(2), 75)

    def test_set_power_invalid_channel(self):
        # Arrange
        ctrl = LEDController()

        # Act / Assert
        with self.assertRaises(ValueError):
            ctrl.set_power(10, 50)

    def test_set_power_invalid_value(self):
        # Arrange
        ctrl = LEDController()

        # Act / Assert
        with self.assertRaises(ValueError):
            ctrl.set_power(1, 200)
