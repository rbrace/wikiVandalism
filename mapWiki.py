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
	dictFilt = {}
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
			tempID = str(child.attrib).split("'revid': \'")[1].split("\'")[0]
            filt.append(tempID)
			tempTitle = str(child.attrib).split("\'title=\"")[1].split("\"")
			print(tempTitle)
			dictFilt.update({tempID:tempTitle}) 
            #print(child.attrib)
        #filt += child
    #zzz = re.findall('<rc type="edit"*>', response)    
    return filt;

def locate(IP_List):
    #'http://api.hostip.info/get_html.php?ip=12.215.42.19&position=true'
    for IP in IP_List:
        response = urllib.urlopen('http://api.hostip.info/get_html.php?ip=' + IP + '&position=true').read()


def getDiff(pTitle, revList):
	iterate = 0
	changes = []
	header = {'User-Agent': 'Mozilla/5.0'} 
	wiki = "https://en.wikipedia.org/w/index.php?title="+pTitle+"&diff="
	if iterate%10==0:
		time.sleep(5)
	for d in revList:
		tempWiki = wiki + d
		req = urllib2.Request(tempWiki, headers=header)
		tempPage = urllib2.urlopen(req)
		tempSoup = BeautifulSoup(tempPage)
		additions = str(tempSoup.find_all("td", {"class" : "diff-addedline"}))
		if len(additions.split(" ")) < 1000:
			changes += "<tr>"
			changes += additions
			changes += "</tr>"
		iterate+=1

	return changes


test = []
test = mostRecent()

print(test)
print("test")
#for z in test:
 #   print(z)

