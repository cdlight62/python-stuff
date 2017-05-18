import random
import string

def generate_password(strength):
   length = random.randint(8, 15)
   return ''.join([random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(length)])

print(generate_password(5))