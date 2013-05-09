#!/usr/bin/env python2

print 'Content-type: text/html\n'

from os.path import join, abspath
import cgi, sys

BASE_DIR = abspath('data')

form = cgi.FieldStorage()
filename = form.getvalue('filename', 'simple2.txt')

if not filename:
    print 'Please enter a file name'
    sys.exit()

try:
    text = open(join(BASE_DIR, filename)).read()
except IOError:
    text = ''

print """
<html>
  <head>
    <title>Editing...</title>
  </head>
  <body>
    <form action="save.cgi" method="POST">
      <b>File:</b> %s<br />
      <input type="hidden" value="%s" name="filename" />
      <b>Password:</b><br />
      <input name="password" type="password" /><br />
      <b>Text:</b><br />
      <textarea name="text" cols="40" rows="20">%s</textarea><br />
      <input type="submit" value="Save" />
    </form>
  </body>
</html>
""" % (filename, filename, text)