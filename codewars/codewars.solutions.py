def string_to_number(s):
    return int(s)

def number_to_string(num):
    return str(num)

def bool_to_word(boolean):
    if boolean:
        return "Yes"
    else:
        return "No"
    
    def opposite(number):
        return -number

def temple_strings(obj, feature): 
    return f"{obj} are {feature}"

def unusual_five():
    return len("five!")

def get_volume_of_cuboid(length, width, height):
    return length * width * height

def find_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def find_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

def find_average(numbers):
    if len(numbers)== 0:
        return 0
    return sum(numbers) / len(numbers)

def make_negative( number ):
    return -abs(number)

def descending_order(num):
    return int("".join(sorted(str(num), reverse=True)))

def square_or_square_root(arr):
    result = []
    for num in arr:
        root = 1
        
        while root * root < num:
            root += 1
        if root * root == num:
            result.append(root)
        else:
            result.append(num * num)
    return result

def count_by(x, n):
    result = []
    for i in range(1, n + 1):
        result.append(x * i)
    return result
