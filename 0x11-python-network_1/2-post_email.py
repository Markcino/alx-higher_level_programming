#!/usr/bin/python3
"""takes url & email, sends a POST request and displays the response"""
from urllib import request, parse
from urllib.error import URLError
from sys import argv

if len(argv) > 2:
    email = {'email': argv[2]}
    data = parse.urlencode(email).encode('ascii')
    req = request.Request(argv[1], data)
    try:
        with request.urlopen(req) as response:
            r = response.read()
            print(r.decode('utf-8'))
    except URLError as e:
        print(f"Error: {e.reason}")
        