import lib.unix_time_randomizer as roll

num1, num2 = roll.get_numbers()

print(f"{num1} + {num2} = ")
answer = int(input("Sum: "))

while answer != (num1 + num2):
    print("Try again!")
    print(f"{num1} + {num2} = ")
    answer = int(input("Sum: "))  

else :
    print("CORRECT!")
    