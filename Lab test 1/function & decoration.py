a = 3
b = 4
def add_numbers(a,b):
    return a + b

def decoration_function(a, b):
    return (2*(3+4))

print(add_numbers(3, 4))
x = decoration_function(3,4)
print(decoration_function(a, b))
print("Arguments are: "+str(a)+", "+str(b))