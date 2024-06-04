# imputs event time, function, any number of arguments 
# example of call to schedule_function
# schedule_function(time.time()+1, print, 'Howdy!')
import sched
import time 

def schedule_function( time, func, *args ):
    scheduler = sched.scheduler(time.time(), time.sleep() )
    scheduler.enter(time,func,*args)



