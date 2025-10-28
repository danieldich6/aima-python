"""
CMSC 421 — Assignment 3: Representation & Planning
--------------------------------

# ==============================================================
#  Preface to Students
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

In this assignment, you will complete a custom rush-hour domain 
definition. Then, you will reason about plans in this domain.
"""

import pytest
from planning import *
from logic import *

"""
PART A: Implement Actions & Domain Components

You must implement the necessary remaining three actions:
 - 'MoveLeft(c, frm, to)'
 - 'MoveUp(c, frm, to)'
 - 'MoveDown(c, frm, to)'
Be careful - this code is case sensitive.

Next, implement the 'AdjacentUp' domain definitions. Don't
overthink, this part is simple. 

At this point, the rush_hour_4x4 function should return a
PlanningProblem object successfully.

Ensure your solution to this is correct, as the following
parts build upon this function.
"""

def rush_hour_4x4(initial, goals, domain):
    """
    Simplified 4x4 grid-shape rush_hour domain.
    
    This domain does not have 'cars' and 'trucks', etc. as in the
    original Rush Hour game. Instead, every vehicle is a 'Car' that
    exists in only one cell.
    
    We define arbitrary start and goal states. The car doesn't 
    have an exit lane, rather we define a goal cell and consider
    the problem solved when it reaches it.
    """
        
    return PlanningProblem(
        initial=expr(initial),
        goals=expr(goals),
        actions=[
            # --- Horizontal moves ---
            Action('MoveRight(c, frm, to)',
                precond=expr('At(c, frm) & Clear(to) & Horizontal(c) & AdjacentRight(frm, to)'),
                effect=expr('At(c, to) & Clear(frm) & ~At(c, frm) & ~Clear(to)'),
                domain=expr('Car(c) & Cell(frm) & Cell(to) & AdjacentRight(frm, to)')),
            
            # BEGIN_YOUR_CODE
            Action('MoveLeft(c, frm, to)',
                precond=expr('At(c, frm) & Clear(to) & Horizontal(c) & AdjacentLeft(frm, to)'),
                effect=expr('At(c, to) & Clear(frm) & ~At(c, frm) & ~Clear(to)'),
                domain=expr('Car(c) & Cell(frm) & Cell(to) & AdjacentLeft(frm, to)')),

            Action('MoveUp(c, frm, to)',
                precond=expr('At(c, frm) & Clear(to) & Vertical(c) & AdjacentUp(frm, to)'),
                effect=expr('At(c, to) & Clear(frm) & ~At(c, frm) & ~Clear(to)'),
                domain=expr('Car(c) & Cell(frm) & Cell(to) & AdjacentUp(frm, to)')),

            Action('MoveDown(c, frm, to)',
                precond=expr('At(c, frm) & Clear(to) & Vertical(c) & AdjacentDown(frm, to)'),
                effect=expr('At(c, to) & Clear(frm) & ~At(c, frm) & ~Clear(to)'),
                domain=expr('Car(c) & Cell(frm) & Cell(to) & AdjacentDown(frm, to)')),
                        
            
            # END_YOUR_CODE
            
        ],
        domain=expr(
            # --- Car definitions ---
            domain + ' & '
            
            # --- Cell definitions ---
            'Cell(C1_1) & Cell(C1_2) & Cell(C1_3) & Cell(C1_4) & '
            'Cell(C2_1) & Cell(C2_2) & Cell(C2_3) & Cell(C2_4) & '
            'Cell(C3_1) & Cell(C3_2) & Cell(C3_3) & Cell(C3_4) & '
            'Cell(C4_1) & Cell(C4_2) & Cell(C4_3) & Cell(C4_4) & '
            
            # --- Adjacency (complete, propositional) ---
            'AdjacentRight(C1_1, C1_2) & AdjacentRight(C1_2, C1_3) & AdjacentRight(C1_3, C1_4) & '
            'AdjacentRight(C2_1, C2_2) & AdjacentRight(C2_2, C2_3) & AdjacentRight(C2_3, C2_4) & '
            'AdjacentRight(C3_1, C3_2) & AdjacentRight(C3_2, C3_3) & AdjacentRight(C3_3, C3_4) & '
            'AdjacentRight(C4_1, C4_2) & AdjacentRight(C4_2, C4_3) & AdjacentRight(C4_3, C4_4) & '
            'AdjacentLeft(C1_2, C1_1) & AdjacentLeft(C1_3, C1_2) & AdjacentLeft(C1_4, C1_3) & '
            'AdjacentLeft(C2_2, C2_1) & AdjacentLeft(C2_3, C2_2) & AdjacentLeft(C2_4, C2_3) & '
            'AdjacentLeft(C3_2, C3_1) & AdjacentLeft(C3_3, C3_2) & AdjacentLeft(C3_4, C3_3) & '
            'AdjacentLeft(C4_2, C4_1) & AdjacentLeft(C4_3, C4_2) & AdjacentLeft(C4_4, C4_3) & '
            'AdjacentDown(C1_1, C2_1) & AdjacentDown(C2_1, C3_1) & AdjacentDown(C3_1, C4_1) & '
            'AdjacentDown(C1_2, C2_2) & AdjacentDown(C2_2, C3_2) & AdjacentDown(C3_2, C4_2) & '
            'AdjacentDown(C1_3, C2_3) & AdjacentDown(C2_3, C3_3) & AdjacentDown(C3_3, C4_3) & '
            'AdjacentDown(C1_4, C2_4) & AdjacentDown(C2_4, C3_4) & AdjacentDown(C3_4, C4_4) & '
            
            # BEGIN_YOUR_CODE
            'AdjacentUp(C2_1, C1_1) & AdjacentUp(C3_1, C2_1) & AdjacentUp(C4_1, C3_1) & '
            'AdjacentUp(C2_2, C1_2) & AdjacentUp(C3_2, C2_2) & AdjacentUp(C4_2, C3_2) & '
            'AdjacentUp(C2_3, C1_3) & AdjacentUp(C3_3, C2_3) & AdjacentUp(C4_3, C3_3) & '
            'AdjacentUp(C2_4, C1_4) & AdjacentUp(C3_4, C2_4) & AdjacentUp(C4_4, C3_4)'
            
            
            # END_YOUR_CODE
        )
    ) 


