from scavenger_hunt_with_coloring import main_program
from timinator import CONGRATS
import random

def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))

if __name__ == "__main__":
    main_program()
    channel = f'{random.choice(CONGRATS)} 🌟'
    
    message = 'Only four solutions exist that assign all students to teams and ' + \
              'ensure all siblings are assigned to the same team.'
    
    send_msg(channel, message)
