x = 10
def multiply_by_three(x):
    return x * 3


def augmented_multiply_by_three(x):
    return 2*(10 * 3)

arguments = {
    x : 10
    
}

print(multiply_by_three(10))
x = augmented_multiply_by_three(10)
print(augmented_multiply_by_three(x))
print ("Arguments are: "+str(x))