# ==============================================================
# The following functions initialize a Planning Problem with the
# associated task. No work is necessary here, but familiarize 
# yourself with the tasks specified.
# ==============================================================
def simple_rush_hour_task():

    initial = ('At(R, C3_2) & At(B1, C1_3) & At(B2, C1_1) & '
            'Clear(C1_2) & Clear(C1_4) & Clear(C2_1) & '
            'Clear(C2_2) & Clear(C2_3) & Clear(C2_4) & '
            'Clear(C3_1) & Clear(C3_3) & Clear(C3_4) & '
            'Clear(C4_1) & Clear(C4_2) & Clear(C4_3) & '
            'Clear(C4_4)'
            )
    goals = 'At(R, C3_4)'
    domain = ('Car(R) & Car(B1) & Car(B2) & '
            'Horizontal(R) & Horizontal(B2) & Vertical(B1)')
    
    return rush_hour_4x4(initial, goals, domain)

def complex_rush_hour_task():
   
    initial = (
        'At(R, C4_1) & At(A, C4_2) & At(B, C4_3) & '
        'At(C, C3_3) & At(D, C3_2) & At(E, C3_4) & '
        'Clear(C1_1) & Clear(C1_2) & Clear(C1_3) & '
        'Clear(C1_4) & Clear(C2_1) & Clear(C2_2) & '
        'Clear(C2_3) & Clear(C2_4) & Clear(C3_1) & '
        'Clear(C4_4)'
    )
    
    goals = "At(R, C4_4)"
    
    domain = (
        'Car(R) & Car(A) & Car(B) & Car(C) & Car(D) & Car(E) & '
        'Horizontal(R) & Vertical(A) & Vertical(B) & Horizontal(C) & Vertical(D) & Vertical(E)'
    )   
    
    return rush_hour_4x4(initial, goals, domain)
   
