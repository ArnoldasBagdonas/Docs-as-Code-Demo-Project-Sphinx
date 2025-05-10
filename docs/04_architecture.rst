Architecture
========================================================================================
High-level system structure and how components interact.

.. needtable::
   :filter: type == 'arch' or type == 'feat'
   :columns: id;title;status;tags
   :style: table


.. raw:: latex
  
   \newpage

LED Controller
----------------------------------------------------------------------------------------

Logical View
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Describes functionality — what the system should do.
(Example: modules - UI handling, LED PWM control, Fan management, Settings storage)

.. arch:: LED Controller - Logical View
   :id: ARCH_001
   :tags: controller, interfaces, ui, hardware
   :links: ARCH_004, ARCH_005
   :status: review
   :open_questions: Headless operation lacks definition!


   .. image:: _static/images/diagrams/LEDControllerLogicalView.drawio.png
      :align: center
      :alt: Logical View



Process View
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Describes dynamic behavior, concurrency, and runtime performance.
(Example: real-time tasks for LED control, UI input polling, serial communication)

.. arch:: LED Controller - Process View
   :id: ARCH_004
   :tags: actors,user
   :links: REQ_003, SPEC_003, REQ_007, SPEC_007, SPEC_008, SPEC_009, SPEC_010, SPEC_011, FEAT_001
   :status: open

   
   .. image:: _static/images/diagrams/LEDControllerProcessView.drawio.png
      :width: 800
      :align: center
      :alt: Development View



.. raw:: latex
  
   \newpage


Features
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Shows use cases or sequences that validate and illustrate the other views.
(Example: sequence diagrams for "user presses power button" or "desktop app changes settings")


.. feat:: LED Controller - Features
   :id: FEAT_001
   :tags: actors,user
   :status: open


   TBD


Development View
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Describes software structure in terms of modules and components.
(Example: source code organized into drivers, middleware, app layer, HAL)

.. arch:: LED Controller - Development View
   :id: ARCH_003
   :tags: actors,user
   :links: ARCH_001
   :status: open

   
   .. image:: _static/images/diagrams/ViewPlaceholder.drawio.png
      :width: 800
      :align: center
      :alt: Development View


.. raw:: latex
  
   \newpage


Physical View
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Describes the deployment — how components are mapped to hardware.
(Example: mapping of firmware to MCU hardware, I2C buses to peripherals, power domains)

.. arch:: LED Controller - Physical View
   :id: ARCH_005
   :tags: actors,user
   :links: SPEC_006, SPEC_001, SPEC_002, SPEC_004, SPEC_012, REQ_001, REQ_002, SPEC_010
   :status: open


   .. image:: _static/images/diagrams/ViewPlaceholder.drawio.png
      :width: 800
      :align: center
      :alt: Physical View


.. raw:: latex
  
   \newpage


Desktop Application
----------------------------------------------------------------------------------------

Logical View
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Describes functionality — what the system should do.
(Example: modules - UI handling, LED PWM control, Fan management, Settings storage)

.. arch:: Desktop Application - Logical View
   :id: ARCH_002
   :tags: controller, interfaces, ui, hardware
   :links: FEAT_002
   :status: open
   :open_questions: Headless operation lacks definition!


   .. image:: _static/images/diagrams/DesktopApplicationLogicalView.drawio.png
      :align: center
      :alt: Logical View


.. raw:: latex
  
   \newpage



Features
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Shows use cases or sequences that validate and illustrate the other views.
(Example: sequence diagrams for "user presses power button" or "desktop app changes settings")


.. feat:: Desktop Application - Features
   :id: FEAT_002
   :tags: actors,user
   :status: open


   TBD
