import datetime
import time
import wave
import pyaudio

def playSound(sound):
	print "Playing sound: " + sound
	
	file = wave.open("sounds/" + sound + ".wav", 'r')
	p = pyaudio.PyAudio()
	chunk = 1024
	stream = p.open(format=p.get_format_from_width(file.getsampwidth()), channels = file.getnchannels(), rate = file.getframerate(), output = True)
	data = file.readframes(chunk)
	while data != '':
		stream.write(data)
		data = file.readframes(chunk)
	if (sound == 'hour'):
		hour = int(time.strftime("%I"))
		for i in range(0, hour):
			file = wave.open("sounds/bellChime.wav", 'r')
			data = file.readframes(chunk)
			while data != '':
				stream.write(data)
				data = file.readframes(chunk)
	print "Finished playing sound."
				
def getTime():
	global nowTime
	global hour
	global minute
	global second
	nowTime = datetime.datetime.now().time()
	array = [int(time.strftime("%I")), int(time.strftime("%M")), int(time.strftime("%S"))]
	hour = array[0]
	minute = array[1]
	second = array[2]
	if (second == 0):
		print "Current time: " + str(nowTime).split('.')[0]

def checkQuarter():
	getTime()

	if (minute % 15 == 0 and second == 0): # quarter hour
		if (minute == 0):
			print "minute = 00"
			playSound('hour')
		elif (minute == 30):
			print "minute = 30"
			playSound('half')
		else:
			if (minute == 15):
				print "minute = 15"
				playSound("quarter1")
			else:
				print "minute = 15 or 45"
				playSound('quarter3')
	else:
		time.sleep(1)

while(1):
	checkQuarter()