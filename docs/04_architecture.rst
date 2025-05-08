Architecture
========================================================================================
High-level system structure and how components interact.

.. needtable::
   :filter: type == 'arch'
   :columns: id;title;status;tags
   :style: table


.. raw:: latex
  
   \newpage


Logical View
----------------------------------------------------------------------------------------
Describes functionality — what the system should do.
(Example: modules - UI handling, LED PWM control, Fan management, Settings storage)

.. arch:: Logical View - LED Controller
   :id: ARCH_001
   :tags: controller, interfaces, ui, hardware
   :links: SPEC_001, SPEC_002, SPEC_003, SPEC_004, SPEC_007, SPEC_008, 
   :status: review
   :open_questions: Headless operation lacks definition!


   .. image:: _static/images/diagrams/LogicalViewLEDController.drawio.png
      :align: center
      :alt: Logical View


.. arch:: Logical View - Desktop Application
   :id: ARCH_002
   :tags: controller, interfaces, ui, hardware
   :status: open
   :open_questions: Headless operation lacks definition!


   .. image:: _static/images/diagrams/LogicalViewDesktopApplication.drawio.png
      :align: center
      :alt: Logical View


.. raw:: latex
  
   \newpage


Development View
----------------------------------------------------------------------------------------
Describes software structure in terms of modules and components.
(Example: source code organized into drivers, middleware, app layer, HAL)

.. arch:: Development View
   :id: ARCH_003
   :tags: actors,user
   :status: open

   
   .. image:: _static/images/diagrams/ViewPlaceholder.drawio.png
      :width: 800
      :align: center
      :alt: Development View


.. raw:: latex
  
   \newpage


Process View
----------------------------------------------------------------------------------------
Describes dynamic behavior, concurrency, and runtime performance.
(Example: real-time tasks for LED control, UI input polling, serial communication)

.. arch:: Process View
   :id: ARCH_004
   :tags: actors,user
   :status: open


   .. image:: _static/images/diagrams/ViewPlaceholder.drawio.png
      :width: 800
      :align: center
      :alt: Process View


.. raw:: latex
  
   \newpage


Physical View
----------------------------------------------------------------------------------------
Describes the deployment — how components are mapped to hardware.
(Example: mapping of firmware to MCU hardware, I2C buses to peripherals, power domains)

.. arch:: Physical View
   :id: ARCH_005
   :tags: actors,user
   :status: open


   .. image:: _static/images/diagrams/ViewPlaceholder.drawio.png
      :width: 800
      :align: center
      :alt: Physical View


.. raw:: latex
  
   \newpage


Scenarios
----------------------------------------------------------------------------------------
Shows use cases or sequences that validate and illustrate the other views.
(Example: sequence diagrams for "user presses power button" or "desktop app changes settings")