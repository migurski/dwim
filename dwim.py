class EpistemicClosure(Exception): pass

def time2str(s, fancy=False, tz=None):
    """
    """
    from datetime import datetime
    from time import strftime

    time = datetime.fromtimestamp(s, tz)
    
    if fancy:
        zone = str(time)[-6:]
        full = strftime('%a, %d %b %Y %H:%M:%S ', time.timetuple())
        
        return full + zone
    else:
        return str(time)

def str2time(s):
    """
    """
    from dateutil.parser import parse
    
    try:
        dt = parse(s)
    except ValueError:
        raise EpistemicClosure('I don\'t what what you mean by "%s"' % s)

    if dt.utcoffset() is None:
        from time import mktime as tuple2epoch

        # no timezone was specified in the input, so we will assume local time.

    else:
        from calendar import timegm as tuple2epoch

        # here, dt has a populated UTC offset.
        # we subtract it from dt so we can return a value in UTC.
        dt -= dt.utcoffset()

    return int(tuple2epoch(dt.timetuple()))
