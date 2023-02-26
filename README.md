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
Enter the function f(x): x^3-2x^2-5
Enter the method (bisection, newtonRaphson, newtonRaphson2, vonMises): bisection
Enter the tolerance: 1e-5
Enter the maximum number of iterations: 100
Enter the left endpoint: 1
Enter the right endpoint: 4
```

### Output
```yaml
i      x              f(x)
0      2.50000        -1.87500
1      3.25000        8.20312
2      2.87500        2.23242
3      2.68750        -0.03442
4      2.78125        1.04324
5      2.73438        0.49078
6      2.71094        0.22481
7      2.69922        0.09436
8      2.69336        0.02976
9      2.69043        -0.00239
10     2.69189        0.01367
11     2.69116        0.00564
12     2.69080        0.00163
13     2.69061        -0.00038
14     2.69070        0.00062
15     2.69066        0.00012
16     2.69064        -0.00013
17     2.69065        -0.00000
18     2.69065        0.00006
The root is:  2.690652847290039
```
![Figure_1](https://user-images.githubusercontent.com/84588180/221438967-7d5b9727-3565-4ee9-af55-78b736f080e9.png)


### Authors
- [Miguel Ángel Mireles Vázquez](https://github.com/MAMV3x3)

## License

This project is licensed under the MIT License - see the LICENSE file for details.
