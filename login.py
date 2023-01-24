#!/usr/bin/env python3

import cgi
import cgitb
cgitb.enable()

from templates import login_page, secret_page, after_login_incorrect
import os
import secret 
from http.cookies import SimpleCookie

s = cgi.FieldStorage()
username = s.getfirst("Username")
password = s.getfirst("Password")

cookie = SimpleCokkie(os.environ["HTTP_COOKIE"])



print("Content-Type: text/html")

print()

if not username and not password:
      print(login_page())
else:
    print(login_page())
    print()