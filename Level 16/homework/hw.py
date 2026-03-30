def average(nums):
    return sum(nums) / len(nums)

numbers = []

for i in range(5):
    num = int(input("Enter number: "))
    numbers.append(num)

print("Average:", average(numbers))


sentence = input("Enter a sentence: ")

print("Length:", len(sentence))


password = input("Enter password: ")

if password.find("1") != -1:
    print("Password contains '1'")
else:
    print("Password does not contain '1'")


    fruits = ["apple", "banana", "orange", "grape"]

fruits.append("cherry") 
fruits[3] = "Blueberry"

print(fruits)


word = input("Enter word: ")

if word[0].isupper():
    print("Perfect")
else:
    print("Your word should be capitalized!")


    fullname = input("Enter name and surname: ")

print("Uppercase:", fullname.upper())
print("Lowercase:", fullname.lower())


my_name = "Ana"

user_name = input("Enter your name: ")

if my_name.lower() == user_name.lower():
    print("Our names are similar!")
else:
    print("We have different names")


    text = "Hello world"

index = text.find("o")

print("Index:", index)


words = ["apple", "banana", "cherry"]

for i in range(len(words)):
    words[i] = words[i].upper()

print(words)


my_list = []

for i in range(3):
    data = input("Enter something: ")
    my_list.append(data)

print(my_list)


fruits = ["apple", "banana", "orange", "grape"]

new_fruit = input("Enter fruit: ")

fruits.insert(2, new_fruit)
print(fruits)