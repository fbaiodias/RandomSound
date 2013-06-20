import urllib2
from BeautifulSoup import BeautifulSoup
import urllib
import os
from pydub import AudioSegment

pageUrl = "http://theremin.music.uiowa.edu/MISpiano.html"
folderUrl = "http://theremin.music.uiowa.edu/"
directory = "/media/xicombd/Storage/Sound/UniIowa/Piano"

os.chdir(directory)
page = BeautifulSoup(urllib2.urlopen(pageUrl))

for link in page.findAll('a'):
    linkUrl = link.get('href')
    
    if(".aiff" in linkUrl):
		completeUrl = folderUrl + linkUrl;
		fileName = linkUrl.split('/')[-1]
		print fileName + " started"
		urllib.urlretrieve(completeUrl, fileName)
		print fileName + " downloaded"
		aac_version = AudioSegment.from_file(fileName, "aiff")
		first_2_seconds = aac_version[:2000]
		fileName = fileName.split('.aiff')[0]
		first_2_seconds.export(fileName+".wav", format="wav")
		print fileName + " converted"