"""
PART B — Manual Solutions

Return a list of strings that represents a solution to each of the 
problems above. Ensure that the goal is reached ONLY by the final 
action. I.e. do not continue performing actions after the goal is 
reached, even if you maintain goal satisfaction. Do not include
persistence actions - i.e. the solution should only contain strings
that represent the actions defined in the PlanningProblem object.

The functions listed below should each return the requested format 
for each of the tasks above respectively:
 - simple_rush_hour_manual()
 - complex_rush_hour_manual()

E.g. 
```
>>> simple_rush_hour_manual()
['MoveUp(A, C3_1, C2_1)', ...]
```
Note - the above example is not correct, and is nonsensical for this task.
"""

def simple_rush_hour_manual():

    # BEGIN_YOUR_CODE
    
    return [    'MoveRight(R, C3_2, C3_3)',
        'MoveRight(R, C3_3, C3_4)']

    # END_YOUR_CODE


def complex_rush_hour_manual():

    # BEGIN_YOUR_CODE
    
    return ['MoveUp(E, C3_4, C2_4)',
        'MoveRight(C, C3_3, C3_4)',
        'MoveUp(B, C4_3, C3_3)',
        'MoveUp(D, C3_2, C2_2)',
        'MoveUp(A, C4_2, C3_2)',
        'MoveRight(R, C4_1, C4_2)',
        'MoveRight(R, C4_2, C4_3)',
        'MoveRight(R, C4_3, C4_4)']

    # END_YOUR_CODE 


"""
PART C -- GraphPlan

In this part, you will run a planner upon the tasks defined above
and return two things - a partial plan, and a linearized plan.

In particular, you will run the GraphPlan algorithm to get the
partial order plan, and the Linearize wrapper to get the 
total order plan. Both take a Planning Problem as input, and
must have the execute() method called to get the solutions.

Return two things in the following order:
 - 1. a list of lists of utils.Expr objects, which represents layers
      of actions that can be concurrently executed. This 
      will be a single partial plan solution, but you may need 
      to coax it into this format. Note - it's okay if you
      leave persistence actions in this output.
 - 2. a list of utils.Expr objects, which represents a total order 
      plan that solves the task. Again, ensure correct 
      formatting.
i.e. return it as `return a, b`
Note - utils.Expr objects are natively returned within the DS' returned
by functions listed above - so this representation is convenient.
      
Hints
 - See the files mentioned in the preface for partial examples.
 - This code should be short. You just need to instantiate a 
   planning problem, execute GraphPlan and Linearize (1 line
   each), and format into the acceptable solution format.
"""

def test_simple_rush_hour_graphplan():

    # BEGIN_YOUR_CODE
    pp = simple_rush_hour_task()
    gp_out = GraphPlan(pp).execute()          # -> [solution] or None
    partial = gp_out[0] if gp_out else []     # list[list[Expr]]
    total = Linearize(pp).execute() or []     # list[Expr]
    return partial, total

    # END_YOUR_CODE
   

def test_complex_rush_hour_graphplan():

    # BEGIN_YOUR_CODE

    pp = complex_rush_hour_task()
    gp_out = GraphPlan(pp).execute()
    partial = gp_out[0] if gp_out else []
    total = Linearize(pp).execute() or []
    return partial, total

    # END_YOUR_CODE



