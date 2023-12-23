import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','(',')','*','+']

print("Welcome to the PyPassword Generator! ")
letters_input = int(input("How many letters would you like in your password?\n"))
symbols_input = int(input("How many symbols would you like in your password?\n"))
numbers_input = int(input("How many numbers would you like in your password?\n"))

#easy level

#password = ""
#for char in range(1, letters_input + 1):
#    rand_char = random.choice(letters)
#    password += rand_char
#for num in range(1, numbers_input + 1):
#   rand_num = random.choice(numbers)
#  password += rand_num
#for sym in range(1, symbols_input + 1):
#   rand_sym = random.choice(symbols)
#  password += rand_sym

#hard level

password = []
for char in range(1, letters_input + 1):
    rand_char = random.choice(letters)
    password += rand_char
for num in range(1, numbers_input + 1):
    rand_num = random.choice(numbers)
    password += rand_num
for sym in range(1, symbols_input + 1):
    rand_sym = random.choice(symbols)
    password += rand_sym
random.shuffle(password)
print(password)

password_change = ""
for char in password:
    password_change += char
print(f"Your password is: {password_change}")


