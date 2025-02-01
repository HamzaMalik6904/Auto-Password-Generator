import random
import string

pass_length=12
values=string.ascii_letters+string.digits+string.punctuation
password=""
for i in range(pass_length):
    password+=random.choice(values)

print("your random password is : ",password) 