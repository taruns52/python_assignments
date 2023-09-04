"""
13. Create a class name Number with the following methods.

*-> Output:

Numbers: [2, 5, 1, 66, 22, 11, 10] 
New values: [4, 10, 2, 132, 44, 22, 20] 
Filtered values: [2, 66, 22, 10] 
Compounded value: 117
Sorted list: [1, 2, 5, 10, 11, 22, 66]

"""

from functools import reduce


class Number:
    def __init__(self, numbers):
        self.numbers = numbers

    def get(self):
        return self.numbers

    def change_original_values(self, func: lambda x: x):
        new_numbers = list(map(func, self.numbers))
        return new_numbers

    def filter_values(self, filter_func: lambda x: x):
        filtered_numbers = list(filter(filter_func, self.numbers))
        return filtered_numbers

    def compound_the_numbers(self, reduce_func: lambda compound, d: compound + d):
        compounded_value = reduce(reduce_func, self.numbers)
        return compounded_value

    def sort(self):
        #  Sorting the list using bubble sort and return sorted list
        for i in range(len(self.numbers) - 1):
            for j in range(len(self.numbers) - 1):
                if self.numbers[j + 1] < self.numbers[j]:
                    self.numbers[j + 1], self.numbers[j] = (
                        self.numbers[j],
                        self.numbers[j + 1],
                    )
        return self.numbers


if __name__ == "__main__":
    numbers = [2, 5, 1, 66, 22, 11, 10]

    # Create an object of Number class and initialize it.
    n1 = Number(numbers)

    # Print the list
    print("\nNumbers: ", n1.get())

    # lambda_func1 = Create lambda function that doubles the value of list
    print("New values:", n1.change_original_values(func=lambda x: 2 * x))

    # lambda func2 = Create lambda function that filter out odd numbers
    print("Filtered values:", n1.filter_values(filter_func=lambda x: (x % 2 == 0)))

    # lambda_func3 = Create lambda function to pass as reduce_function
    print(
        "Compounded value:",
        n1.compound_the_numbers(reduce_func=lambda sum, x: (sum + x)),
    )

    # Sort the list
    print("Sorted list:", n1.sort(), "\n")
