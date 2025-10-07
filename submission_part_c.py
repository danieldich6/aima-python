"""
CMSC 421 — Programming Assignment 2: Planning
Part (c): Introducing Time Resources
------------------------------------

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

In this part, you will extend your logistics domain to include
non-uniform time costs. You will simulate cumulative time resources
and ensure your plan respects a total time constraint.

Time costs:
  • D1 → D2: 3 time units
  • D2 → D3: 5 time units
  • D1 → D3: 10 time units
  • Load: 1 time unit
  • Unload: 1 time unit

Problem setup:
  • Initial state: same as in part (b), with CurrentTime(0)
  • Goal: all containers at D3
  • Constraint: total time ≤ 50 units

You will implement:
  • A planning problem that tracks cumulative time costs.
  • A manual solution test showing how time accumulates.
  • A GraphPlan-based test verifying a valid plan completes within time limit.
"""

import pytest
from planning import *
from logic import *


# ==============================================================
#  Part (c): Logistics Domain with Time Resources
# ==============================================================

def logisticsDomainWithTime():
    """
    Part (c): Introducing Time Resources
    ------------------------------------
    Extends the logistics domain by including cumulative time tracking
    for each action. Each move or load/unload action increases the time
    counter according to specified costs. The plan must complete within
    50 total time units.
    """

    # BEGIN_YOUR_CODE



    # END_YOUR_CODE


# ==============================================================
#  Pytest 1 — Manual Solution (No GraphPlan)
# ==============================================================

def test_logistics_time_manual():
    """
    Manual test with cumulative time tracking.
    ------------------------------------------
    Executes the plan:
        [Move_D1_D2(R1, 0),
         Unload(R1, C1, D1, 0),
         Load(R1, C3, D2, 0),
         Move_D2_D3(R1, 0),
         Load(R1, C2, D1, 0),
         Unload(R1, C3, D3, 0),
         Unload(R1, C2, D3, 0),
         Unload(R1, C1, D3, 0)]

    This sequence simulates a valid execution respecting the
    non-uniform time costs defined in the domain.
    """

    # BEGIN_YOUR_CODE



    # END_YOUR_CODE

# ==============================================================
#  Pytest 2 — GraphPlan Verification with Time
# ==============================================================

def test_logistics_time_graphplan():
    """
    GraphPlan-based verification for the time-extended logistics domain.
    --------------------------------------------------------------------
    Run GraphPlan to automatically find a plan that respects time costs
    and verify it completes within the allowed 50 time units.
    """

    # BEGIN_YOUR_CODE



    # END_YOUR_CODE
