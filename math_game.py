import utils.unix_time_randomizer as roll

if __name__ == "__main__":

    num1, num2 = roll.get_numbers()

    correct_answer = (num1 + num2)
    counter = 0

# Loop requests input until user gets it right, or exceeds 5 tries
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