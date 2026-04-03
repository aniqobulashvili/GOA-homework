
def average(numbers):
    return sum(numbers) / len(numbers)


def count_even(numbers):
    count = 0
    for num in numbers:
        if num % 2 == 0:
            count += 1
    return count


def count_odd(numbers):
    count = 0
    for num in numbers:
        if num % 2 != 0:
            count += 1
    return count


def double_values(lst):
    return [x * 2 for x in lst]


def square_values(lst):
    return [x ** 2 for x in lst]


def sum_three(a, b, c):
    return a + b + c


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def check_age(age):
    if age >= 18:
        print("Access Granted")
    else:
        print("Access Denied")


def print_names(names):
    for name in names:
        print(name)


def odd_or_even(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"


def student_grade(score):
    if 90 <= score <= 100:
        print("A")
    elif 70 <= score <= 89:
        print("B")
    elif 50 <= score <= 69:
        print("C")
    else:
        print("F")


def user_info(name, surname, age):
    return f'User: {name} {surname}, Age: {age}'



def Arithmetic_mean(numbers):
    if len(numbers) == 0:
        return 0
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)


def get_vowels(text):
    vowels = "aeiouaeiou"
    result = ""
    for char in text:
        if char in vowels:
            result += char
    return result


def unique_elements(lst):
    unique = []
    for item in lst:
        if item not in unique:
            unique.append(item)
    return unique


def manual_sum(lst):
    total = 0
    for num in lst:
        total += num
    return total