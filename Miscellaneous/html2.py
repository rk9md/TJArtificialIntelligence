import sys, re, os.path
import requests
import html2text

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
    try:
        page = requests.get(location).text
        h = html2text.HTML2Text()
        h.ignore_images = True
        h.ignore_links = True
        text = h.handle(page)
        # finalString = ""
        # for s in text:
        #     finalString+=s.get_text()
    except:
        text= "No site found"
    print(text)