#!/usr/bin/python

import http.client, urllib.request, urllib.parse, urllib.error, sys

# Define the parameters for the POST request and encode them in
# a URL-safe format.
f = open('jquery.i18n.properties.js', 'r')

params = urllib.parse.urlencode([
    ('js_code', f.read()),
    ('compilation_level', 'SIMPLE_OPTIMIZATIONS'),
    ('output_format', 'text'),
    ('output_info', 'compiled_code'),
  ])
f.close()
# Always use the following value for the Content-type header.
headers = { "Content-type": "application/x-www-form-urlencoded" }
conn = http.client.HTTPSConnection('closure-compiler.appspot.com')
conn.request('POST', '/compile', params, headers)
response = conn.getresponse()
data = response.read()

#print data
f2 = open('jquery.i18n.properties.min.js', 'wb')
f2.write(data)
f2.close()

conn.close
