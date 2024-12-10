def test_function():
    print("Starting test")
    x = 1/0  # This will cause a ZeroDivisionError
    print("This won't be reached")

print("Before function call")
test_function()
print("After function call")