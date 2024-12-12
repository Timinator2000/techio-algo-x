from part_I_solver import main_program
from timinator import CONGRATS
import random

def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))


def success():
    print("TECHIO> success true")


def fail():
    print("TECHIO> success false")
    

if __name__ == "__main__":
    main_program()
    success()
    send_msg(f"{random.choice(CONGRATS)} 🌟", "Notice how Algorithm X handles all the backtracking for us!")
