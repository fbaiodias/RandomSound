from pydub import AudioSegment
import os
import random
import urllib2

# Returns a list of the path of all the wav files in a folder
def getFiles(directory):
	directoryFiles = [os.path.join(root, name)
		 for root, dirs, files in os.walk(directory)
		 for name in files
		 if name.endswith(".wav")]
	return directoryFiles

originalDir = "/media/xicombd/Storage/Sound/StudioCollection"
finalDir = "/media/xicombd/Storage/Sound/StudioCollectionConverted"
allFiles = getFiles(originalDir)

# Converts the chosen files
for files in allFiles:
	relativePath = "/".join(files.split(originalDir)[-1].split('/')[:(len(files.split(originalDir)[-1].split('/'))-1)])
	
	if not os.path.exists(finalDir + relativePath):
		os.makedirs(finalDir + relativePath)
	os.chdir(finalDir + relativePath)
	
	print "relativePath: " + relativePath
	print "files: " + files
	#print "navigated to: " + finalDir + relativePath
	
	fileName = files.split("/")[-1].split('.wav')[0]

	track = AudioSegment.from_file(files, format="wav")
	track.export(fileName + ".aiff", format="aiff")

	convertedTrack = AudioSegment.from_file(fileName + ".aiff", format="aiff")
	convertedTrack.export(fileName + ".wav", format="wav")
    