"""
PART D -- Below, we provide 4 (initial/domain, goal) state and (actions) combos. 
Complete the function to identify which (initial, goal) state matches
which action list.

Assume A,B,C,D,E are cars

The part_d() function is expected to return a list of tuples. 
Each tuple should be of form (solution_name, initial/domain_name),
where each part of the tuple is a string. This is not necessarily a 
one to one mapping. If multiple domains are solved by an action set,
return any of the solved domains. Note - `a3` represents the case 
where the environment is not solveable by any other action set.

E.g.
```
>>> part_d()
[('a1', 'i1'), ('a2', 'i1'), ('a3', 'i1'), ('a4', 'i1')]
"""

i1 = (
    'At(R, C3_1) & At(A, C3_2) & At(B, C3_3) & '
    'At(C, C2_3) & At(D, C4_3) & At(E, C2_2) & '
    'Clear(C1_1) & Clear(C1_2) & Clear(C1_3) & '
    'Clear(C1_4) & Clear(C2_1) & Clear(C2_4) & '
    'Clear(C3_4) & Clear(C4_1) & Clear(C4_2) & '
    'Clear(C4_4) & Horizontal(R) & Vertical(A) & '
    'Horizontal(B) & Horizontal(C) & Horizontal(D) & '
    'Horizontal(E)'
    ,
    'At(R, C3_4)'
)

a1 = [
    'MoveDown(A, C3_2, C4_2)',
    'MoveRight(C, C2_3, C2_4)',
    'MoveRight(R, C3_1, C3_2)',
    'MoveUp(B, C3_3, C2_3)',
    'MoveRight(R, C3_2, C3_3)',
    'MoveRight(R, C3_3, C3_4)'
]

i2 = (
    'At(R, C3_1) & At(A, C3_2) & At(B, C3_3) & '
    'At(C, C2_3) & At(D, C4_3) & At(E, C2_2) & '
    'Clear(C1_1) & Clear(C1_2) & Clear(C1_3) & '
    'Clear(C1_4) & Clear(C2_1) & Clear(C2_4) & '
    'Clear(C3_4) & Clear(C4_1) & Clear(C4_2) & '
    'Clear(C4_4) & Horizontal(R) & Vertical(A) & '
    'Vertical(B) & Vertical(C) & Horizontal(D) & '
    'Horizontal(E)'
    ,
    'At(R, C3_4)'
)

a2 = [
    'MoveDown(A, C3_2, C4_2)',
    'MoveUp(C, C2_3, C1_3)',
    'MoveUp(B, C3_3, C2_3)',
    'MoveRight(R, C3_1, C3_2)',
    'MoveRight(R, C3_2, C3_3)',
    'MoveRight(R, C3_3, C3_4)'
]

i3 = (
    'At(R, C3_1) & At(A, C3_2) & At(B, C3_3) & '
    'At(C, C2_3) & At(D, C4_3) & At(E, C2_2) & '
    'Clear(C1_1) & Clear(C1_2) & Clear(C1_3) & '
    'Clear(C1_4) & Clear(C2_1) & Clear(C2_4) & '
    'Clear(C3_4) & Clear(C4_1) & Clear(C4_2) & '
    'Clear(C4_4) & Horizontal(R) & Vertical(A) & '
    'Vertical(B) & Horizontal(C) & Vertical(D) & '
    'Horizontal(E)'
    ,
    'At(R, C3_4)'
)

a3 = [
    "None"
]

i4 = (
    'At(R, C3_1) & At(A, C3_2) & At(B, C3_3) & '
    'At(C, C2_3) & At(D, C4_3) & At(E, C2_2) & '
    'Clear(C1_1) & Clear(C1_2) & Clear(C1_3) & '
    'Clear(C1_4) & Clear(C2_1) & Clear(C2_4) & '
    'Clear(C3_4) & Clear(C4_1) & Clear(C4_2) & '
    'Clear(C4_4) & Horizontal(R) & Vertical(A) & '
    'Horizontal(B) & Horizontal(C) & Horizontal(D) & '
    'Vertical(E)'
    ,
    'At(R, C3_4)'
)

