# create a sound file in AU format playing a sine wave
# of a given frequency, duration and volume
# vegaseat code modified to work with Python27 and Python32
from struct import pack
from math import sin, pi
from io import StringIO
from pydub import AudioSegment
import subprocess
from memoryAcoustatic import *
import pprint
pp = pprint.PrettyPrinter(indent=4)
def au_file(name='test.au', freq=440, dur=1000, vol=0.5):
    """
    creates an AU format sine wave audio file
    of frequency freq (Hz)
    of duration dur (milliseconds)
    and volume vol (max is 1.0)
    """
    fout = open(name, 'wb')
    # header needs size, encoding=2, sampling_rate=8000, channel=1
    fout.write(pack('>4s5L', '.snd'.encode("utf8"), 24, 8*dur, 2, 8000, 1))
    factor = 2 * pi * freq/8000
    # write data
    for seg in range(8 * dur):
        # sine wave calculations
        sin_seg = sin(seg * factor)
        val = pack('b', int(vol * 127 * sin_seg))
        fout.write(val)
    fout.close()
    

#crear el sonido maestro
def outputTrack(playList):
	au_file(name='master.au', freq=0, dur=playList[len(playList)-1][0][1], vol=0.2)
	masterSong = AudioSegment.from_file("master.au", "au")
	for item in playList:
		#obten la longitudDelSegmento
		longitudDelSegmento = int(item[0][1]) - int(item[0][0])
		#obten Si se loopea 
		loops = item[2]
		#crea los sonidos de esta seccion
		sonidoNum = 1 #integra un contador para los sonidos
		#crea un sonido temporal que contendra toda esta seccion
		au_file(name="instrumento.au", freq=0, dur=longitudDelSegmento, vol=1)
		
		for itemSonido in item[1]:
			nombre = 'sound' + str(sonidoNum) +".au"
			#print(nombre,itemSonido[2],itemSonido[1], float(itemSonido[0]))
			au_file(name=nombre, freq=int(itemSonido[2]), dur=int(itemSonido[1]), vol=float(itemSonido[0]))
			sonidoNum += 1
		instrumento = AudioSegment.from_file("instrumento.au", "au")
		
		
		
		for i in range(1, sonidoNum):
			nombre = 'sound' + str(i) +".au"
			#abreElArchivo
			temp = AudioSegment.from_file(nombre, "au")
			#insertaloEnElinstrumento
			instrumento =  instrumento.overlay(temp, position=0, loop=loops)
		#concatenaElInstrumento
		instrumento = instrumento[:longitudDelSegmento]
		
		#sobrelapa los sonidos en master
		masterSong = masterSong.overlay(instrumento, position=int(item[0][0]))
	#final = masterSong*2
	masterSong.export("testingSong.emepetres", format="mp3")