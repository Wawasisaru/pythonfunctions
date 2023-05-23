def even_Numbers():
    x = range(10)
    for i in x:
        if i%2 == 0:
            print(i)

def odd_Numbers():
    y = range(10)
    for i in y:
        if(i%2!= 0):
            print(y)
# else statement can be opitianally be combined with an else statement. 
# The code inside else will be executed if the preceding if statement returns false
def divisible_by_5():
    x = range(50)
    for i in x:
        if i%5 == 0:
            print(f"{i} is divivble by 5")
        else:
            print(f"{i} is not divible by 5")
# ELIF statement  it allows to do more than one comparison in the flow
def mutiple_comparison():
    x = range(50)
    for i in x:
        if i%5 == 0:
            print(f"{i} is divivble by 5")
        elif i%7 == 0:
            print(f"{i} is divisible by 7")
        elif i%9 == 0:
            print(f"{i} is divisible by 9")
        else:
            print(f"{i}  is not divisible by 5,7,9")

# combine if statement with logical operators && ||
def add_or_even():
    x = range(20)
    for i in x:
        if i%2 == 0 and i%3 == 0:
            print(f"{i} is divisble by both 2 and 3")
        elif i%2 == 0 or i%3 == 0:
            print(f"{i} is divisble by both 2 or 3")
        else:
            print(f"{i} is divisble by either 2 or 3")

# while loop it continue running as long as the set condition remains true

def while_loop():
    x=1
    while x<10:
        print("HELLO!")
        x+=1

# break statement stops the while condition even if statement is true
def break_statement():
    x = 1
    while x<10:
        print("hello")
        x+=1
        if x==5:
            break
# contine statement skips the reminder of the current iteration and goes to the next iteration.
def continue_statement():
    x=0
    while x<=20:
       x+=1
       if x%3==0:
          continue
       print(x)