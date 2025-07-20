# Function to calculate the mean of a list of numbers
def mean(numbers):
    return sum(numbers) / len(numbers)

# Function to calculate the correlation coefficient
def correlation_coefficient(x, y):
    n = len(x)

    # Calculate means
    mean_x = mean(x)
    mean_y = mean(y)

    # Calculate the covariance
    covariance = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))

    # Calculate standard deviations
    std_dev_x = (sum((xi - mean_x) ** 2 for xi in x) / (n - 1)) ** 0.5
    std_dev_y = (sum((yi - mean_y) ** 2 for yi in y) / (n - 1)) ** 0.5

    # Calculate correlation coefficient
    correlation = covariance / ((std_dev_x * std_dev_y)* (n - 1))

    return correlation

# Input decimal numbers
x = [float(num) for num in input("Enter the values of x separated by spaces: ").split()]
y = [float(num) for num in input("Enter the values of y separated by spaces: ").split()]

# Check if the lengths of the two lists are equal
if len(x) != len(y):
    print("Error: Lengths of x and y must be equal")
else:
    # Calculate and print the correlation coefficient
    correlation = correlation_coefficient(x, y)
    print("Correlation coefficient:", correlation)
