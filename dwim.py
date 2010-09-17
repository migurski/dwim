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
        raise Exception(s)

    return int(mktime(dt.timetuple()))