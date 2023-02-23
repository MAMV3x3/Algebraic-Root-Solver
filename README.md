# Algebraic-Root-Solver

This program allows you to solve algebraic equations using various numerical methods, including:
1. Bisection method
2. Newton-Raphson method
3. 2nd order Newton-Raphson method
4. Von Mises method
## Getting Started
### Prerequisites
- Python 3
- SymPy
- Matplotlib
### Installing

Clone the repository:
```bash
git clone https://github.com/MAMV3x3/Algebraic-Root-Solver.git
```
Install SymPy:
```bash
pip install sympy
```

Install Matplotlib:
```bash
pip install matplotlib
```

## Usage

To use the program, run the RootSolver.py file in a Python environment. You will be prompted to input the function you want to solve, the method you want to use, the tolerance, and the maximum number of iterations.

If you want to use the bisection method, you will also be prompted to input the interval.

If you want to use any other method, you will be prompted to input the initial guess.

The program will output a table of iterations, x values, and f(x) values, as well as the result of the equation. It will also graph the function and the root.

## Supported Operations

The program supports the following operations:

- Addition (+)
- Subtraction (-)
- Multiplication (*)
- Division (/)
- Power (^)
- Parentheses ( )
- Trigonometric functions: sin, cos, tan, cot, sec, csc

## Examples

### Input
```yaml
Enter the function f(x): x^2 - 2
Enter the method (bisection, newtonRaphson, newtonRaphson2, vonMises): newtonRaphson
Enter the tolerance: 0.001
Enter the maximum number of iterations: 100
Enter the initial guess: 2
```

### Output
```yaml
i      x              f(x)
0      1.50000        0.25000
1      1.41667        0.00694
2      1.41422        0.00001
The root is:  1.4142156862745099
```
![Figure_1](https://user-images.githubusercontent.com/84588180/221038840-1605650c-9c0b-40c2-b58a-531112cf2c0d.png)

### Authors
- [Miguel Ángel Mireles Vázquez](https://github.com/MAMV3x3)

## License

This project is licensed under the MIT License - see the LICENSE file for details.
