Testing
============================================

Verifies system against requirements and specs.

The **AAA (Arrange–Act–Assert)** pattern is a structured way to write clear,
readable, and consistent unit tests. Each test is divided into three stages:

1. **Arrange** – Set up the data and environment for the test.
2. **Act** – Execute the code or function being tested.
3. **Assert** – Verify that the output is correct.

This pattern is primarily used for **unit tests**, which focus on isolated
functions or classes. Examples include testing a single function like `multiply`
to ensure it produces the expected results.

Integration Tests
-----------------

For **integration tests**, where multiple components interact (for example,
a service calling a database and an API), the AAA pattern can be adapted
or extended. Common guidelines include:

- **Arrange / Setup / GIVEN** – Prepare all necessary components, services,
  databases, or external APIs.
- **Act / Exercise / WHEN** – Execute the integrated functionality you want
  to test.
- **Assert / Verify / THEN** – Check that the results are correct across all
  interacting components.
- **Teardown / Cleanup** – Reset state, rollback databases, or stop services
  to avoid side effects on other tests.

Integration tests are generally heavier and slower than unit tests and may
require fixtures, mocks, or test containers to manage external dependencies.

Helper to run individual tests from test_controller.py
------------------------------

>>> import sys, os, unittest
>>> sys.path.insert(0, os.path.abspath('/workspace/src'))
>>> sys.path.insert(0, os.path.abspath('/workspace/tests'))
>>> import test_controller
>>> def run(test_name):
...     suite = unittest.TestLoader().loadTestsFromName(test_name, module=test_controller)
...     result = unittest.TextTestRunner(stream=open(os.devnull, 'w')).run(suite)
...     return result.wasSuccessful()


LED Controller Unit Tests (Example)
-----------------------------------

This example demonstrates the **AAA pattern** applied to a real module from
the QuadLED project: the `LEDController` class.

The tests validate:

- default initialization
- valid power updates
- error conditions (invalid channel, invalid value)

**test_initial_power_levels**

- **Arrange** – create a controller with default 4 channels
- **Act** – (no action)
- **Assert** – channel 0 power is `0` and total channels is `4`

>>> run('TestLEDController.test_initial_power_levels')
True

**test_set_power_valid**

- **Arrange** – create a controller
- **Act** – `set_power(2, 75)`
- **Assert** – channel 2 power equals `75`

>>> run('TestLEDController.test_set_power_valid')
True

**test_set_power_invalid_channel**

- **Arrange** – create a controller
- **Act / Assert** – calling `set_power(10, 50)` raises `ValueError`

>>> run('TestLEDController.test_set_power_invalid_channel')
True

**test_set_power_invalid_value**

- **Arrange** – create a controller
- **Act / Assert** – calling `set_power(1, 200)` raises `ValueError`

>>> run('TestLEDController.test_set_power_invalid_value')
True