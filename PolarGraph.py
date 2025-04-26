#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
polar_grapher.py

Interactive polar-function grapher.
Enter expressions in terms of 'theta', e.g.:
    3*sin(2*theta)
    1 + 2*cos(5*theta)
    theta**2

Type 'quit' at any prompt to exit.
"""

import sys
from fractions import Fraction
import numpy as np
import matplotlib.pyplot as plt

# Namespace of allowed functions/constants for eval()
SAFE_NS = {
    'sin': np.sin, 'cos': np.cos, 'tan': np.tan,
    'exp': np.exp, 'log': np.log, 'sqrt': np.sqrt,
    'pi': np.pi, 'e': np.e, 'abs': np.abs,
}

def prompt_function():
    expr = input("Enter r(θ) = ").strip()
    if expr.lower() == 'quit':
        sys.exit(0)
    return expr

def prompt_range():
    rng = input("θ range (start,end in radians) [default 0,2π]: ").strip()
    if rng.lower() == 'quit':
        sys.exit(0)
    if not rng:
        return 0.0, 2*np.pi
    try:
        start_s, end_s = rng.split(',')
        # evaluate expressions (allows use of pi, e, etc.)
        start = eval(start_s, {'__builtins__': {}}, SAFE_NS)
        end   = eval(end_s,   {'__builtins__': {}}, SAFE_NS)
        return float(start), float(end)
    except Exception:
        print("Invalid format. Using default 0,2π.")
        return 0.0, 2*np.pi

def prompt_points():
    pts = input("Number of sample points [default 1000]: ").strip()
    if pts.lower() == 'quit':
        sys.exit(0)
    if not pts:
        return 1000
    try:
        n = int(pts)
        return max(n, 1000)
    except:
        print("Invalid number. Using default 1000.")
        return 1000

def prompt_save():
    fn = input("Save as filename (e.g. 'rose.png') [leave blank to skip]: ").strip()
    if fn.lower() == 'quit':
        sys.exit(0)
    return fn or None

def plot_polar(expr, theta, r, savefile=None):
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw={'projection': 'polar'})
    theta_plot = np.where(r >= 0, theta, theta + np.pi)
    r_plot     = np.abs(r)
    ax.plot(theta_plot, r_plot, linewidth=2)
    # ax.set_title(f"r(θ) = {expr}", va='bottom')
    # --- Light gray grid for angular and radial lines ---
    ax.xaxis.grid(True, color='lightgray', linestyle='--', linewidth=0.5)
    ax.yaxis.grid(True, color='lightgray', linestyle='--', linewidth=0.5)

    # --- Dynamic pi/12 theta labels ---
    angles_deg = np.arange(0, 360, 15)
    angles_rad = np.deg2rad(angles_deg)
    ax.set_xticks(angles_rad)
    labels = []
    for deg in angles_deg:
        frac = Fraction(deg, 180).limit_denominator()
        if frac.numerator == 0:
            labels.append(r"$0$")
        elif frac.numerator == frac.denominator:
            labels.append(r"$2\pi$")
        else:
            labels.append(rf"$\frac{{{frac.numerator}\pi}}{{{frac.denominator}}}$")
    ax.set_xticklabels(labels)

    # --- Radial ticks: start at 0, increment by 1, and position labels along θ=0 axis ---
    r_max = np.max(np.abs(r))
    r_max = np.ceil(r_max)
    rticks = np.arange(0, r_max + 1, 1)
    ax.set_theta_zero_location("E")
    ax.set_theta_direction(1)
    ax.set_rlabel_position(0)
    # --- Lighten radial tick label color ---
    ax.tick_params(axis='y', labelcolor='lightgray')

    if savefile:
        fig.savefig(savefile, dpi=300, bbox_inches='tight')
        print(f"Saved plot to '{savefile}'")
    else:
        plt.show()
    plt.close(fig)

def main():
    print("=== Polar Function Grapher ===")
    print("Type 'quit' at any prompt to exit.\n")
    while True:
        expr = prompt_function()
        th0, th1 = prompt_range()
        n_pts    = prompt_points()
        savefile = prompt_save()

        # Auto-generate filename if none given
        if savefile is None:
            safe_expr = expr.replace('*', '').replace('**', '').replace('/', '').replace('(', '').replace(')', '').replace('+', '').replace('-', '').replace(' ', '')
            savefile = f"graph_{safe_expr}.png"

        # generate θ values
        theta = np.linspace(th0, th1, n_pts)
        
        # ensure we hit the pole: include the exact zeros of sin(2θ)
        zero_thetas = np.arange(th0, th1 + 1e-8, np.pi/2)
        theta = np.unique(np.concatenate([theta, zero_thetas]))
        theta.sort()

        # evaluate r(θ)
        # build namespace so eval can see theta + the numpy functions
        ns = SAFE_NS.copy()
        ns['theta'] = theta
        try:
            r = eval(expr, {'__builtins__': {}}, ns)
        except Exception as e:
            print(f"Error evaluating expression: {e}\nTry again.\n")
            continue

        # plot
        plot_polar(expr, theta, r, savefile)
        print("")  # blank line before next loop

if __name__ == '__main__':
    main()