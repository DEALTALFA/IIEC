#!/usr/bin/python3


print("Content-Type:text/html")
print()



import cgi

import subprocess as sp

form=cgi.FieldStorage()

cmd=form.getvalue("pgm")

ostype=form.getvalue("ostype")

if cmd!="docker":

 if cmd=="firefox":   

  runned=sp.getstatusoutput("export DISPLAY=:0;setenforce 0;sudo "+cmd)
  if runned[0]==0:
    print("runned")
  else:
    print(runned[1]) 	
 else:

   runned=sp.getstatusoutput(cmd)

   print("entered else")

   status=runned[0]

   output=runned[1]

   if status==0:

    print("command runned and O/P is:{}".format(output))

   else:

    print("some error occurred:{}".format(output))

else:

 print("An OS is being lauched with the help of docker in ur linux system")

 print("it will launch if u have::")

 runned=sp.getstatusoutput("sudo docker run -itd {}".format(ostype))
 if runned[0]==0:
  print("runned ur docker in ur linux system")
 else:
  print("failed to run due To :{}".format(runned[1])) 


