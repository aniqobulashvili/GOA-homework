# 1. შექმენით პროგრამა, რომელიც შეამოწმებს, არის თუ არა მომხმარებლის მიერ შეყვანილი სიტყვა მთლიანად დიდ ასოებში
# 2. მომხმარებელს შეაყვანინე სიტყვა და ერთი ასო. იპოვე ამ ასოს მდებარეობა სიტყვაში
# 3. fruits = ['apple','banana','peach','pineapple'] სიაში ჩაამატეთ შესაბამისი მეთოდით 3 ახალი ელემენტი ხოლო შემდეგ დაპრინტეთ სიის სიგრძე

word = input('enter a word')
if word != word.upper():
    print('the word isnt in upper case')

word = input('enter a word')
letter = input('enter a letter')
print('word'.find('o'))


fruits = ['apple','banana','peach','pineapple']
fruits.append('strawberry')
fruits.append('pear')
fruits.append('orange')
print(fruits)
