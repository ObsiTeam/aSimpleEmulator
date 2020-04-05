import serial
from PyUserInput.pymouse import PyMouse
from PyUserInput.pykeyboard import PyKeyboard
import os
m = PyMouse()
k = PyKeyboard()
x_dim, y_dim = m.screen_size()
data = serial.Serial('COM10', 9600)
cul = []
left = []
right = []
os.system("cls")
while True:
	rag = data.read()
	rag = str(rag)
	if rag == "b'/'":
		cul = str(cul)
		cul = cul.replace('["', "")
		cul = cul.replace("", "b'\\\\n'")
		cul = cul.replace('", "', ",")
		cul = cul.replace("\\", "")
		cul = cul.replace("b", "")
		cul = cul.replace("n", "")
		cul = cul.replace("'", "")
		cul = cul.replace("'", "")
		cul = cul.replace("'", "")
		cul = cul.replace("'", "")
		cul = cul.replace("'", "")
		cul = cul.replace("'", "")
		cul = cul.replace("'", "")
		cul = cul.replace("'", "")
		cul = cul.replace("'", "")
		cul = cul.replace("'", "")
		cul = cul.replace("'", "")
		cul = cul.replace("'", "")
		cul = cul.replace('"', "")
		cul = cul.replace('"', "")
		cul = cul.replace('"', "")
		cul = cul.replace('"', "")
		cul = cul.replace(",", "")
		cul = cul.replace(" ", "")
		cul = cul.replace("]", "")
		rawdata = str(cul)
		print (rawdata)
		ix = rawdata.split("aX=")
		ix = str(ix[1])
		ix = ix.split("|")
		ix = str(ix[0])
#		print ("iX = "+ix)

		iy = rawdata.split("aY=")
		iy = str(iy[1])
		iy = iy.split("|")
		iy = str(iy[0])
#		print ("iY = "+iy)

		iz = rawdata.split("aZ=")
		iz = str(iz[1])
		iz = iz.split("|")
		iz = str(iz[0])
#		print ("iZ = "+iz)

		gx = rawdata.split("gX=")
		gx = str(gx[1])
		gx = gx.split("|")
		gx = str(gx[0])
#		print ("gX = "+gx)

		gy = rawdata.split("gY=")
		gy = str(gy[1])
		gy = gy.split("|")
		gy = str(gy[0])
#		print ("gY = "+gy)

		gz = rawdata.split("gZ=")
		gz = str(gz[1])
		gz = gz.split("|")
		gz = str(gz[0])
#		print ("gZ = "+gz)

		cd = rawdata.split("cd=")
		cd = str(cd[1]) #0
		cd = cd.split("|")
		cd = str(cd[0])
#		print ("cd = "+cd)

		ci = rawdata.split("ci=")
		ci = str(ci[1]) #1
		ci = ci.split("|")
		ci = str(ci[0])
#		print ("ci = "+ci)

		coords = m.position()
		xcord = coords[0]
		ycord = coords[1]

		useless = """
		right.append(cd)
		print (right)
		try:
			if str(right[0])== "1":
				if str(right[1]) == "1":
					if str(right[2]) == "1":
						if str(right[3]) == "1":
							if str(right[4]) == "1":
								m.click(xcord, ycord)
								right = []
							else:
								right = []
						else:
							right = []
					else:
						right = []
				else:
					right = []
			else:
				right = []
		except:
			pass"""

		if int(iy) < -6000:
			giro = "Izquierda"
			xcord = int(xcord) -70
			m.move(int(xcord),int(ycord))
		elif int(iy) > 2500:
			giro = "Derecha"
			xcord = int(xcord) +70
			m.move(int(xcord),int(ycord))
		else:
			giro = "Neutro"

		if int(ix) < -12000:
			estado = "Norte"
			k.press_key('w') #Delante
		elif int(ix) > 0:
			estado = "Sur"
			k.press_key('s') #Detras
		else: 
			estado = "Central"
			k.release_key('w') #Delante
			k.release_key('s') #Detras

		#print (ix+" / "+iy+" / "+iz)


		gx = int(gx)
		gx = int(gx)/100
		gx = int(gx)

		gy = int(gy)
		gy = int(gy)/100
		gy = int(gy)

		gz = int(gz)
		gz = int(gz)/100
		gz = int(gz)


		#print (str(gx)+" / "+str(gy)+" / "+str(gz))
		print (">> "+str(estado)+" // "+str(giro)+" // "+str(cd)+" "+str(ci))

		print ("==========================================")
		cul = []
	else:
		cul.append(rag)
