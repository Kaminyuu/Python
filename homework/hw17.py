import re


def password(pas):
    return re.findall("^[A-Za-z0-9_@-]{6,18}$", pas)


print(password("my-p@ssw0rd"))
