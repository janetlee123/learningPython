# imputs event time, function, any number of arguments 
# example of call to schedule_function
# schedule_function(time.time()+1, print, 'Howdy!')
import schedule
import time 

def schedule_function( time, func, *args ):
    schedule.every(time,func,*args)



