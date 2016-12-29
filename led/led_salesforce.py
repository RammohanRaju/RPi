import RPi.GPIO as GPIO
from simple_salesforce import Salesforce
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(7, GPIO.OUT)

print ">> The Program Is Trying To Login Into Salesforce.com. Please Wait..."

username='USERNAME'
password='PASSWORD'
security_token='SALESFORCE_SECURITY_TOKEN'

sf = Salesforce(username=username, password=password, security_token=security_token)

try:
    while True:
        toggle = sf.query("SELECT Toggle__c FROM Raspi_ctrl__c WHERE Name='N-0002'")
        records=toggle["records"]
        temp = records[0]
        state = temp["Toggle__c"]
        print(state)
        if state == "1":
            print("Turning LED on..")
            GPIO.output(7, 1)          # set GPIO7 to 1/GPIO.HIGH/True
            sleep(0.5)                   # wait a second
        elif state == '0':
            print("Turning LED off..")
            GPIO.output(7, 0)          # set GPIO7 to 0/GPIO.LOW/False
            sleep(0.5)                   # wait a second
        else:
            print("Unknown state.. turning LED off")
            GPIO.output(7, 0)          # set GPIO7 to 0/GPIO.LOW/False
            sleep(0.5)                   # wait a second

except KeyboardInterrupt:          # trap a CTRL+C keyboard interrupt
    GPIO.cleanup()                 # resets all GPIO ports used by this program