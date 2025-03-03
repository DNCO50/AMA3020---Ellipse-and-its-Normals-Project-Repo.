#Solving for a given point
import numpy as np
from scipy.optimize import fsolve

def combined_equation(vars, a, b, x0, y0):
    x, y = vars
    eq1 = x * y * (a**2 - b**2) - a**2 * x0 * y + b**2 * y0 * x
    eq2 = x**2 / a**2 + y**2 / b**2 - 1
    return [eq1, eq2]  #the two equations to find the intersections of

def solve_combined(a, b, x0, y0, initial_guesses):
    solutions = []
    for guess in initial_guesses:
        sol = fsolve(combined_equation, guess, args=(a, b, x0, y0))
        sol = tuple(np.round(sol, 6))  #Rounds to avoid duplicates
        if sol not in solutions:
            solutions.append(sol)
    return solutions

#Parameters of ellipse used in paper
a = 7
b = 4
#Point I want to talk about
x0, y0 = 2, 2  
initial_guesses = [(1, 1), (-1, 1), (1, -1), (-1, -1), (2, 2), (-2, 2), (2, -2), (-2, -2)]  #initial guesses for fsolve to get the 4 intersection points - more than 4 are used because sometimes two guesses converge to the same root :/

solutions = solve_combined(a, b, x0, y0, initial_guesses)
print("Intersection points:", solutions)    