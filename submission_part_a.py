"""
CMSC 421 — Programming Assignment 2: Planning
Part (a): Blocks World Extension
--------------------------------

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

In this part, you will modify the simple Blocks World problem
to include an additional block D. Your task is to specify:

A planning problem PlanningProblem object, which defines
  • An initial state (with D under C)
  • A goal state (same as the original goal, but with D on top of C)
  • The available actions and their logical effects as a domain

You will then use the GraphPlan algorithm to find a valid plan.

This file also includes two blank pytest test stubs, which you must 
complete:
    1. Manual solution test (no GraphPlan)
    2. GraphPlan solution verification test
"""

import pytest
from planning import *
from logic import *


# ==============================================================
#  Part (a): Blocks World Extension
# ==============================================================

def blocksWorldExtension():
    """
    Part (a): Blocks World Extension
    --------------------------------
    Extend the simple Blocks World problem by adding a new block D.
    The goal is to modify the initial and goal states so that D becomes
    part of the tower.

    Original (3-block) problem:
        Initial: On(A, B) & Clear(A) & OnTable(B) & OnTable(C) & Clear(C)
        Goal:    On(B, A) & On(C, B)

    Extended problem (4-block):
        - Add block D under C in the initial state.
        - Update goal: D ends up on top of C (forming a 4-block tower).
        
    Return the planning problem object
    """

    # BEGIN_YOUR_CODE



    # END_YOUR_CODE


# ==============================================================
#  Pytest 1 — Manual Solution (No GraphPlan)
# ==============================================================

def test_blocksworld_extension_manual():
    """
    Manual solution for the Blocks World Extension.
    ------------------------------------------------
    Follow the style of test_blocksworld_manual() from test_graphplan.py.

    The goal is to manually apply actions using .act(expr(...))
    to demonstrate that the environment is solvable, without using GraphPlan.
    
    You should call your blocksWorldExtension() function defined above.
    You should assert conditions to validate the problem solvability.
    """

    # BEGIN_YOUR_CODE



    # END_YOUR_CODE


# ==============================================================
#  Pytest 2 — GraphPlan Verification
# ==============================================================

def test_blocksworld_extension_graphplan():
    """
    GraphPlan-based verification of the Blocks World Extension.
    ------------------------------------------------------------
    Use GraphPlan to find a valid plan automatically, then execute
    the resulting sequence to verify that it achieves the goal.
    
    You should call your blocksWorldExtension() function to get the
    problem. Then, execute GraphPlan and ensure solution is valid.
    """

    # BEGIN_YOUR_CODE



    # END_YOUR_CODE
