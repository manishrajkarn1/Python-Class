Find the second largest element in a list.

def second_largest(numbers):
    first = second = float('-inf')

    for number in numbers:
        if number > first:
            second = first
            first = number
        elif first > number > second:
            second = number 
    return second
                