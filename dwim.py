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
    from time import mktime
    
    try:
        dt = parse(s)
    except ValueError:
        raise EpistemicClosure('I don\'t what what you mean by "%s"' % s)

    return int(mktime(dt.timetuple()))