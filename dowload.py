from urllib import request
import sys

myUrl = "http://adv400.tripod.com/kartinka.jpg"
myFile = r"C:\Users\dom\Desktop\nd\f.jpg"

try:
    print("Start Down" + myUrl)

    request.urlretrieve(myUrl,myFile)
except Exception:
    print("Error")
    print(sys.exc_info())
    exit

print("Fille URA")