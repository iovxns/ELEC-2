import math
import numpy as np
import matplotlib.pyplot as plt
from bisection import bisection


def solve_problem_1():
    print("=== Problem 1 (Tolerance: 1e-6) ===")
    
    p1a = bisection(lambda x: x**3 - 9, 2.0, 3.0, tol=1e-6)
    p1b = bisection(lambda x: 3 * x**3 + x**2 - x - 5, 1.0, 2.0, tol=1e-6)
    p1c = bisection(lambda x: math.cos(x)**2 + 6 - x, 6.0, 7.0, tol=1e-6)

    print(f"1(a) Root: {p1a:.6f}")
    print(f"1(b) Root: {p1b:.6f}")
    print(f"1(c) Root: {p1c:.6f}\n")


def solve_problem_2():
    print("=== Problem 2 (Tolerance: 1e-8) ===")
    
    p2a = bisection(lambda x: x**5 + x - 1, 0.0, 1.0, tol=1e-8)
    p2b = bisection(lambda x: math.sin(x) - 6 * x - 5, -1.0, 0.0, tol=1e-8)
    p2c = bisection(lambda x: math.log(x) + x**2 - 3, 1.0, 2.0, tol=1e-8)

    print(f"2(a) Root: {p2a:.8f}")
    print(f"2(b) Root: {p2b:.8f}")
    print(f"2(c) Root: {p2c:.8f}\n")


def solve_problem_3():
    print("=== Problem 3 (Tolerance: 1e-6) ===")
    
    # 3(a): 2x^3 - 6x - 1 = 0
    f3a = lambda x: 2 * x**3 - 6 * x - 1
    r3a_1 = bisection(f3a, -2.0, -1.0, tol=1e-6)
    r3a_2 = bisection(f3a, -1.0, 0.0, tol=1e-6)
    r3a_3 = bisection(f3a, 1.0, 2.0, tol=1e-6)
    print(f"3(a) Roots: [{r3a_1:.6f}, {r3a_2:.6f}, {r3a_3:.6f}]")

    # 3(b): e^(x-2) + x^3 - x = 0
    f3b = lambda x: math.exp(x - 2) + x**3 - x
    r3b_1 = bisection(f3b, -2.0, -1.0, tol=1e-6)
    r3b_2 = bisection(f3b, -1.0, 0.0, tol=1e-6)
    r3b_3 = bisection(f3b, 0.0, 1.0, tol=1e-6)
    print(f"3(b) Roots: [{r3b_1:.6f}, {r3b_2:.6f}, {r3b_3:.6f}]")

    # 3(c): 1 + 5x - 6x^3 - e^(2x) = 0
    f3c = lambda x: 1 + 5 * x - 6 * x**3 - math.exp(2 * x)
    r3c_1 = bisection(f3c, -1.0, 0.0, tol=1e-6)
    r3c_2 = bisection(f3c, 0.0, 1.0, tol=1e-6)
    r3c_3 = bisection(f3c, 1.0, 2.0, tol=1e-6)
    print(f"3(c) Roots: [{r3c_1:.6f}, {r3c_2:.6f}, {r3c_3:.6f}]\n")

    # Save visualization to file
    generate_plots()


def generate_plots():
    x = np.linspace(-2.5, 2.5, 500)
    fig, axes = plt.subplots(3, 1, figsize=(8, 10))

    # Plot 3a
    axes[0].plot(x, 2 * x**3 - 6 * x - 1, color='blue', label=r'$2x^3 - 6x - 1$')
    axes[0].axhline(0, color='gray', linestyle='--')
    axes[0].set_title('Problem 3(a)')
    axes[0].grid(True)
    axes[0].legend()

    # Plot 3b
    axes[1].plot(x, np.exp(x - 2) + x**3 - x, color='green', label=r'$e^{x-2} + x^3 - x$')
    axes[1].axhline(0, color='gray', linestyle='--')
    axes[1].set_title('Problem 3(b)')
    axes[1].grid(True)
    axes[1].legend()

    # Plot 3c
    axes[2].plot(x, 1 + 5 * x - 6 * x**3 - np.exp(2 * x), color='red', label=r'$1 + 5x - 6x^3 - e^{2x}$')
    axes[2].axhline(0, color='gray', linestyle='--')
    axes[2].set_title('Problem 3(c)')
    axes[2].grid(True)
    axes[2].legend()

    plt.tight_layout()
    plt.savefig('problem_3_plots.png')
    print("Plot saved as 'problem_3_plots.png'")


if __name__ == "__main__":
    solve_problem_1()
    solve_problem_2()
    solve_problem_3()