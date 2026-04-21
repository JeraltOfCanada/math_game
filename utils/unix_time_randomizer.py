""" Even though there is already a randomizer module that I can import, I wanted
to create my own randomizer for fun and apply what I already know. """
import time

HIGHEST_SUM = 12

def unix_time():
    """ Returns the current time since unix epoch as a string. """
    current_time = time.time()
    return str(current_time)

def get_numbers():
    """ Creates 2 indices of unix_time and has a check to ensure sum of two
     indices isn't higher than 12. """
    time_now = unix_time()
    randomized_number = time_now.replace(".", "")
    num1 = int(randomized_number[-1])
    number2 = int(randomized_number[-7])
    num2 = number2 % (HIGHEST_SUM - num1)
    return num1, num2

if __name__ == "__main__":
    num1, num2 = get_numbers()

    print(num1)
    print(num2)