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
    print("File %s written" % name)
# test the module 17 posiciones de 275 a 2740 saltos de 145
# test the module 17 posiciones de 300 a 1100 saltos de 50
au_file(name='sound440.au', freq=300, dur=3000, vol=1.0)
au_file(name='sound490.au', freq=700, dur=3000, vol=1.0)
au_file(name='sound940.au', freq=1100, dur=3000, vol=1.0)
# print("Waiting a little")
song1 = AudioSegment.from_file("sound440.au", "au")
song2 = AudioSegment.from_file("sound490.au", "au")
song3 = AudioSegment.from_file("sound940.au", "au")
lastSecond = song1[:1000]
lastSecond = lastSecond - 3
withStyle = lastSecond * 3
withStyle = withStyle.fade_in(1000).fade_out(1000)
withStyle = withStyle.append(song2)
withStyle = withStyle.append(song3, crossfade=2000)
output = withStyle.overlay(withStyle, position=5000, loop=True)
output2 = song1.append(song2)
output2 = output2.append(song3)
output2.export("testingSong.emepetres", format="mp3")
# song2 = AudioSegment.from_wav("sound490.acoustaticSoundByte")
# song3 = AudioSegment.from_wav("sound940.acoustaticSoundByte")

#creacion de la estructura de datos provisional, tendremos que sacarla de archivo y sera de flojera
playList = []

parteUno = []
parteDos = []
parteTres = []
parteUno.append((1,1000,700))
parteUno.append((1,1000,705))
parteUno.append((1,1000,695))

parteDos.append((1,2000,800))
parteDos.append((1,2000,805))
parteDos.append((1,2000,795))

parteTres.append((.5,1000,650))
parteTres.append((.5,1000,655))
parteTres.append((.8,1000,645))

playList.append(((0,1000),parteUno,False))
playList.append(((1000,1800),parteDos,True))
playList.append(((1800,2800),parteTres,False))
pp.pprint(playList)
print(playList[len(playList)-1][0][1])

#crear el sonido maestro
au_file(name='master.au', freq=0, dur=playList[len(playList)-1][0][1], vol=0.2)
masterSong = AudioSegment.from_file("master.au", "au")
for item in playList:
	print(item)
	#obten la longitudDelSegmento
	longitudDelSegmento = int(item[0][1]) - int(item[0][0])
	#obten Si se loopea 
	loops = item[2]
	#crea los sonidos de esta seccion
	sonidoNum = 1 #integra un contador para los sonidos
	#crea un sonido temporal que contendra toda esta seccion
	au_file(name="instrumento.au", freq=0, dur=longitudDelSegmento, vol=1)
	
	contadorSonido = 0
	for itemSonido in item[1]:
		nombre = 'sound' + str(sonidoNum) +".au"
		print(nombre,itemSonido[2],itemSonido[1], float(itemSonido[0]))
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
print("Termine")