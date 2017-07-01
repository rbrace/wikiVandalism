import xml.etree.ElementTree as ET
import urllib2
import re
#from bs4 import BeautifulSoup
import time
"""
iterate = 0
vandalTest = []
def GetRevisions(pageTitle):
    url = "https://en.wikipedia.org/w/api.php?action=query&format=xml&prop=revisions&rvlimit=500&titles=" + pageTitle #+"&rvprop=ids|comment|content"
    ###altURL = "https://en.wikipedia.org/w/api.php?action=query&titles=September_11_attacks&prop=revisions&rvprop=ids|comment|content&rvlimit=5&rvdifftotext=prev&format=xml&callback=?"
    
    revisions = []                                        #list of all accumulated
    next = ''                                             #information for the next request
    while True:
        response = urllib2.urlopen(url + next).read()     #web request
        temp = re.findall('<rev [^>]*>', response)
            
        revisions += temp #adds all revisions from the current request to the list
        cont = re.search('<continue rvcontinue="([^"]+)"', response)
        if not cont:                                      #break the loop if 'continue' element missing
            break
        next = "&rvcontinue=" + cont.group(1)             #gets the revision Id from which to start the next request
    return revisions;
"""
def mostRecent():
    filt = []
    rcURL = "https://en.wikipedia.org/w/api.php?action=query&list=recentchanges&rcprop=title|ids|sizes|user|comment&rclimit=500&format=xml"
    #rcURL = "https://en.wikipedia.org/w/api.php?action=query&list=recentchanges&rcprop=title|ids|flags&rclimit=500&format=xml"
    response = urllib2.urlopen(rcURL).read()
    root = ET.fromstring(str(response))
    #root = tree.getroot()
    #print(root.
    #print(root[1][0])
    for child in root[1][0]:
        if 'vandalism' in str(child.attrib):
            #print(child.attrib)
            print(str(str(child.attrib).split("'revid': \'")[1].split("\'")[0]))
            #print(child.attrib)
        #filt += child
    #zzz = re.findall('<rc type="edit"*>', response)    
    return filt;

def locate(IP_List):
    #'http://api.hostip.info/get_html.php?ip=12.215.42.19&position=true'
    for IP in IP_List:
        response = urllib.urlopen('http://api.hostip.info/get_html.php?ip=' + IP + '&position=true').read()


test = []
test = mostRecent()
print("test")
for z in test:
    print(z)
print(len(test))

