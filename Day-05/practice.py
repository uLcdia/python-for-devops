from logging import log
import sys
import argparse
from urllib import response
import requests

""" 
args=map()
if len(sys.argv) > 1:
    args['verbose'] = any(flag in sys.argv for flag in ('-v', '--verbose'))

    args['count'] = 1
    for opt in ('-c', '--count'):
        if opt in sys.argv:
            try:
                index = sys.argv.index(opt)
                args['count'] = int(sys.argv[index + 1])
            except IndexError:
                log("Error: Missing value for count option")
            break
 """


arg_parser = argparse.ArgumentParser('AltCurl')

arg_parser.add_argument('url', type=str, help='URL to fetch')
arg_parser.add_argument('-m', '--method', choices=('GET', 'POST'), default='GET', help='HTTP method to use')
arg_parser.add_argument('-d', '--data', type=str, help='Data to send with the request (for POST method)')
# arg_parser.add_argument('-h', '--help', action='help', help='Show this help message and exit') # argparse automatically adds this
arg_parser.add_argument('-s', '--silent', action='store_true', help='Silent mode')
arg_parser.add_argument('-v', '--verbose', action='store_true', help='Make the operation more talkative')
arg_parser.add_argument('-o', '--output', type=str, help='Write to file instead of stdout')

args = arg_parser.parse_args()

if args.method == 'POST' and args.data is None:
    arg_parser.error('the following arguments are required when using -m POST: -d/--data')

if args.silent and args.verbose:
    arg_parser.error('Cannot use both --silent and --verbose options together')
    # curl allows it though

method = args.method
url = args.url
data = args.data
req = requests.Request(method, url, data=data)
prepared = req.prepare()

if args.verbose:
    print(f"Method: {prepared.method}")
    print(f"URL: {prepared.url}")
    print(f"Headers: {prepared.headers}")

if args.silent:
    # Not going to implement
    pass

with requests.Session() as session:
    response = session.send(prepared)

if args.output:
    with open(args.output, 'w') as f:
        f.write(response.text)
else:
    print(response.text)

if args.verbose:
    print(f"Status code: {response.status_code}")
    print(f"Response headers: {response.headers}")
