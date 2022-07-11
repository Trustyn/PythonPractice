#For loops
primes = [2,4,5,7]
for prime in primes:
    print(prime) #Prints full list 2,4,5,7

for x in range(5):
    print(x) #Prints 0,1,2,3,4

for x in range(3,6):
    print(x) #Prints 3,4,5

for x in range(3,8,2):
    print(x) #Prints 3,5,7

#While loops
count = 0
while count < 5:
    print(count)
    count += 1 

#Break and Continue
# Break is used to exit a loop, Continue is used to skip the current block.
while True:
    print(count) #Prints 0,1,2,3,4
    count += 1
    if count >= 5:
        break

for x in range(10):
    if x % 2 == 0: #Check if x is even
        continue
    print(x) #Prints odd numbers 1,3,5,7,9

#Else clause loops
#If break is used else is skipped, if continue is used else is still executed.
while(count < 5):
    print(count)
    count += 1
else:
    print("count value reached %d" % (count))

for i in range(1, 10):
    if(i % 5 == 0):
        break
    print(i)
else:
    print("This is not printed because the for loop is termintated becaues of the break and not the failed condition.")
