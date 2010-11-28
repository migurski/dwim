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
        raise EpistemicClosure('I don\'t know what you mean by "%s"' % s)

    if dt.utcoffset() is None:
        from time import mktime as tuple2epoch

        # no timezone was specified in the input, so we will assume local time.

    else:
        from calendar import timegm as tuple2epoch

        # here, dt has a populated UTC offset.
        # we subtract it from dt so we can return a value in UTC.
        dt -= dt.utcoffset()

    return int(tuple2epoch(dt.timetuple()))

def oauthdance(consumer_key, consumer_secret, request_token_url='http://twitter.com/oauth/request_token', authorize_url='http://twitter.com/oauth/authorize', access_token_url='http://twitter.com/oauth/access_token'):
    """
    """
    from oauth2 import Consumer, Client, Token
    from urlparse import parse_qsl

    con = Consumer(consumer_key, consumer_secret)
    cli = Client(con)

    res, bod = cli.request(request_token_url, 'GET')
    
    assert res['status'] == '200', 'Expected status=200, got %s.' % res['status']
    
    tok = dict(parse_qsl(bod))
    tok = Token(tok['oauth_token'], tok['oauth_token_secret'])
    
    print 'Visit this URL to get a PIN:'
    print '    %s?oauth_token=%s' % (authorize_url, tok.key)
    
    pin = raw_input('PIN: ').strip()
    
    tok.set_verifier(pin)
    cli = Client(con, tok)
    
    res, bod = cli.request(access_token_url, 'GET')
    
    assert res['status'] == '200', 'Expected status=200, got %s.' % res['status']
    
    tok = dict(parse_qsl(bod))
    tok = Token(tok['oauth_token'], tok['oauth_token_secret'])
    
    print 'Your token key is: ', tok.key
    print 'And your secret is:', tok.secret
    
    return tok
