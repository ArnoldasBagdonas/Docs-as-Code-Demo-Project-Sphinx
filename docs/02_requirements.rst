Requirements
========================================================================================

What the system must do — functional and non-functional.

.. needtable::
   :filter: type == 'req'
   :columns: id;title;status;tags
   :style: table


Standards Compliance
----------------------------------------------------------------------------------------

Ensure adherence to relevant industry standards and regulations to guarantee safety,
reliability, and market eligibility.

.. req:: CE Compliance
   :id: REQ_001
   :tags: compliance, ce
   :status: closed

   - The LED Controller shall comply with applicable **CE marking directives**,
     particularly:
     
     - **Low Voltage Directive (2014/35/EU)**
     - **EMC Directive (2014/30/EU)**
     - **RoHS Directive (2011/65/EU)**
   
   - Compliance ensures electrical safety, electromagnetic compatibility, and
     restriction of hazardous substances for the European market.


.. req:: UL Certification
   :id: REQ_002
   :tags: compliance, ul
   :status: closed

   - The LED Controller must meet **UL 8750** requirements for LED equipment
     used in lighting products.
   - Certification ensures fire, electric shock, and mechanical safety for
     the U.S. and Canadian markets.
   - All critical components (e.g., power supply, housing, connectors) must
     also be UL-listed or -recognized where applicable.


.. raw:: latex
  
   \newpage


Functional Requirements
----------------------------------------------------------------------------------------

Define the core features and capabilities of the system.


.. req:: Multichannel LED Controller
   :id: REQ_003
   :tags: controller, channels
   :status: open

   - The controller shall support simultaneous control of up to **four
     independent LED channels**.

.. req:: Waveform Control
   :id: REQ_004
   :tags: controller, waveform
   :status: open

   - The controller shall support waveform control including **sine and
     square patterns** with adjustable frequency.


.. req:: Frequency Control
   :id: REQ_005
   :tags: controller, frequency
   :status: in progress

   - The controller shall support frequency adjustments between
     **0.001 Hz and 10,000 Hz** per channel.


.. req:: Output Power Control
   :id: REQ_006
   :tags: controller, power
   :status: in progress

   - The controller shall allow configurable **power output in five levels per channel**,
     supporting full-duty operation.


.. req:: Operating Time Control
   :id: REQ_007
   :tags: controller, timer
   :status: in progress

   - The controller shall support **count-up and countdown timers**, configurable
     in 1-second increments.


.. req:: Display Interface
   :id: REQ_008
   :tags: controller, ui
   :status: open

   - The controller shall include an onboard **display screen** that presents
     channel status, wavelength, stage, and timer info.


.. req:: Operating Settings Control
   :id: REQ_009
   :tags: controller, ui
   :status: open

   - The user shall be able to configure waveform, frequency, power stage, and
     timers prior to channel arming.


.. req:: Display Settings Control
   :id: REQ_010
   :tags: controller, ui
   :status: open

   - The interface shall allow the user to switch power display units, set background
     color based on wavelength, and display wavelength (in nm).


.. req:: Headless Operation
   :id: REQ_011
   :tags: controller, headless
   :status: open

   - Unit must also be able to operate headless-ly by receiving serial commands
     (device control without display/buttons) from external devices communicating
     over the same Client-defined protocol


.. req:: Fan Control
   :id: REQ_012
   :tags: controller, cooling
   :status: open

   - The controller shall supply **continuous power to fans on all connected
     LED panels while powered on**.


.. req:: Physical Power Switch
   :id: REQ_013
   :tags: controller, switch
   :status: open

   - The controller shall include a **physical on/off switch** on the enclosure.


.. req:: Channel Cycle Button
   :id: REQ_014
   :tags: controller, ui
   :status: open

   - The controller shall include a button to cycle through channels 1–4.


.. req:: Control Buttons
   :id: REQ_015
   :tags: controller, ui
   :status: open

   - The controller shall include **analog buttons or dial** for input and control of
     all settings and operations.


.. req:: Audio Feedback
   :id: REQ_016
   :tags: controller, ui, audio, safety
   :status: open

   - Upon firing a channel, the controller shall emit an **audible warning tone**.


.. req:: Desktop Application Communication
   :id: REQ_017
   :tags: controller, desktop, usb
   :status: open

   - The controller shall support **USB/UART** communication with a desktop application.


.. req:: I2C Communication with LED Panels
   :id: REQ_018
   :tags: controller, led, i2c
   :status: open

   - The controller shall use the **I2C protocol** to communicate with attached LED panels
     for control and calibration.


.. req:: Debug Communication Interface
   :id: REQ_019
   :tags: controller, debug
   :status: open

   - The controller shall include a debug interface for **firmware updates via debugger**.


.. raw:: latex
  
   \newpage


Non-functional Requirements
----------------------------------------------------------------------------------------

Define performance and operational characteristics essential for system success.


.. req:: Backward Compatibility with LED Panels
   :id: REQ_020
   :tags: compatibility, led
   :status: open

   - The controller shall retain full compatibility with all existing LED devices.
   - Calibration data, configuration settings, and model information shall be readable
     from legacy hardware.


.. req:: EEPROM Compatibility
   :id: REQ_021
   :tags: compatibility, eeprom
   :status: open

   - The controller shall use the same EEPROM device format and maintain read/write
     functionality.


.. req:: Design Reference Support
   :id: REQ_022
   :tags: validation
   :status: open

   - The Client shall provide LED panels and current-generation controllers for
     validation and design comparison.


.. req:: Developer Documentation
   :id: REQ_023
   :tags: documentation
   :status: open

   - The Contractor shall deliver firmware documentation and training materials
     suitable for developer onboarding and customer support.
