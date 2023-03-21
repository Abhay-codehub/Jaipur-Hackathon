import schedule
import time

named_tuple = time.localtime() # get struct_time
time_string = time.strftime("%H:%M:%S", named_tuple)

print(time_string)