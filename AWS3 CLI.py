import json
import os
import subprocess as sp
import speech_recognition as rs
import pyttsx3

def createKey(name):
    p=f"aws ec2 create-key-pair --key-name {name} > C:\\Users\\alfo7\\Desktop\\key.json"
    found=sp.getstatusoutput(p)
    if found[0]==0:
        return "Made key Successfully!"
    else:
        return "failed to create!!!"

def getKey():
    with open(r'C:\Users\alfo7\Desktop\key.json') as f:
        keypair=json.load(f)
    return keypair["KeyName"]

def createSecG(sgname):
    des="Personelsecuritygroup"
    p=f"aws ec2 create-security-group --group-name {sgname} --description {des} > C:\\Users\\alfo7\\Desktop\\sGroup.json"
    run=sp.getstatusoutput(p)
    if run[0]==0:
        return f" Security Key Generated with Security group : {sgname}"
    else:
        print("Error:",run[1])
        return f"Failed to create Security group as {sgname}"

def getSGroup():
    with open(r'C:\Users\alfo7\Desktop\sGroup.json') as f:
        groupid=json.load(f)
    return groupid["GroupId"]  

def createVolume():
    p="aws ec2 create-volume --availability-zone ap-south-1b --volume-type gp2 --size 1 --tag-specifications ResourceType=volume,Tags=[{Key=Name,Value=cliVolume}] >C:\\Users\\alfo7\\Desktop\\cliVolume.json"
    run=sp.getstatusoutput(p)
    if run[0]==0:
        return "Volume Created"
    else:
        print("Error:",run[1])
        return "Failed to create Volume"

def getvolId():
    with open(r'C:\Users\alfo7\Desktop\cliVolume.json') as f:
        volId=json.load(f)
    return volId["VolumeId"]
def AttachVol():
    vol=getvolId()
    instanceId=getInstanceId()
    p=f"aws ec2 attach-volume --volume-id {vol} --instance-id {instanceId} --device /dev/sdf"
    run=sp.getstatusoutput(p)
    if run[0]==0:
        return("Volume Attached to ur Instance")
    else:
        return("Failed to attach Volume")    
def launchAWS():
    p=f"aws ec2 run-instances --image-id ami-0e306788ff2473ccb --instance-type t2.micro --count 1 --subnet-id subnet-ebec93a7 --security-group-ids {getSGroup()} --key-name {getKey()} > C:\\Users\\alfo7\\Desktop\\awsInstance.json"
    run=sp.getstatusoutput(p)
    if run[0]==0:
        return " Instance launched"
    else:
        print("Error:",run[1])
        return "Failed to Launch"

def getInstanceId():
    with open(r'C:\Users\alfo7\Desktop\awsInstance.json') as f:
        InstId=json.load(f)
        iID=InstId["Instances"]
    return iID[0]["InstanceId"]

print("I can Perform this tasks")
print("\n 1.Create key \t 2.create a New Security Group \t 3.Create volume \t 4.Attach volume \t 5.Launch Instance")
r=rs.Recognizer()
print("\nOut of this Above Option speak what you want me to do for You")
while True:
    key=0
    guard=0
    with rs.Microphone() as source:
    	print("Said :",end="")
    	data=r.listen(source)
    try:
        text=(r.recognize_google(data)).lower()
    except Exception as e:
        pyttsx3.speak("Please speak loud,Can't hear your voice")
        print("Please speak loud")
        continue
    print("\t",text)   
    if ("key" in text or "key pair " in text) and ("run" in text or "launch" in text or "create" in text):
        pyttsx3.speak("Enter key name")
        keypas=input("Enter key name:")
        print(createKey(keypas))
        key=getKey()
    elif ("security" in text or "security group" in text) and ("run" in text or "launch" in text or "create" in text):
        pyttsx3.speak("Enter security guard name")
        sguard=input("Enter security guard name:")
        print(createSecG(sguard))
        guard=getSGroup()
    elif ("disk" in text or "pendrive" in text or "volume" in text) and ("create" in text or "make" in text):
        p=createVolume()
        pyttsx3.speak(p)
        print(p)   
    elif ("instance" in text or "os" in text or "operating system" in text) and ("run" in text or "launch" in text):
        p=launchAWS()
        pyttsx3.speak(p)
        print(p)
    elif ("disk" in text or "pendrive" in text or "volume" in text) and ("attach" in text or "mount" in text or "insert" in text):
        p=AttachVol()
        pyttsx3.speak(p)
        print(p)    
    elif "exit" in text:
        pyttsx3.speak("Exiting the Program....")
        exit()
   
    check=input("\nWant to continue with more Task? (y/N)")
    if check=="y":
        continue
    else:
        exit()