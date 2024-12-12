from part_II_solver import main_program
from timinator import CONGRATS
import random

def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))

if __name__ == "__main__":
    main_program()
    channel = f'{random.choice(CONGRATS)} 🌟'
    
    message = 'We live in the age of Artificial Intelligence and the first rule of AI is, ' + \
              '“Show me the data!” In a different, but similar way, Algorithm X depends ' + \
              'on data. As you find more and more information to pass to Algorithm X, ' + \
              'mostly in the form of requirements, Algorithm X will make better and faster decisions.'

    send_msg(channel, message)

    send_msg(channel, '')

    message = 'Identifying requirements for mutual exclusivity can significantly boost the performance ' + \
              'of Algorithm X. For some problems, it isn’t even important to identify all the ' + \
              'mutual exclusivity. Simply identifying SOME of the mutual exclusivity ' + \
              'gives Algorithm X the intelligence necessary to refine its search and produce results much quicker.'
   
    send_msg(channel, message)
