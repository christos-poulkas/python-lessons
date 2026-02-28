#easy level (4 exercises)

import numpy as np
import matplotlib.pyplot as plt

def task1():
    print("Create a 1D NumPy array with the values [4, 7, 2, 9]. Print the first element, the last element, and the shape of the array.")
    n = np.array([4, 7, 2, 9])
    print(n[0])

def task2():
    print("Create a 3x3 matrix filled with zeros. Then change the center element to 5 and print the matrix")
    n = np.zeros([3,3])
    n[1,1] = 5
    print(n)

def task3():
    print("Use np.arange() to create an array from 10 to 30 with step 5. Sort it in descending order.")
    n = np.arange(10, 30, 5)
    print(n[::-1])

def task4():
    print("Create two arrays: a = [1,2,3] and b = [4,5,6]. Concatenate them and print the result.")
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    n = np.concatenate((a,b))
    print(n)

#Medium Level (4 Exercises)

def task5():
    print("Create a 4x4 matrix with random values between 0 and 1. Print only the first two rows and last two columns.")
    n = np.random.default_rng().random((4,4))
    print(n)
    print("/////////////////////")
    print(n[:2,2:])

def task6():
    print("Generate a 1D array of 20 equally spaced numbers between -5 and 5 using np.linspace(). Reshape it into a 4x5 matrix")
    n = np.linspace(-5, 5, 20)
    print(n)
    n = n.reshape(4,5)
    print(n)

def task7():
    print("7) Create a 3x3 random matrix. Compute and print its transpose. Then reshape it into a 1x9 row vector")
    n = np.random.default_rng().random((3,3))
    print(n)
    n = n.reshape(1,9)
    print(n)

def task8():
    print("8) Create x values from -2 to 2 (100 points). Plot y = x^3 - 2x + 1 using matplotlib.")
    x = np.linspace(-2, 2, 100)
    y = x**3 - 2*x + 1
    plt.plot(x, y)
    plt.xlabel("x axis")
    plt.ylabel("y axis")
    plt.title("function y= x^3 - 2x +1")
    plt.grid(True)
    plt.show()


#Hard Level (4 Exercises)

def task9():
    print("9) Create two random 3x3 matrices A and B. Perform matrix multiplication (not element-wise) and print the result.")
    A = np.random.default_rng().random((3,3))
    print(A)
    B = np.random.default_rng().random((3,3))
    print(B)
    C = A@B
    print(C)

def task10():
    print("10) Generate a 100x100 grid using meshgrid for x and y in range [-3,3]. Plot the 3D surface Z = sin(X^2 + Y^2).")
    x_values = np.linspace(-3, 3, 100)
    y_values = np.linspace(-3, 3, 100)
    X, Y = np.meshgrid(x_values, y_values)
    Z = np.sin(X ** 2 + Y ** 2)

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    ax.plot_surface(X,Y,Z)

    plt.show()

def task11():
    print("11) Create a 5x5 matrix with random integers from 1 to 50. Sort each row independently in ascending order.")
    rng = np.random.default_rng()
    n = rng.integers(0, 51, (5,5))
    print(n)
    n = n.reshape(1, 25)
    n = np.sort(n)
    print(n)

def task12():
    print("12) Create a saddle surface Z = X^2 - Y^2. Then modify it to Z = X^2 - Y^2 + sin(XY). Plot both surfaces in separate figures.")
    x = np.linspace(-3,3,100)
    y = np.linspace(-3, 3, 100)
    X, Y = np.meshgrid(x, y)

    Z1 = X**2 - Y**2

    Z2 = X**2 - Y**2 + np.sin(X * Y)

    fig1 = plt.figure()
    ax1 = fig1.add_subplot(projection="3d")
    ax1.plot_surface(X, Y, Z1)

    fig2 = plt.figure()
    ax2 = fig2.add_subplot(projection="3d")
    ax2.plot_surface(X, Y, Z2)

    plt.show()

def task13():
    x = np.linspace(-3, 3, 100)
    y = np.linspace(-3, 3, 100)
    X, Y = np.meshgrid(x, y)

    Z = np.exp((-(X**2 + Y**2)))

    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")
    ax.plot_surface(X, Y, Z)

    plt.show()

def task14():
    x = np.linspace(1,2,15)
    y = np.linspace(1, 2, 15)
    X, Y = np.meshgrid(x, y)

    Z = X**3 / Y**0.5

    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")
    ax.plot_surface(X, Y, Z)
    plt.show()

task14()