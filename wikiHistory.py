import urllib2
import re
from bs4 import BeautifulSoup
import time
iterate = 0
vandalTest = []
def GetRevisions(pageTitle):
    url = "https://en.wikipedia.org/w/api.php?action=query&format=xml&prop=revisions&rvlimit=500&titles=" + pageTitle #+"&rvprop=ids|comment|content"
    altURL = "https://en.wikipedia.org/w/api.php?action=query&titles=September_11_attacks&prop=revisions&rvprop=ids|comment|content&rvlimit=5&rvdifftotext=prev&format=xml&callback=?"
    
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
revisions = GetRevisions("David_P._Steiner")
vandalismRev = []
vandalIDs = []
revIDs = {}
print(len(revisions))

for i in revisions:
    if "vandalism" in i:
        vandalismRev.append(i)
        #print(i)
vandalNum = len(vandalismRev)
print(vandalNum)

for z in vandalismRev:
    yoof = z.split("revid=\"")[1].split("\"")
    #foo = z.split("parentid=\"")[1]
    #bar = foo.split("\"")[0]
    revisionID = yoof[0]
    parentID = yoof[2]
    revIDs[revisionID] = parentID
    vandalIDs.append(parentID)
    #print(bar)


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

t = getDiff("David_P._Steiner", vandalIDs)
#for z in t:
#	print(z)

filename = "kinkaid.html"
fz = open(filename, "w")
fz.writelines(t)
fz.write("</html>")
#for z in t:
#	fz.write(z)
fz.close()

