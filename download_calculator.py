# Write a procedure download_time which takes as inputs a file size, the
# units that file size is given in, bandwidth and the units for
# bandwidth (excluding per second) and returns the time taken to download 
# the file.
# Your answer should be a string in the form
# "<number> hours, <number> minutes, <number> seconds"

# Some information you might find useful is the number of bits
# in kilobits (kb), kilobytes (kB), megabits (Mb), megabytes (MB),
# gigabits (Gb), gigabytes (GB) and terabits (Tb), terabytes (TB).

#print 2 ** 10      # one kilobit, kb
#print 2 ** 10 * 8  # one kilobyte, kB

#print 2 ** 20      # one megabit, Mb
#print 2 ** 20 * 8  # one megabyte, MB

#print 2 ** 30      # one gigabit, Gb
#print 2 ** 30 * 8  # one gigabyte, GB

#print 2 ** 40      # one terabit, Tb
#print 2 ** 40 * 8  # one terabyte, TB

# Often bandwidth is given in megabits (Mb) per second whereas file size 
# is given in megabytes (MB).

def get_plural(unit, string):
    if unit == 1:
        return string
    else:
        return string + "s"

def convert_seconds(tot_seconds):
    hours = int(tot_seconds)  / 3600
    minutes = int( tot_seconds - hours * 3600 ) / 60
    seconds = tot_seconds - hours * 3600 - minutes * 60
    return str(hours) +" "+ get_plural(hours,"hour")+", " +str(minutes)  + " " + get_plural(minutes,"minute") +", " + str(seconds)  +" "+ get_plural(seconds,"second") 

def bytes(bw, bw_u):
    if bw_u == 'kb':
        return bw * ( 2 ** 10 )
    elif bw_u == 'kB':
        return bw * ( 2 ** 10 * 8 )
    elif bw_u == 'Mb':
        return bw * ( 2 ** 20 )
    elif bw_u == 'MB':    
        return bw * ( 2 ** 20 * 8)
    elif bw_u == 'Gb':
        return bw * ( 2 ** 30 )
    elif bw_u == 'GB':    
        return bw * ( 2 ** 30 * 8)
    elif bw_u == 'Tb':
        return bw * ( 2 ** 40 )
    elif bw_u == 'TB':    
        return bw * ( 2 ** 40 * 8)
        
    
def download_time(t, t_u, bw, bw_u):
    bw_n = bytes(bw, bw_u)     
    t_n =  bytes(t, t_u)
    tot_sec = t_n * 1.0 / bw_n
    print tot_sec
    s_rep = convert_seconds(tot_sec)
    return s_rep

print download_time(1024,'kB', 1, 'MB')
#>>> 0 hours, 0 minutes, 1 second

print download_time(1024,'kB', 1, 'Mb')
#>>> 0 hours, 0 minutes, 8 seconds  # 8.0 seconds is also acceptable

print download_time(13,'GB', 5.6, 'MB')
#>>> 0 hours, 39 minutes, 37.1428571429 seconds

print download_time(13,'GB', 5.6, 'Mb')
#>>> 5 hours, 16 minutes, 57.1428571429 seconds

print download_time(10,'MB', 2, 'kB')
#>>> 1 hour, 25 minutes, 20 seconds  # 20.0 seconds is also acceptable

print download_time(10,'MB', 2, 'kb')
#>>> 11 hours, 22 minutes, 40 seconds  # 40.0 seconds is also acceptable

print download_time(11,'GB', 5, 'MB')
#>>> 0 hours, 37 minutes, 32,8 seconds  # 

