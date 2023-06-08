import redis 
import time

r = redis.Redis(
    host ='redis-15970.c276.us-east-1-2.ec2.cloud.redislabs.com',
    port=15970,
    password='vwmqP05QaR0yMFsIU8OSVMbSX7JQGomi')

ts = r.ts()
#ts.create("Sens2")

for i in range(100):
    ts.add("flujo", "*",i)
    time.sleep(1)
    