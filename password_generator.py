import random

print("Welcome to the password Generator?")

letters_list=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
        'q','r','s','t','u','v','w','x','y','z','A','B','C',
        'D','E','F','G','H','I','J','K','L','M','N','O'
        ,'P','Q','R','S','T','U','V','W','X','Y','Z']
numbers_list=['0','1','2','3','4','5','6','7','8','9']

symbols_list=['!','@','#','$','%','^','&','*','(',')','+','-']

letters=int(input("how many letters would you like in your password?"))

symbols=int(input("How many symbols would you like?"))

numbers=int(input("How many numbers would you like"))

password=[]
for i in range(letters):
    letter=random.choices(letters_list)
    print(letter)
    print(type(letter))
    password=password+letter

for i in range(symbols):
    symbol=random.choices(symbols_list)
    password=password+symbol

for i in range(numbers):
    number=random.choices(numbers_list)
    password=password+number


print(f"The password is : {password}")
shuffle=random.shuffle(password)
print(f"The password is : {password}")