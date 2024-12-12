from part_III_v1 import main_program
from timinator import CONGRATS
import random

def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))

if __name__ == "__main__":
    main_program()
    # channel = f"{random.choice(CONGRATS)} 🌟"
    # send_msg(channel, "I want you to know it is way harder to hard-code all those requirements and actions than it is to build them algorithmically with loops. " + \
    #                   "I probably had to fix 20+ typos before it worked properly. Proof that algorithms are much more precise than us humans!\n")

    # send_msg(channel, "Does it make sense where all those requirements came from? 'instrument on day' requirements had to be added for every day of the week " + \
    #                   "because Mrs. Knuth has availability on all 5 days. There are also a bunch more 'slot filled' requirements.\n")

    # send_msg(channel, "Understanding the multiplicity is usually the hardest part. Just keep in mind that scheduling a student's first lesson is a different " + \
    #                   "action than scheduling a student's second lesson. That is why Ella now has 6 entries in the actions dictionary.\n")
