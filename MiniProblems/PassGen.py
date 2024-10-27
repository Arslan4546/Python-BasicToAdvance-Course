import random
import string
pass_len = 12
charValues = string.ascii_letters + string.digits + string.punctuation
# Method 1

# password = ""
# for i in range(pass_len):
#     password += random.choice(charValues)


# list comprehension

# Method 2
resutl ="".join([random.choice(charValues) for i in  range(pass_len)])


print(resutl)