a4 = [
    'MoveDown(A, C3_2, C4_2)',
    'MoveUp(C, C2_3, C1_3)',
    'MoveRight(R, C3_1, C3_2)',
    'MoveUp(B, C3_3, C2_3)',
    'MoveRight(R, C3_2, C3_3)',
    'MoveRight(R, C3_3, C3_4)'
]

def part_d():
    
    # BEGIN_YOUR_CODE
    
    # Modify the template below to solve the problem
   
    # a1 needs Vertical(B) and Horizontal(C) -> matches i3
    # a2 needs Vertical(B) and Vertical(C)  -> matches i2
    # a3 is the unsolvable/none case          -> use i4 (no a1/a2/a4 fits)
    # a4 also needs Vertical(B) and Vertical(C)-> matches i2 (order differs)
    return [('a1', 'i3'), ('a2', 'i2'), ('a3', 'i4'), ('a4', 'i2')]
    # END_YOUR_CODE


"""
PART E — EXTRA CREDIT
Generalized Rush Hour (4x4, with Trucks)
-------------------------------------------------

In this final part, you will implement a *generalized* Rush Hour domain 
for a 4x4 grid with trucks, which occupy two consecutive cells instead 
of just one.

The trucks may be:
 - Horizontal trucks: length 2 along a row
 - Vertical trucks:   length 2 along a column

You must define:
 -  A new function `rush_hour_with_trucks(config)` that creates 
    a `PlanningProblem` for this domain.

Once defined, the function should:
 - Create a `PlanningProblem` instance from a provided configuration.

Executing `GraphPlan` to compute a partial-order plan and
linearizing that plan on this planning problem should solve
in a reasonable amount of time on the autograder. 

Note:
    This part is HARD (a valid solution may not exist within compute 
    constraints imposed by the autograder). The GraphPlan algorithm (and its 
    linearization step) suffers greatly from the curse of dimensionality
    — as the grid and # vehicles/sizes grow, the search space 
    expands combinatorially. Even small configurations may 
    require nontrivial computation to solve. It will be graded as
    full points or none.

### Configuration Format

You will receive a configuration dictionary such as:

```
config = {
    'cars': {
        'R': {'pos': (3, 1), 'dir': 'Horizontal'},   # Red car, horizontal
        'A': {'pos': (1, 1), 'dir': 'Horizontal'},   # Car A, horizontal
        'B': {'pos': (4, 3), 'dir': 'Vertical'}      # Car B, vertical
    },
    'trucks': {
        'T1': {'pos': ((3, 2), (4, 2)), 'dir': 'Vertical'},  # Horizontal truck
        'T2': {'pos': ((2, 3), (3, 3)), 'dir': 'Vertical'}     # Vertical truck
    },
    'goal': {
        'R': (3, 4),                                 # Red car must reach exit
        'T1': ((1, 2), (2, 2))                       # Truck T2 must move up two cells
    }
}
```

Which represents an inital state of:

      C1  C2  C3  C4
   +------------------+
R1 |  A   *   .   .  |
R2 |  .   *   T2  .  |
R3 |  R   T1  T2  *  |      * represents goals for R, T1
R4 |  .   T1  B   .  |
   +------------------+


Note - positions are 1-indexed in the configuration
Note - the direction of trucks is included, but they will always
  only move in the direction of their longest axis.
Note - You can assume there will always be 3 cars - A,B,R, and two
  trucks - T1, T2.

Feel free to add, modify, or remove your own predicates, actions, etc.
"""

