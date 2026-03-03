Total=0
for number in range(1,101):
    Total+=number #like we've done before , using this and having total=0 at the top is good for adding values or scores etc
print(Total)

for Number in range(1,101):
    if Number%3==0 and Number%5==0:
        print("FizzBuzz")
    elif Number%3==0:
        print("Fizz")
    elif Number%5==0:
        print("Buzz")
    else:
        print(Number)


