""" Even though there is already a randomizer module that I can import, I wanted
to create my own randomizer for fun and apply what I already know. """
import time

def unix_time():
    """ Returns the current time since unix epoch as a string to be indexed and
    used as a randomizer. """
    current_time = time.time()
    return str(current_time)

def get_numbers():
    time_now = unix_time()

    randomized_number = time_now.replace(".", "")

    number1 = int(randomized_number[-1])
    number2 = int(randomized_number[-7])

    while (number1 == 0 or number2 == 0) or (number1 + number2 > 10):
        time_now = unix_time()
        randomized_number = time_now.replace(".", "")
        number1 = int(randomized_number[-1])
        number2 = int(randomized_number[-7])
    return number1, number2

if __name__ == "__main__":
    num1, num2 = get_numbers()
    print(num1)
    print(num2)