a = 5
b = 0

try:
    print("resource open")
    print(a/b)
except Exception as e:
    print("Can't divide by Zero", e)
finally:
    print("resource closed")