from functools import wraps

# def outer_function():
#     message = "Hi"

#     def inner_function():
#         print(message)

#     # return inner_function()
#     return inner_function


def decorator_function(original_function):
    @wraps(original_function)
    def wrapper_function(*args, **kwargs):
        print("wrapper executed this before {}".format(original_function.__name__))
        return original_function(*args, **kwargs)

    return wrapper_function


# outer_function()
# my_func = outer_function()
# my_func()
# my_func()


class decorator_class(object):
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print(
            "Call method executed this before {}".format(
                self.original_function.__name__
            )
        )
        return self.original_function(*args, **kwargs)


@decorator_function
# @decorator_class
def display():
    print("display function ran")


@decorator_function
# @decorator_class
def display_info(name, age):
    print("display_info ran with arguments ({}, {})".format(name, age))


# decorator_display = decorator_function(display)
# decorator_display()

display()

display_info("John", 25)
