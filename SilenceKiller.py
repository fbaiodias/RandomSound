from pydub import AudioSegment
from pydub.utils import db_to_float
import os
import random

# Returns a list of the path of all the aiff files in a folder
def getFiles(directory):
	directoryFiles = [];
	os.chdir(directory)
	for files in os.listdir("."):
		if files.endswith(".aiff"):
			directoryFiles += [files]
	return directoryFiles

originalDir = "/media/xicombd/Storage/Sound/UniIowa/Piano"
finalDir = originalDir
allFiles = getFiles(originalDir)

# Converts the chosen files
if not os.path.exists(finalDir):
    os.makedirs(finalDir)
os.chdir(finalDir)
for files in allFiles:
	print files
	# Let's load up the audio we need...
	track = AudioSegment.from_file(originalDir + "/" + files, format="aiff")
	# Let's consider anything that is 30 decibels quieter than
	# the average volume of the podcast to be silence
	average_loudness = track.rms
	silence_threshold = average_loudness * db_to_float(-1)
	# filter out the silence
	track_parts = (ms for ms in track if ms.rms > silence_threshold)
	# combine all the chunks back together
	track = reduce(lambda a, b: a + b, track_parts)
	# save the result
	fileName = files.split('.aiff')[0]
	track.export(fileName + ".wav", format="wav")

