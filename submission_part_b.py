"""
CMSC 421 — Programming Assignment 2: Planning
Part (b): Logistics Domain
--------------------------

# ==============================================================
#  Note to Students
# ==============================================================

You are expected to take some time to explore the repository in order
to understand the syntax and structure of the provided codebase. This
is an excellent opportunity to practice reading and reasoning about
existing code — a skill that is crucial in research and industry alike,
where you'll often need to extend or modify large, mature projects.

Hint:
    The most relevant files to review before beginning this part are:
        • planning.py
        • tests/test_planning.py
        • tests/test_graphplan.py

# ==============================================================

In this part, you will formulate a new planning problem for the
Logistics Domain, in which a robot must move several containers
between destinations.

You will implement:
  • A PlanningProblem object for the logistics setup.
  • A manual solution that demonstrates solvability.
  • A GraphPlan-based test verifying that the planner finds a valid plan.

Your domain should include:
  • Bidirectional adjacency between destinations (i.e., roads are two-way).
  • Precondition and effect logic for moving, loading, and unloading actions.
"""

import pytest
from planning import *
from logic import *


# ==============================================================
#  Part (b): Logistics Domain
# ==============================================================

def logisticsDomain():
    """
    Part (b): Logistics Domain
    --------------------------
    Define a logistics planning problem in which a single robot (R1)
    moves containers (C1, C2, C3) between destinations (D1, D2, D3).

    The robot can move between adjacent destinations, pick up a container,
    and put down a container, but can carry only one at a time.

    Initial State:
        R1 at D1
        C1 loaded on R1
        C2 at D1
        C3 at D2

    Goal State:
        All containers at D3
        
    Return the planning problem object
    """

    # BEGIN_YOUR_CODE



    # END_YOUR_CODE


# ==============================================================
#  Pytest 1 — Manual Solution (No GraphPlan)
# ==============================================================

def test_logistics_domain_manual():
    """
    Manual solution for the Logistics Domain.
    -----------------------------------------
    Follow the style of test_logistics_manual() from test_graphplan.py.

    The goal is to manually apply actions using .act(expr(...))
    to demonstrate that the environment is solvable, without using GraphPlan.
    
    You should generate a problem with the function defined above.
    You should assert conditions to validate the problem solvability.
    """

    # BEGIN_YOUR_CODE



    # END_YOUR_CODE


# ==============================================================
#  Pytest 2 — GraphPlan Verification
# ==============================================================

def test_logistics_domain_graphplan():
    """
    GraphPlan-based verification of the Logistics Domain.
    -----------------------------------------------------
    Use GraphPlan to find a valid plan automatically, then execute
    the resulting sequence to verify that it achieves the goal.
    
    You should call the problem constructor function to get the
    problem. Then, execute GraphPlan and ensure solution is valid.
    """

    # BEGIN_YOUR_CODE



    # END_YOUR_CODE
