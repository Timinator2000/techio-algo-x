from part_I_solver import main_program
import random

def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))

if __name__ == "__main__":
    main_program()
    send_msg(f"Mission Accomplished? 🌟", "Were you able to create all the error situations?")
