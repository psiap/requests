from urllib import request, parse
import sys

myUrl = "http://www.google.com/search?"
value = {'q': 'Yandex'}
myheader = {}
myheader['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 YaBrowser/20.3.2.242 Yowser/2.5 Safari/537.36'

try:
    mydata = parse.urlencode(value)
    print(mydata)

    myUrl = myUrl + mydata
    req = request.Request(myUrl,headers=myheader)
    otvet = request.urlopen(req)
    otvet = otvet.readlines()
    for line in otvet:
        print(line)

except Exception:
    print("Error")
    print(sys.exc_info()[1])