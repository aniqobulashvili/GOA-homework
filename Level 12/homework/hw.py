num = int(input("Enter number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")


temp = int(input("Enter temperature: "))

if temp > 30:
    print("It's Hot")
elif 15 <= temp <= 30:
    print("It's Warm")
else:
    print("It's Cold")


num = int(input("Enter number: "))

if num > 0:
    if num % 2 == 0:
        print("Positive even")
    else:
        print("Positive odd")
else:
    print("Negative")


    num = int(input("Enter number: "))

for i in range(num + 1):
    if i % 2 == 0:
        print(i, "Even")
    else:
        print(i, "Odd")


        positive = 0
negative = 0
zero = 0

for i in range(10):
    num = int(input("Enter number: "))
    
    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1
    else:
        zero += 1

print("Positive:", positive)
print("Negative:", negative)
print("Zero:", zero)


fruits = ["apple", "banana", "orange", "grape"]

fruits[1] = "kiwi"

print(fruits)


nums = [4, 8, 12, 16, 20]

result = nums[0] + nums[-1]

print(result)


my_list = [1, 2, 3, 4, 5]

for item in my_list:
    print(item)


    nums = [1, 2, 3, 4, 5, 6]

for num in nums:
    if num % 2 == 0:
        print(num)


        nums = [1, 2, 3, 4, 5, 6]

sum_even = 0

for num in nums:
    if num % 2 == 0:
        sum_even += num

print(sum_even)


nums = [2, 5, 7, 9, 3, 10]

for num in nums:
    if num > 6:
        print(num)


        word = "hello"

for letter in word:
    print(letter)


    nums = [1, 2, 3, 4, 5]

print(nums[:3])