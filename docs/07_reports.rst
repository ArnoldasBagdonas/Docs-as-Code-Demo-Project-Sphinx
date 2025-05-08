Reports
============================================

Pending Open Questions
--------------------------------------------

.. needtable::
   :status: review
   :columns: id;open_questions
   :style: table



.. raw:: latex
  
   \newpage


Risk Management Report
--------------------------------------------
Identify risks and document mitigation strategies.


.. raw:: latex
  
   \newpage


Progress Report
--------------------------------------------
Summarize the current project status, including milestones achieved and issues.

.. needpie:: Overall status
   :labels: open, review, in progress, closed
   :colors: #FFF4C2, #FAD390, #BFD8D2, #B0B0B0
   :style: docs/_static/styles/transparent.mplstyle

   status == 'open'
   status == 'review'
   status == 'in progress'
   status == 'closed'


.. raw:: latex
  
   \newpage


Traceability Report
--------------------------------------------
Trace all requirements to their implementation and test cases.

.. needtable::
   :columns: id;title;status;incoming;outgoing
   :style: table


.. needflow:: Traceability Report
   :config: lefttoright

