import string
import secrets

char = string.ascii_letters + string.punctuation + string.digits
pwd = ''
for i in range(10):
    pwd += secrets.choice(char)

print (f'Your Generated Password: {pwd}')