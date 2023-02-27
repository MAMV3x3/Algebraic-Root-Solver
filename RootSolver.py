# Solve algebraic equations using numerical methods
# 1. Bisection method
# 2. Newton-Raphson method
# 3. 2nd order Newton-Raphson method
# 4. Von Mises method
# Make it so that the user can input the function they want to solve
# Ask the user for the method they want to use
# Ask the user for the tolerance
# Ask the user for the maximum number of iterations
# If the user wants to use the bisection method, ask for the interval
# If the user wants to use any other method, ask for the initial guess
# Print a table of iterations, x values, and f(x) values
# Print the results of the equation
# Graph the function and the root

import sympy as sp
import matplotlib.pyplot as plt
import re

# Define the methods


def bisection(f, a, b, tol, maxIter, col_widths, x_points, y_points):
    # Check if the interval is valid
    if f(a) * f(b) > 0:
        print("The interval is not valid")
        return
    # Check if the interval is valid
    if f(a) * f(b) == 0:
        print("One of the endpoints is a root")
        return
    # Initialize the variables
    x = 0
    i = 0
    # Print the table header
    print("{:<{}} {:<{}} {:<{}}".format(
        "i", col_widths[0], "x", col_widths[1], "f(x)", col_widths[2]))
    # Loop until the tolerance is met
    while abs(b - a) > tol:
        # Calculate the midpoint
        x = (a + b) / 2
        # Check if the midpoint is a root
        if f(x) == 0:
            print("The root is: ", x)
            return
        # Check if the midpoint is in the left interval
        if f(a) * f(x) < 0:
            b = x
        # Check if the midpoint is in the right interval
        else:
            a = x
        # Print the table formatted with the specified width
        print("{:<{}} {:<{}} {:<{}}".format(i, col_widths[0], "{:.5f}".format(
            x), col_widths[1], "{:.5f}".format(f(x)), col_widths[2]))
        # Add a point for the graph iteration vs result use pointers to the list
        x_points.append(i)
        y_points.append(x)
        # Increment the counter
        i += 1
        # Check if the maximum number of iterations is reached
        if i == maxIter:
            print("The maximum number of iterations was reached")
            return
    # Print the results
    print("The root is: ", x)
    graph(x_points, y_points)


def newtonRaphson(f, df, x0, tol, maxIter, col_widths, x_points, y_points):
    # Initialize the variables
    x = 0
    i = 0
    # Print the table header
    print("{:<{}} {:<{}} {:<{}}".format(
        "i", col_widths[0], "x", col_widths[1], "f(x)", col_widths[2]))
    # Loop until the tolerance is met
    while abs(f(x0)) > tol:
        # Check if the derivative is zero
        if df(x0) == 0:
            print("The derivative is zero")
            return
        # Calculate the next x value
        x = x0 - f(x0) / df(x0)
        # Print the table formatted with the specified width
        print("{:<{}} {:<{}} {:<{}}".format(i, col_widths[0], "{:.5f}".format(
            x), col_widths[1], "{:.5f}".format(f(x)), col_widths[2]))
        # Check if the maximum number of iterations is reached
        if i == maxIter:
            print("The maximum number of iterations was reached")
            return
        # Add a point for the graph iteration vs result use pointers to the list
        x_points.append(i)
        y_points.append(x)
        # Increment the counter
        i += 1
        # Update the x value
        x0 = x
    # Print the results
    print("The root is: ", x)
    graph(x_points, y_points)

# Second order Newton-Raphson method


def newtonRaphson2(f, df, ddf, x0, tol, maxIter, col_widths, x_points, y_points):
    # Initialize the variables
    x = 0
    i = 0
    # Print the table header
    print("{:<{}} {:<{}} {:<{}}".format(
        "i", col_widths[0], "x", col_widths[1], "f(x)", col_widths[2]))
    # Loop until the tolerance is met
    while abs(f(x0)) > tol:
        # Check if the derivative is zero
        if df(x0) == 0:
            print("The derivative is zero")
            return
        # Calculate the next x value
        x = x0 - f(x0) * df(x0) / (df(x0) ** 2 - f(x0) * ddf(x0))
        # Print the table formatted with the specified width
        print("{:<{}} {:<{}} {:<{}}".format(i, col_widths[0], "{:.5f}".format(
            x), col_widths[1], "{:.5f}".format(f(x)), col_widths[2]))
        # Check if the maximum number of iterations is reached
        if i == maxIter:
            print("The maximum number of iterations was reached")
            return
        # Add a point for the graph iteration vs result use pointers to the list
        x_points.append(i)
        y_points.append(x)
        # Increment the counter
        i += 1
        # Update the x value
        x0 = x
    # Print the results
    print("The root is: ", x)
    graph(x_points, y_points)


