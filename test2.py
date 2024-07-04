count = 0
def counter(func):
    def wrapper(*args,**kwargs):
        global count
        count += 1
        print(f"{func.__name__} was called")
        return func(*args,**kwargs)
    return wrapper

@counter
def example_function():
    print("Inside the function")
example_function()
example_function()
print(f"example_function was called {count} times")