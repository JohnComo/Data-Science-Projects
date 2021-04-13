import random 

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
uppercases = alphabet.upper()
lowercases = alphabet.lower()
digits = '0123456789'
special_chars = '()[]{}!@#$%^&*?,.<>'

upper, lower, nums, symbols = True, True, True, True 

password = ''

# Makes one big string named password
if upper: 
    password += uppercases
if lower: 
    password += lowercases
if nums: 
    password += digits
if symbols: 
    password += special_chars

# Number of passwords 
amount = 10 

for x in range(amount): 
    final_password = ''.join(random.sample(password, random.randrange(8,17)))
    print(final_password)