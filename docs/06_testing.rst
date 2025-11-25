Testing
============================================

Verification of system behavior against requirements and specifications.

.. needtable::
   :filter: type == 'test'
   :columns: id;title;status;links;tags
   :style: table

The **AAA (Arrange–Act–Assert)** pattern is a structured way to write clear,
readable, and consistent unit tests. Each test is divided into three stages:

1. **Arrange** – Set up the data and environment for the test.
2. **Act** – Execute the code or function being tested.
3. **Assert** – Verify that the output is correct.

This pattern is primarily used for **unit tests**, which focus on isolated
functions or classes. Examples include testing a single function like to
ensure it produces the expected results.

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


.. testsetup:: *
   
   # Helper to run individual tests from test_controller.py
   #
   # This block is executed before every doctest in this file.
   # It makes the “run()” helper function and imports available to doctests
   # without exposing these lines as doctests themselves.

   import sys, os, unittest
   sys.path.insert(0, os.path.abspath('/workspace/src'))
   sys.path.insert(0, os.path.abspath('/workspace/tests'))

   import test_controller

   def run(test_name):
       suite = unittest.TestLoader().loadTestsFromName(test_name, module=test_controller)
       result = unittest.TextTestRunner(stream=open(os.devnull, 'w')).run(suite)
       return result.wasSuccessful()

LED Controller Unit Tests (Example)
-----------------------------------

This example demonstrates the **AAA pattern** applied to a real module from
the QuadLED project: the `LEDController` class.

The tests validate:

- default initialization
- valid power updates
- error conditions (invalid channel, invalid value)

.. test:: Initial power levels are zero for all channels
   :id: TEST_LEDCTRL_001
   :tags: unit, controller, power
   :links: SPEC_005, SPEC_010, REQ_020
   :status: implemented

   **Arrange:**  
   - Create a new `LEDController` instance with default 4 channels.

   **Act:**  
   - No action (initialization check).

   **Assert:**  
   - Channel 0 power equals `0`.  
   - Total number of channels equals `4`.

   **Autodoc Execution:**

   >>> run('TestLEDController.test_initial_power_levels')
   True

.. test:: Setting valid power updates channel correctly
   :id: TEST_LEDCTRL_002
   :tags: unit, controller, power
   :links: SPEC_005, SPEC_010
   :status: implemented

   **Arrange:**  
   - Create a new `LEDController`.

   **Act:**  
   - Call `set_power(2, 75)`.

   **Assert:**  
   - Channel 2 power equals `75`.

   **Autodoc Execution:**

   >>> run('TestLEDController.test_set_power_valid')
   True

.. test:: Setting power on invalid channel raises ValueError
   :id: TEST_LEDCTRL_003
   :tags: unit, controller, errors, validation
   :links: SPEC_005, SPEC_010
   :status: implemented

   **Arrange:**  
   - Create a new `LEDController`.

   **Act / Assert:**  
   - Calling `set_power(10, 50)` must raise `ValueError`.

   **Autodoc Execution:**

   >>> run('TestLEDController.test_set_power_invalid_channel')
   True

.. test:: Setting invalid power value raises ValueError
   :id: TEST_LEDCTRL_004
   :tags: unit, controller, errors, validation
   :links: SPEC_005, SPEC_010
   :status: implemented

   **Arrange:**  
   - Create a new `LEDController`.

   **Act / Assert:**  
   - Calling `set_power(1, 200)` must raise `ValueError`.

   **Autodoc Execution:**

   >>> run('TestLEDController.test_set_power_invalid_value')
   True