def vonMises(f, df, x0, tol, maxIter, col_widths, x_points, y_points):
    # Initialize the variables
    x = x0
    i = 0
    # Print the table header
    print("{:<{}} {:<{}} {:<{}}".format(
        "i", col_widths[0], "x", col_widths[1], "f(x)", col_widths[2]))
    # Loop until the tolerance is met
    while abs(f(x)) > tol:
        # Check if the derivative is zero
        if df(x) == 0:
            print("The derivative is zero")
            return
        # Calculate the next x value
        x = x - f(x) / df(x0)
        # Print the table
        print("{:<{}} {:<{}} {:<{}}".format(i, col_widths[0], "{:.5f}".format(
            x), col_widths[1], "{:.5f}".format(f(x)), col_widths[2]))
        # Check if the maximum number of iterations is reached
        if i == maxIter:
            print("The maximum number of iterations was reached")
            return
        # Add a point for the graph iteration vs result use pointers to the list
        x_points.append(i)
        y_points.append(x)
        # Increment the counter
        i += 1
    # Print the results
    print("The root is: ", x)
    graph(x_points, y_points)

# Graph the function and the root obtained


def graph(x_points, y_points):
    # Create the figure
    fig = plt.figure()
    # Create the axes
    ax = fig.add_subplot(111)
    # Set the title
    ax.set_title("Root vs Iteration")
    # Set the x label
    ax.set_xlabel("Iteration")
    # Set the y label
    ax.set_ylabel("Root")
    # Show the reached root with a red dot and a label "root" in the legend and put it on the left
    ax.plot(x_points[-1], y_points[-1], "ro", label="root", markersize=10)
    # Mark the root value in the y axis and make it fit inside the graph and dont overflow
    ax.annotate("{:.5f}".format(y_points[-1]), xy=(x_points[-1], y_points[-1]), xytext=(0, 20), textcoords="offset points",
                ha="center", va="bottom", bbox=dict(boxstyle="round", fc="w"), arrowprops=dict(arrowstyle="->"))
    # Set the x axis ticks
    ax.set_xticks(x_points)
    # Set the x axis limits
    ax.set_xlim([0, len(x_points) + 1])
    # Set the y axis limits
    ax.set_ylim([min(y_points) - 1, max(y_points) + 1])
    # Connect the points with a line and plot the graph
    ax.plot(x_points, y_points)
    # Add dotted line in the y axis to mark the root
    ax.axhline(y=y_points[-1], color="black", linestyle="--")
    # Show the legend
    ax.legend()
    # Show the graph
    plt.show()


# Main function


def main():
    # Ask the user for the function
    f_expr = input("Enter the function f(x): ")

    # Replace "^" with "**"
    f_expr = f_expr.replace("^", "**")

    # Replace "number x" or "x number" with "number*x" or "x*number"
    f_expr = re.sub(r"(\d+)x", r"\1*x", f_expr)
    f_expr = re.sub(r"x(\d+)", r"x*\1", f_expr)

    # Parse the expression using sympify
    f_expr = sp.sympify(f_expr)
    # Calculate the derivative of the function
    df = sp.diff(f_expr)
    ddf = sp.diff(df)
    # Lambdifying the function
    x = sp.symbols('x')
    f = sp.lambdify(x, f_expr)
    df = sp.lambdify(x, df)
    ddf = sp.lambdify(x, ddf)
    # Define format for the table
    col_widths = [6, 14, 14]
    # Define arrays for the graph
    x_points = []
    y_points = []
    # Ask the user for the method (show the options)
    method = input(
        "Enter the method (bisection, newtonRaphson, newtonRaphson2, vonMises): ")
    # Ask the user for the tolerance
    tol = float(input("Enter the tolerance: "))
    # Ask the user for the maximum number of iterations
    maxIter = int(input("Enter the maximum number of iterations: "))
    # Check if the user wants to use the bisection method
    if method == "bisection":
        # Ask the user for the interval
        a = float(input("Enter the left endpoint: "))
        b = float(input("Enter the right endpoint: "))
        # Call the bisection method
        bisection(f, a, b, tol, maxIter, col_widths, x_points, y_points)
    # Check if the user wants to use any other method
    else:
        # Ask the user for the initial guess
        x0 = float(input("Enter the initial guess: "))
        # Check if the user wants to use the Newton-Raphson method
        if method == "newtonRaphson":
            # Call the Newton-Raphson method
            newtonRaphson(f, df, x0, tol, maxIter,
                          col_widths, x_points, y_points)
        # Check if the user wants to use the 2nd order Newton-Raphson method
        elif method == "newtonRaphson2":
            # Call the 2nd order Newton-Raphson method
            newtonRaphson2(f, df, ddf, x0, tol, maxIter,
                           col_widths, x_points, y_points)
        # Check if the user wants to use the Von Mises method
        elif method == "vonMises":
            # Call the Von Mises method
            vonMises(f, df, x0, tol, maxIter, col_widths, x_points, y_points)
        # Check if the user wants to use any other method
        else:
            print("Invalid method")


# Call the main function
if __name__ == "__main__":
    main()
