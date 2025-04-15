import base64

input = [
    "Hello, world!",
    "<script>alert('XSS')</script>",
    "<img src=x onerror=alert(1)>",
    "%3Cscript%3Ealert('x')%3C%2Fscript%3E",
    "<ScRiPt>alert('test')</ScRiPt>",
    "data:text/html;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg=="
]


for k in input:
    if "alert" in k or "script" in k:
        print("xss")
    else:
        print("not xss")


# this is just to test jenkins