# Write a short program that prints each number from 1 to 100 on a new line. 
# For each multiple of 3, print "Fizz" instead of the number. 
# For each multiple of 5, print "Buzz" instead of the number. 
# For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of the number.


def fizzbuzz(x): #defines function
    if x % 15 == 0: # if x is a number that gives moduolo 15 = 0 therefore is a multiple of 15, in other words a multiple of 3 and 5
        print("FizzBuzz") #prints fizzbuzz
        
    elif x % 3 == 0: #if it is not moduolo 15 = 0, check for moduolo 3 = 0 then print fizz is this proves true
        print("Fizz")
        
    elif x % 5 == 0: #same as before
        print("Buzz")
    else:   #if it is neither of these options then print the number
        print(x)

[fizzbuzz(x) for x in range(1,101)] #run the defined function for every value of x between 1 and 101 not including 101



Faster Solution:


for i in range(1,101):print("Fizz"*(i%3<1)+(i%5<1)*"Buzz"or i)

#for every interger i in a range of 1 and 101 not including 101, print r
#Fizz if i moduolo 3 is less than 1 ( the only possible value is 0) therefore 0<1 using boolean operations gives us 0<1 
#which is True and goes ahead and print Fizz (if this is False , fizz will not print) The same applies to Buzz, this 
# efficient as it lets us combine get FizzBuzz if both moduolos prove true. If neither is True, aka both are shown to be false , it will print i, given by the or operator