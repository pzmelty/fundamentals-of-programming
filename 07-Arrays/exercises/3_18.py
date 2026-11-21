# Returns the second largest element
def second_largest(arr):
    largest = arr[0]
    second = None

    for i in arr:
        if i > largest:
            second = largest
            largest = i
        elif second is None or (i > second and i != largest):
            second = i

    return second


# Returns the difference between largest and smallest
def difference(arr):
    largest = arr[0]
    smallest = arr[0]

    for i in arr:
        if i > largest:
            largest = i
        if i < smallest:
            smallest = i

    return largest - smallest


# Returns the median
def median(arr):
    numbers = arr.copy()

    for i in range(len(numbers)):
        for j in range(len(numbers) - 1 - i):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    middle = len(numbers) // 2

    if len(numbers) % 2 == 1:
        return numbers[middle]
    else:
        return (numbers[middle - 1] + numbers[middle]) / 2


# Returns smallest and largest values
def smallest_largest(arr):
    smallest = arr[0]
    largest = arr[0]

    for i in arr:
        if i < smallest:
            smallest = i
        if i > largest:
            largest = i

    return [smallest, largest]


# Returns array elements as a string separated by minus
def array_to_string(arr):
    result = ""

    for i in range(len(arr)):
        result += str(arr[i])

        if i < len(arr) - 1:
            result += "-"

    return result