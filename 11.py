import copy
import sudoku_constraints11 as sudo
#from flask import Flask, render_template, request
#import tkinter as tk


grid = [[0, 0, 0, 0, 9, 0, 0, 7, 5],
        [0, 0, 1, 2, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 0, 0, 1, 8, 0],
        [3, 0, 0, 6, 0, 0, 9, 0, 0],
        [1, 0, 0, 0, 5, 0, 0, 0, 4],
        [0, 0, 6, 0, 0, 2, 0, 0, 3],
        [0, 3, 2, 0, 0, 0, 0, 4, 0],
        [0, 0, 0, 0, 0, 6, 5, 0, 0],
        [7, 9, 0, 0, 1, 0, 0, 0, 0]]

# Define the puzzle to be solved
puzzle_9 = {
    "variables": {},
    "domain": [1, 2, 3, 4, 5, 6, 7, 8, 9],
    "constraints": sudo.constraints,
    #"neighbors": {}
}

# Define the variables and initial values for the puzzle
for i in range(1,10):
    for j in range(1,10):
        cell_name = "C" + str(i) + str(j)
        if grid[i - 1][j - 1] == 0:
            puzzle_9["variables"][cell_name] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        else:
            puzzle_9["variables"][cell_name] = [grid[i - 1][j - 1]]
        #print(puzzle_9["variables"][cell_name])


#............
def revise(csp, var1, var2):
    revised = False
    domain1 = csp["variables"][var1]
    domain2 = csp["variables"][var2]

    for x in domain1:
        is_compatible = any([[(x, y) in csp["constraints"] or (y, x) in csp["constraints"]] for y in domain2])
        if not is_compatible:
            domain1.remove(x)
            revised = True
    return revised


#.....
def ac3(csp):
    queue = [(xi, xj) for xi in csp["variables"] for xj in csp["variables"] if xi != xj]
    while queue:
        xi, xj = queue.pop(0)
        if revise(csp, xi, xj):
            if len(csp["variables"][xi]) == 0:
                return False
            for var in csp["variables"]:
                if var != xi and var != xj:
                    queue.append((var, xi))
    return True

#.....
def minimum_remaining_values(csp, assignments):
    unassigned_vars = []
    for var in csp['variables']:
        if var not in assignments:
            unassigned_vars.append(var)
    min_var = unassigned_vars[0]
    min_domain_size = len(csp['variables'][min_var])
    for var in unassigned_vars:
        domain_size = len(csp['variables'][var])
        if domain_size < min_domain_size:
            min_var = var
            min_domain_size = domain_size
    return min_var



def backtrack(csp, assignments):
    # Check if all variables have been assigned
    if len(assignments) == len(csp['variables']):
        return assignments

    # Select an unassigned variable with the smallest domain size
    unassigned_vars = [var for var in csp['variables'] if var not in assignments]
    var = min(unassigned_vars, key=lambda var: len(csp['variables'][var]))

    # Try each value in the domain of the selected variable
    for val in csp['variables'][var]:
        # Create a new set of assignments with the new assignment
        new_assignments = copy.deepcopy(assignments)
        new_assignments[var] = val

        # Create a new CSP with the new assignments
        new_csp = copy.deepcopy(csp)

        # Enforce arc consistency using AC3
        if ac3(new_csp):
            # Recursively call the function with the new CSP and assignments
            result = backtrack(new_csp, new_assignments)

            # If a solution is found, return it
            if result:
                return result

    # If no solution was found, backtrack
    return False



def solve(csp):
    # Make a copy of the variables dictionary to use as the initial solution
    solution = copy.deepcopy(csp['variables'])

    # Use backtracking to find a solution
    result = backtrack({}, solution, csp)

    if not result:
        return None
    else:
        return result

solve = backtrack(puzzle_9,{})
print(solve)
print()