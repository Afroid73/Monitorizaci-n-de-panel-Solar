
import redis 
import time
import serial

 
r = redis.Redis(
    host ='redis-15970.c276.us-east-1-2.ec2.cloud.redislabs.com',
    port=15970,
    password='vwmqP05QaR0yMFsIU8OSVMbSX7JQGomi')


uc = serial.Serial("/dev/ttyACM1", baudrate=9600,timeout=5.0)

ts=r.ts()

while True:
    
    val_bytes = uc.readline() 

# Convertir la cadena de bytes a cadena de caracteres
    val = val_bytes.decode()
# Dividir la cadena utilizando la coma como separador y asignar cada parte a variables separadas
    volt1, volt2, temp = val.split(",")
    
    print(val)
# Imprimir las partes separadas
    print(volt1)
    print(volt2)
    print(temp)
    
    r.set('volt1',volt1) #Formato String
    ts.add("Volt1",'*',volt1) #Formato Ts - Time Series
    r.set('volt2',volt2)
    ts.add("Volt2",'*',volt2)
    r.set('temp',temp)
    ts.add("Temp",'*',temp)
    time.sleep(2)

#uc.close()

