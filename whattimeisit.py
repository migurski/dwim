from time import time
from sys import stderr, argv
from dwim import time2str, str2time
from dateutil.tz import tzutc, tzlocal

if len(argv) == 1:
    arg = str(int(time()))
    print >> stderr, 'time: ', arg

else:
    arg = argv[1]

if not arg.isdigit():
    t = str2time(arg)
    arg = t
    
    print >> stderr, 'time: ', t

print >> stderr, 'local:', time2str(int(arg), False, tzlocal())
print >> stderr, '      ', time2str(int(arg), True, tzlocal())
print >> stderr, 'utc:  ', time2str(int(arg), False, tzutc())
print >> stderr, '      ', time2str(int(arg), True, tzutc())
