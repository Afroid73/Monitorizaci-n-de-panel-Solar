import serial

arduino_port ="COM3"
baud = 9600
fileName = "Sensor-data.csv"
samples =5
line = 0
print_labels=False

ser = serial.Serial(arduino_port,baud)
print("Connectado al puerto:" + arduino_port)
file = open(fileName, "a")
print("Archivo Creado")


while line <= samples:
    if print_labels:
        if line==0:
            print("imprimiendo")
        else:
            print("linea" + str(line)+"Escribiendo...")
    getData=str(ser.readline())
    data=getData[2:][:-5]      #[2:] primeros caracteres son eliminados
                               #[:-5] 5 Ultimos caracteres son eliminados
    print(data)
    
    file=open(fileName,"a")
    file.write(data +"\n")
    line=line+1
print("recolección de datos terminada")        