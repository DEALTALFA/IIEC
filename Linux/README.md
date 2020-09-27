   # Docker
   Thanks to the kernel hacker that implemented *namespacing kernel* for linux.What it means in techincal language is that a set of processes only see a set of resources. now in layman language we can say that we can isolate the processes from other process .like isolating the file system,network interface and memory the whole thing .
   
   *to install docker in Redhat* 
   you type 
    
    curl -sSL https://get.docker.com | sh
   
   `yum install docker-ce` 
   
   it will give error bcz community edition docker for Rhel is not available(Except for Enteprise Edition which is paid)
   ## So we need to trick the system  .
   **Step 1**: Go to browser and search for [docker rpm download](https://www.google.com/search?q=docker+rpm+download&rlz=1C1CHBD_enIN907IN907&oq=docker&aqs=chrome.0.69i59l2j35i39j0l2j69i61l2j69i60.1427j0j7&sourceid=chrome&ie=UTF-8).
   
   **Step2**:Follow the first link of docker.download.But to need to go to this parent folder where packages and repodata is there
   
   **Step3**:copy the url of it and make a repo file in /etc/yum.repos.d/ and paste it there 
   
   ```
   [docker]
   name=yum for docker
   baseurl=https://download.docker.com/linux/centos/7/x86_64/stable/
   gpgcheck=0    
   
   ```
## Docker installation
In terminal run `yum install docker-ce --nobest` to install docker in ur system
Once installed run docker with **systemctl start docker** for permanent *enable* the docker,replace with start

For every OS we need image file.here in docker files are know as docker images with less than 200mb in size 
.Go to site [Docker Hub](https://hub.docker.com/) to download some images for your docker.like ubuntu ,centos etc
to download images get back to terminal and write `docker pull <osname>:<ver>`.eg: docker pull ubuntu:14.04 by default if ver  is not mention than it download the latest one.
 
## Docker commands
`docker container ls`or `docker images`to see available images in ur system
`docker container run -i -t ubuntu:14.04` 

-i=interactive -t=terminal  to start a new container with a random name u can also specify name by _--name_(its like a tag) before       osname like `docker container -i -t --name myos ubuntu:14.04` type exit inside container to get out to your orginial terminal
 
`docker rm tag` to delete  a particular container but if we had open to many container we cannot keep writing the same command again and again so we write
`docker rm $(docker container ls -q -a)` to delete all the container lauched till know $(docker container ls -q -a) gives o/p of every tag ever lauched.
but this code will fail for the process which are in running state. so we add `-f` after rm to forcely delete the container
`docker rm -f $(docker conatiner ls -q -a)`
`docker rmi imagename` to delete the image file 
`docker container run -it --rm centos date ` it create a os run date commamd and then also delete the history of os that it was ever made

 
### If facing connectivity or yum issues in Docker.
U need to make port 80 and 443 public access by any program
Http & https work on port 80 & 443.
Normally, these ports aren't public that means they are under control of rhel and any foreign program can't access them.
That's why U have enabled these ports to public access

To know which port are public
>firewall-cmd --list-all

If u know about zones, u can get all active zones by -
firewall-cmd --get-active-zones

Note - These cmds need to be run in RHEL vm & not in any Docker containers

1) `firewall-cmd  --zone=public --add-masquerade --permanent`            //to make changes permanent

2) `firewall-cmd  --zone=public --add-port=80/tcp`                     //made 80 public


3) `firewall-cmd  --zone=public --add-port=443/tcp`                    //made 443 public

4) `firewall-cmd  --reload`

5) `systemctl restart docker`

## Installation of s/w in container
  bydefault some application are installed while other are not so u can do is that. open a new tab in the terminal
* bychance if there is no ifconfig(a free utility for non-interactive download of files from the Web)go in ur rhel terminal and type `which ifconfig`
* copy that path in `rpm -qf <path>` to know the name of that provider.
* now get in ur container and type `yum install <providername>` eg
> yum install net-tools

## Some tricks
* To get out of conatiner we always have to exit from the container which result in closing of container.
>ctrl+P+Q 

u will be in ur base RedHat System and your OS is also keep on running 
to go in back `docker container attach osname` or `docker attach osname` but soon this may get deprecated 
* To run OS for only till the program runs
`docker container run -it --name os1 centos:7 <program>`  eg:-  
>docker container run -it --name os1 centos:7 date    

it launch new os,boot the os,run the date command inside this os,gives o/p and then OS stops. it ran in that os not the base rhel
u can see check the history of container there u will find that recently one container was open and closed ina short duration of time
and If u want to *remove the container history or say remove the OS of that file* then add *--rm* after u give the osname

* Creating personal image

syntax= `docker commit <osname> <newname>:<version>`

`docker commit os1 mynev:v1`         

everything installed in this docker image will be already setup for next use

* To know about the container  info like ip address without installing net-tools(provider)

`docker container inspect`

## Start services

* **apache server(httpd)**

Install httpd in container when trying to start httpd u will have error
>operation not supported
many people thing that it doesn't support but it support,but  bydefault it don't allow

![image](https://user-images.githubusercontent.com/60976631/93016144-a9498780-f5dc-11ea-9d6d-fbfa0da38d29.png)

Behind this systemctl command behind it runs a program  

![image](https://user-images.githubusercontent.com/60976631/93016223-3391eb80-f5dd-11ea-9229-e0e468e6edbf.png)

internally they are loading this file

![image](https://user-images.githubusercontent.com/60976631/93016256-8370b280-f5dd-11ea-9382-9539c37cd420.png)

get inside that service using vim.when u are starting the services with systemctl start httpd .when ur exceuting this service they run this command internally 

![image](https://user-images.githubusercontent.com/60976631/93016300-d3e81000-f5dd-11ea-91de-a474ccaa0d4d.png)

this means u can run the service with that command too. when u type `which httpd` it also has the same path.

![image](https://user-images.githubusercontent.com/60976631/93016478-1b22d080-f5df-11ea-8496-e7a936109a3a.png)

u can start the httpd with both the command **systemctl start httpd** aswell as with **usr/sbin/httpd**

![image](https://user-images.githubusercontent.com/60976631/93016038-d3e71080-f5db-11ea-8508-eb995a867267.png)

u will see the server started

Now u can do the same thing with docker to run httpd server `/usr/sbin/httpd` u server wil  satart running.now u can do things whatever u want
