"""
You are given a list of numbers and your task is to sort the list without any inbuilt method of python.
Input: numbers = [2, 5, 6, 1, 3, 8, 9, 10]
Output: [1, 2, 3, 5, 6, 8, 9, 10]
"""

def heapify(arr, N, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < N and arr[largest] < arr[l]:
        largest = l

    if r < N and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        heapify(arr, N, largest)


def heapSort(arr):
    N = len(arr)

    for i in range(N // 2 - 1, -1, -1):
        heapify(arr, N, i)

    for i in range(N - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)


if __name__ == "__main__":
    numbers = [2, 5, 6, 1, 3, 8, 9, 10]

    heapSort(numbers)
    N = len(numbers)

    print("\nSorted array is: ", end=' ')
    print(*numbers)
