num1 = int(input('Enter number: '))
if num1 > 0:
    print('positive')
elif num1 < 0:
    print('negative')
else: num1 == 0 
print ('zero')


user = input('Enter your password')
password = 'python123'
while user != password:
    print('Wrong password, try again')
if password == user:
    print('Acsess granted')


fruits=["banana" , "apple" , "orange" , "mango" , "cherry"]
print(fruits[2])
print(fruits[3])
print(fruits[5])
