person = {"name": "Jenn", "age": 23}


sentence = (
    "My name is " + person["name"] + " and I am " + str(person["age"]) + " years old."
)

sentence2 = "My name is {} and I am {} years old.".format(person["name"], person["age"])
sentence3 = "My name is {0} and I am {1} years old. Just call me {0}".format(
    person["name"], person["age"]
)

sentence4 = "My name is {0[name]} and I am {1[age]} years old.".format(person, person)
sentence4 = "My name is {0[name]} and I am {0[age]} years old.".format(person)

sentence5 = "My name is {name} and I am {age} years old.".format(name="Jenn", age=23)
sentence6 = "My name is {name} and I am {age} years old.".format(**person)
# print(sentence6)

for i in range(1, 11):
    sentence = "The value is {:03}".format(i)
    # print(sentence)

pi = 3.14159265

sentence = "Pi is equal to {:.3f}".format(pi)
# print(sentence)

sentence = "1 MB is equal to {:,.2f} bytes".format(1000 ** 2)
# print(sentence)

import datetime

my_date = datetime.datetime(2019, 9, 24, 12, 30, 45)
# print(my_date)

sentence = "{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of the week".format(
    my_date
)

print(sentence)
