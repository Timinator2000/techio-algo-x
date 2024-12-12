from part_III_v2 import main_program
from timinator import CONGRATS
import random

def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))

if __name__ == "__main__":
    main_program()
    channel = f"{random.choice(CONGRATS)} 🌟"
    send_msg(channel, "So much better without those duplicates, right? And way faster on the big test cases!")
