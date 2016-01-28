#!/usr/bin/env python

import os, json, cgi

print "Content-type: text/html"
#print "Location: http://google.ca/"
#works on real webserve, but not on python
print
print "<HTML><BODY><h1>Hello, World!</h1>"
print "<form method='POST'><input name='x'></form>"

form = cgi.FieldStorage()

print "<P>X was:"+cgi.escape(str(form.getvalue("x")))
#html escape 
print "<P>"
#print json.dumps(dict(os.environ), indent=4)
print "</BODY></HTML>"
