import lib.unix_time_randomizer as roll

num1, num2 = roll.get_numbers()

print(f"{num1} + {num2} = ")
answer = int(input("Sum: "))

if answer == (num1 + num2):
    print("CORRECT!")
    
else :
    print("Try again!")
    print(f"{num1} + {num2} = ")