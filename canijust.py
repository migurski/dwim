from sys import stderr, exit
from optparse import OptionParser
from dwim import oauthdance

parser = OptionParser(usage="""%prog [options] <consumer key> <consumer secret>""")

defaults = {
    'request_token_url': 'http://twitter.com/oauth/request_token',
    'authorize_url': 'http://twitter.com/oauth/authorize',
    'access_token_url': 'http://twitter.com/oauth/access_token'
    }

parser.set_defaults(**defaults)

parser.add_option('-r', '--request-token-url', dest='request_token_url',
                  help='Default: %s' % defaults['request_token_url'])

parser.add_option('-a', '--authorize-url', dest='authorize_url',
                  help='Default: %s' % defaults['authorize_url'])

parser.add_option('-t', '--access-token-url', dest='access_token_url',
                  help='Default: %s' % defaults['access_token_url'])

if __name__ == '__main__':
    options, args = parser.parse_args()
    
    try:
        key, secret = args
    except ValueError:
        print >> stderr, 'Need a key and secret, got: ' + repr(args)
        exit(1)

    oauthdance(key, secret, options.request_token_url, options.authorize_url, options.access_token_url)
