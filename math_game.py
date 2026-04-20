import lib.unix_time_randomizer as roll

num1, num2 = roll.get_numbers()

correct_answer = (num1 + num2)
counter = 0

while True:
    print(f"{num1} + {num2} = ")
    answer = int(input("Sum: "))
    counter = counter + 1
    if answer == correct_answer:
        print("CORRECT!")
        break
    if answer != correct_answer and counter <= 5:
        print("Try again!")
    else:
        print("You lost!")
        break