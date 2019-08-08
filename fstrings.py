from datetime import datetime

first_name = "Homer"
last_name = "Simpson"

# sentence = "My name is {} {}".format(first_name, last_name)
# sentence = f"My name is {first_name} {last_name}"
# sentence = f"My name is {first_name.upper()} {last_name.upper()}"

person = {"name": "Jenn", "age": 23}

# sentence = "My name is {} and I am {} years old".format(person["name"], person["age"])

# for n in range(1, 11):
#     sentence = f"The value is {n:02}"
#     print(sentence)

pi = 3.14159265

# sentence = f"Pi is equal to {pi:.4f}"

birthday = datetime(1990, 1, 1)

sentence = f"Jenn has a birthday on {birthday:%B %d, %Y}"

print(sentence)
