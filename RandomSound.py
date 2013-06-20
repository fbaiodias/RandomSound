from pydub import AudioSegment
import os
import random

# Variable Definitions
beatTime = 250
beatFadeTime = 100
beatLenght = beatTime + beatFadeTime / 2
beatFilesNumber = (3,8)
beatRepeatsNumber = (1,5)

# Returns a list of the path of all the wav files in a folder
def getFiles(directory):
	directoryFiles = [os.path.join(root, name)
		 for root, dirs, files in os.walk(directory)
		 for name in files
		 if name.endswith(".wav")]
	return directoryFiles

i = ''
while(i != 'x' and i != 'X'):
	if i == 'r':
		os.chdir("/media/xicombd/Storage/")
		os.system("play yeeees.wav")		
	elif i == 'h' or i == 'help':
		print " -> r to repeat last song"
		print " -> x to exit"
		print " -> any other thing to generate new song"		
	else:
		allFiles = getFiles("/media/xicombd/Storage/Sound/StudioCollectionConverted/Electro Studio")
		firstFile = "/media/xicombd/Storage/Sound/UniIowa/Piano/Piano.ff.A0.wav"

		# Gets the beat files
		chosenBeatFiles = random.sample(allFiles,  random.randint(beatFilesNumber[0], beatFilesNumber[1]))
		random.shuffle(chosenBeatFiles)

		mainBeat = AudioSegment.from_wav(firstFile)[:100]

		# Mixes the chosen beat files 
		for files in chosenBeatFiles:
			print files
			track = AudioSegment.from_wav(files)
			beginning = track[:beatLenght] - 1
			mainBeat = mainBeat.append(beginning, crossfade=beatFadeTime)

		# Gets the beat files
		chosenBeatFiles = random.sample(allFiles,  random.randint(beatFilesNumber[0], beatFilesNumber[1]))
		random.shuffle(chosenBeatFiles)

		alternativeBeat = AudioSegment.from_wav(firstFile)[:100]

		# Mixes the chosen beat files for the alternative beat
		for files in chosenBeatFiles:
			track = AudioSegment.from_wav(files)
			beginning = track[:beatLenght] + 2
			alternativeBeat = alternativeBeat.append(beginning, crossfade=beatFadeTime)

		loop = mainBeat * random.randint(beatRepeatsNumber[0], beatRepeatsNumber[1]) + alternativeBeat

		song = loop * 2	

		# Goes to a diretory and saves there the files
		os.chdir("/media/xicombd/Storage/Sound/")
		song.export("yeeees.wav", format="wav")

		os.system("play yeeees.wav")
	i = raw_input("\nEnter something (h to help): ")
