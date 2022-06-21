# Advanced functionality
# Functions in python are first-class OBJECTS
# Like any object, they can be defined inside another function,
# passed as an argument to another function,
# and returned from a function


####################################################################
# Passing a function into another function
####################################################################
def function_to_pass_in():
    print("I am doing something")


def some_function(func_ptr):
    print("I decorate the front of the func_ptr")
    func_ptr()
    print("I decorate the back of the func_ptr")


some_function(function_to_pass_in)
print("The name of this function is:", some_function.__name__)
print()


####################################################################
# Decorate a function (func_ptr) and return the decorated function
####################################################################
def decorate_and_return_decorator_function(func_ptr):

    def decorator_function(*args, **kwargs):
        print("I decorate the front of the func_ptr")
        loc_result = func_ptr(*args, **kwargs)
        print("I decorate the back of the func_ptr")
        return loc_result

    return decorator_function


decorated_function = decorate_and_return_decorator_function(function_to_pass_in)
decorated_function()
print("The name of this function is:", decorated_function.__name__)
print()


####################################################################
# Using a decorator!
# This will behave the same as decorated_function
####################################################################
@decorate_and_return_decorator_function
def some_decorated_function():
    print("I am going to be decorated")


some_decorated_function()
print("The name of this function is:", some_decorated_function.__name__)
print()


####################################################################
# Using a decorator on a function that requires arguments
####################################################################
@decorate_and_return_decorator_function
def some_decorated_function_with_args(num):
    loc_result = num * num

    return loc_result


result = some_decorated_function_with_args(10)
print(result)
print("The name of this function is:", some_decorated_function_with_args.__name__)
print()
