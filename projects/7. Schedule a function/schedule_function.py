# imputs event time, function, any number of arguments 
# example of call to schedule_function
# schedule_function(time.time()+1, print, 'Howdy!')
import sched
import time 

def schedule_function( timegiven, func, *args ):
    scheduler = sched.scheduler(time.time, time.sleep)
    scheduler.enterabs(timegiven ,1,func,argument=args);
    scheduler.run()
    return None

schedule_function(time.time() + 1, print, 'Howdy!','How are you?')