def rush_hour_with_trucks(config):
    """
    Returns a PlanningProblem object, emulating rush_hour_4x4()
    """
    
    # BEGIN_WORK_HERE
    
    
    # ----- helpers -----
    def C(r, c): return f"C{r}_{c}"

    # ----- grid/domain base -----
    cells = [C(r, c) for r in range(1, 5) for c in range(1, 5)]
    cell_defs = " & ".join(f"Cell({x})" for x in cells)

    # Adjacency (Right/Left/Down/Up) — propositional over named cells
    adj = []
    for r in range(1, 5):
        for c in range(1, 4):
            adj.append(f"AdjacentRight({C(r,c)}, {C(r,c+1)})")
            adj.append(f"AdjacentLeft({C(r,c+1)}, {C(r,c)})")
    for c in range(1, 5):
        for r in range(1, 4):
            adj.append(f"AdjacentDown({C(r,c)}, {C(r+1,c)})")
            adj.append(f"AdjacentUp({C(r+1,c)}, {C(r,c)})")
    adj_defs = " & ".join(adj)

    # ----- initial state: types + positions + clears -----
    occ_cells = set()

    car_facts = []
    for name, data in config.get('cars', {}).items():
        r, c = data['pos']
        ori = data['dir']
        car_facts.append(f"Car({name})")
        car_facts.append(f"At({name}, {C(r,c)})")
        if ori.lower().startswith('h'):
            car_facts.append(f"Horizontal({name})")
        else:
            car_facts.append(f"Vertical({name})")
        occ_cells.add(C(r,c))

    truck_facts = []
    for name, data in config.get('trucks', {}).items():
        (r1, c1), (r2, c2) = data['pos']
        ori = data['dir']
        truck_facts.append(f"Truck({name})")
        truck_facts.append(f"Occupy({name}, {C(r1,c1)})")
        truck_facts.append(f"Occupy({name}, {C(r2,c2)})")
        if ori.lower().startswith('h'):
            truck_facts.append(f"HorizontalTruck({name})")
        else:
            truck_facts.append(f"VerticalTruck({name})")
        occ_cells.add(C(r1, c1))
        occ_cells.add(C(r2, c2))

    clear_cells = [x for x in cells if x not in occ_cells]
    clear_facts = " & ".join(f"Clear({x})" for x in clear_cells)

    initial = " & ".join(
        [*car_facts, *truck_facts, clear_facts] if clear_facts else [*car_facts, *truck_facts]
    )

    # ----- goals -----
    goal_facts = []
    for name, g in config.get('goal', {}).items():
        # car goal: (r,c)
        # truck goal: ((r1,c1),(r2,c2)) – we require both Occupy facts
        if isinstance(g[0], int):  # (r,c)
            goal_facts.append(f"At({name}, {C(g[0], g[1])})")
        else:                      # ((r1,c1),(r2,c2))
            (r1, c1), (r2, c2) = g
            goal_facts.append(f"Occupy({name}, {C(r1,c1)})")
            goal_facts.append(f"Occupy({name}, {C(r2,c2)})")
    goals = " & ".join(goal_facts) if goal_facts else ""

    # ----- typed domain annotations (static) -----
    type_defs = []
    if car_facts:
        type_defs.append(" & ".join({f.split('(')[0] for f in car_facts}))  # no-op, keep explicit types below
    domain_types = []
    if car_facts:
        domain_types.append(" & ".join({f"Car({k})" for k in config['cars'].keys()}))
        domain_types.append(" & ".join({
            (f"Horizontal({k})" if v['dir'].lower().startswith('h') else f"Vertical({k})")
            for k, v in config['cars'].items()
        }))
    if truck_facts:
        domain_types.append(" & ".join({f"Truck({k})" for k in config['trucks'].keys()}))
        domain_types.append(" & ".join({
            (f"HorizontalTruck({k})" if v['dir'].lower().startswith('h') else f"VerticalTruck({k})")
            for k, v in config['trucks'].items()
        }))

    typed_domain = " & ".join([x for x in domain_types if x])

    # ----- actions -----
    actions = [
        # Cars (length 1), constrained by orientation
        Action('MoveRightCar(c, frm, to)',
               precond='At(c, frm) & Clear(to) & Car(c) & Horizontal(c) & AdjacentRight(frm, to)',
               effect='At(c, to) & Clear(frm) & ~At(c, frm) & ~Clear(to)',
               domain='Car(c) & Cell(frm) & Cell(to) & AdjacentRight(frm, to)'),
        Action('MoveLeftCar(c, frm, to)',
               precond='At(c, frm) & Clear(to) & Car(c) & Horizontal(c) & AdjacentLeft(frm, to)',
               effect='At(c, to) & Clear(frm) & ~At(c, frm) & ~Clear(to)',
               domain='Car(c) & Cell(frm) & Cell(to) & AdjacentLeft(frm, to)'),
        Action('MoveUpCar(c, frm, to)',
               precond='At(c, frm) & Clear(to) & Car(c) & Vertical(c) & AdjacentUp(frm, to)',
               effect='At(c, to) & Clear(frm) & ~At(c, frm) & ~Clear(to)',
               domain='Car(c) & Cell(frm) & Cell(to) & AdjacentUp(frm, to)'),
        Action('MoveDownCar(c, frm, to)',
               precond='At(c, frm) & Clear(to) & Car(c) & Vertical(c) & AdjacentDown(frm, to)',
               effect='At(c, to) & Clear(frm) & ~At(c, frm) & ~Clear(to)',
               domain='Car(c) & Cell(frm) & Cell(to) & AdjacentDown(frm, to)'),

        # Trucks (length 2), represented by two Occupy(t, cell) facts.
        # Horizontal right: tail -- head -- to
        Action('MoveRightTruck(t, tail, head, to)',
               precond=('Truck(t) & HorizontalTruck(t) & Occupy(t, tail) & Occupy(t, head) & '
                        'AdjacentRight(tail, head) & AdjacentRight(head, to) & Clear(to)'),
               effect='Occupy(t, to) & Clear(tail) & ~Occupy(t, tail) & ~Clear(to)',
               domain='Truck(t) & Cell(tail) & Cell(head) & Cell(to)'),
        # Horizontal left: to -- head -- tail
        Action('MoveLeftTruck(t, head, tail, to)',
               precond=('Truck(t) & HorizontalTruck(t) & Occupy(t, head) & Occupy(t, tail) & '
                        'AdjacentLeft(head, tail) & AdjacentLeft(tail, to) & Clear(to)'),
               effect='Occupy(t, to) & Clear(head) & ~Occupy(t, head) & ~Clear(to)',
               domain='Truck(t) & Cell(head) & Cell(tail) & Cell(to)'),
        # Vertical up: to above head; free tail (the lower cell)
        Action('MoveUpTruck(t, head, tail, to)',
               precond=('Truck(t) & VerticalTruck(t) & Occupy(t, head) & Occupy(t, tail) & '
                        'AdjacentDown(head, tail) & AdjacentUp(head, to) & Clear(to)'),
               effect='Occupy(t, to) & Clear(tail) & ~Occupy(t, tail) & ~Clear(to)',
               domain='Truck(t) & Cell(head) & Cell(tail) & Cell(to)'),
        # Vertical down: to below tail; free head (the upper cell)
        Action('MoveDownTruck(t, head, tail, to)',
               precond=('Truck(t) & VerticalTruck(t) & Occupy(t, head) & Occupy(t, tail) & '
                        'AdjacentDown(head, tail) & AdjacentDown(tail, to) & Clear(to)'),
               effect='Occupy(t, to) & Clear(head) & ~Occupy(t, head) & ~Clear(to)',
               domain='Truck(t) & Cell(head) & Cell(tail) & Cell(to)'),
    ]

    domain = " & ".join(filter(None, [
        typed_domain,
        cell_defs,
        adj_defs
    ]))

    return PlanningProblem(
        initial=expr(initial) if initial else [],
        goals=expr(goals) if goals else [],
        actions=actions,
        domain=expr(domain)
    )

    # #END_WORK_HERE
