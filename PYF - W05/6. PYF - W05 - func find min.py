def get_min_numbers(numbers):
    result = numbers[0]
    for num in numbers:
            if result > num:
                result = num
    return result
numbers = [10, 9, 21, 36, 2]
min_number = get_min_numbers(numbers)
print("Min number: ", min_number)