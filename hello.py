#!/usr/bin/env python

import json, os, cgi, Cookie

form = cgi.FieldStorage()

username = form.getvalue('user')
password = form.getvalue('password')

C = Cookie.SimpleCookie()
C.load(os.environ['HTTP_COOKIE'])

print "Content-Type: text/html"
if username == 'bob' and password == 'hunter2':
    print "Set-Cookie: loggedin=True"
else:
    print "Set-Cookie: loggedin=False"

print
print "<HTML><BODY>"
print "<H1>Hello world!</H1>"
print "Your magic tracking number is:"
print form.getvalue('magic_tracking_number')
if "Firefox" in os.environ['HTTP_USER_AGENT']:
    browser = "Firefox"
elif "Chrome" in os.environ['HTTP_USER_AGENT']:
    browser = "Chrome"
else:
    browser
print "<P>Your Browser is " + browser + "</P>"

print "<FORM method='POST'>Username: <INPUT name='user'>"
print "<P>Password: <INPUT name='password' type='password'>"
print "<P><INPUT type='submit'></FORM>"

if "loggedin" in C:
    print "<P>Logged in: " + str(C['loggedin'].value)
else:
    print "<P>No cookie"



#print "<P><P>Username: " + form.getvalue('user')
#print "<P>Password: " + form.getvalue('password')

#print json.dumps(dict(os.environ), indent = 2, sort_keys = True)
