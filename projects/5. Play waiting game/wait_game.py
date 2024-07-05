import random
import time

def waiting_game():
    num = random.randint(2,4)
    print(f"Your target time is {num} seconds.\n")
    print(f"---Press Enter to Begin---")
    
    input()
    starttime=time.time()
    print(f"...Press Enter again after {num} seconds...")

    input()
    lastime =time.time()
    timebetween = lastime - starttime

    print(f"Elapsed time: {timebetween:.3f} seconds")
    if timebetween > num:
        print(f"({timebetween-num:.3f} too fast)")
    if timebetween < num: 

        print(f"({num-timebetween:.3f} too slow)")
    if timebetween == num: 
        print(f"Congratulations, you were on time!")
waiting_game()
