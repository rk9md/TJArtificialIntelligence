import sys, re, os.path
import requests
from bs4 import BeautifulSoup as bs

#beatiful soup and requests
location = sys.argv[1]
##########################################################################################################################
# ^(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?$#
# Regex for URLs                                                                                                         #
##########################################################################################################################
if os.path.isfile(location):
    f = open(location, mode='r')
    try:
        inp = f.read()
        print(inp)
    except:
        print("Not a file")
elif re.match("^(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?$", location):
    if re.match("^www.", location):
        location= "http://"+location
    elif not re.match("^(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)", location):
        location= "http://www."+location
    page = requests.get(location)
    soup = bs(page.content, 'html.parser')
    text = soup.get_text()
    # finalString = ""
    # for s in text:
    #     finalString+=s.get_text()
    print(text)