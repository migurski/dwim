class EpistemicClosure(Exception): pass

def time2str(s, tz=None):
    """
    """
    from datetime import datetime

    return datetime.fromtimestamp(s, tz)

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