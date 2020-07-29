#for x in range(51):

def fizzbuzz(x):
    if x % 3 == 0 and x % 5 == 0:
        print("fizzbuzz")
        
    elif x % 3 == 0:
        print("fizz")
        
    elif x % 5 == 0:
        print("buzz")
    else:
        print(x)

[fizzbuzz(x) for x in range(51)]
