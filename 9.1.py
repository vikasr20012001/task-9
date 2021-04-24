import os
import speech_recognition as sr
import webbrowser as wb
import pyttsx3

os.system("tput setaf 2")
print()
print("Welcome to the Menu")
pyttsx3.speak("Welcome to the menu")
os.system("tput setaf 6")
print()
print("")
os.system("tput setaf 5")
while(True):
	print("\t\t Menu")
	print("""
	\t\t Hadoop
	\t\t Docker
	\t\t Linux
	\t\t Exit
	""")
	os.system("tput setaf 1")
	r=sr.Recognizer()
	with sr.Microphone() as source:
		os.system("tput setaf 6")
		print("Start Saying")
		pyttsx3.speak("start saying")
		audio = r.listen(source)
		print("I got it , plz wait....")
		pyttsx3.speak("I got it , please wait")

	choice = r.recognize_google(audio)
	print(choice)
	choice=choice.lower()
	os.system("tput setaf 3")
	if choice=="hadoop":
		while(True==1):
			print("""
			\n
		  ********************Welcome to Hadoop World**************************
		\n
			\t\tsay To configure the Namenode
			\t\tsay To configure the Datanode
			\t\tsay To configure the Client
			\t\tsay To exit to main menu
			""")
			os.system("tput setaf 6")
			with sr.Microphone() as source:
				os.system("tput setaf 6")
				print("Start Saying")
				pyttsx3.speak("start saying")
				audio = r.listen(source)
				print("I got it , plz wait....")
				pyttsx3.speak("I got it , please wait")

			choice1a = r.recognize_google(audio)
			print(choice1a)
			choice1a=choice1a.lower()
			os.system("tput setaf 7")
			
			os.system("tput setaf 1")
			os.system("tput setaf 5")
			if choice1a==("configure" and "namenode"):
				os.system("tput setaf 3")
				os.system("tput setaf 1")
				print("""
				\n
				\t\tsay 1 :To configure the Hdfs-site file
				\t\tsay 2 :To configure the Core-site file
				\t\tsay 3 :To Format the namenode
				\t\tsay 4 :To start the service of namenode
				\t\tsay 5 :To see the status of namenode
				\t\tsay 6 :To see the report of the hadoop cluster
				""")
				with sr.Microphone() as source:
					os.system("tput setaf 6")
					print("Start Saying")
					pyttsx3.speak("start saying")
					audio = r.listen(source)
					print("I got it , plz wait....")
					pyttsx3.speak("I got it , please wait")

				choice1 = r.recognize_google(audio)
				print(choice1)
				choice1=choice1.lower()
				os.system("tput setaf 3")
				ip= input("Enter IP of Namenode at which you want to configure :")
				if choice1==("configure" and "hdfs"):
					
					os.system("scp namenode_hdfs_site.py root@{}:/root/".format(ip))
					os.system("ssh root@{} python3 namenode_hdfs_site.py".format(ip))
				elif choice1==("configure" and "core"):
				
					os.system("scp namenode_core_site.py root@{}:/root/".format(ip))
					os.system("ssh root@{} python3 namenode_core_site.py".format(ip))
				elif choice1==("format"):
					
					os.system("ssh root@{} hadoop namenode -format".format(ip))
				elif choice1==("start" and "namenode"):
					
					os.system("ssh root@{} hadoop-daemon.sh start namenode".format(ip))
				elif choice1==("status" and "namenode"):
					
					os.system("ssh root@{} jps".format(ip))
				elif choice1==("report"):
					
					os.system("ssh root@{} hadoop dfsadmin -report".format(ip))
				else:
					print("Say correct input")
					pyttsx3.speak("Say correct input")
				
			elif choice1a==("configure" and "datanode"):
				os.system("tput setaf 4")
				os.system("tput setaf 5")
				print("""
				\n
				\t\tsay 1 :To configure the Hdfs-site file
				\t\tsay 2 :To configure the Core-site file
				\t\tsay 3 :To start the service of datanode
				\t\tsay 4 :To see the status of datanode
				\t\tsay 5 :To see the report of the hadoop cluster	
				""")
				with sr.Microphone() as source:
					os.system("tput setaf 6")
					print("Start Saying")
					pyttsx3.speak("start saying")
					audio = r.listen(source)
					print("I got it , plz wait....")
					pyttsx3.speak("I got it , please wait")

				choice2 = r.recognize_google(audio)
				print(choice2)
				choice2=choice2.lower()
				os.system("tput setaf 7")
				ip= input("Enter IP of Datanode at which you want to configure :")
				if choice2==("configure" and "hdfs"):
					
					os.system("scp datanode_hdfs_site.py root@{}:/root/".format(ip))
					os.system("ssh root@{} python3 datanode_hdfs_site.py".format(ip))
				elif choice2==("configure" and "core"):
					
					os.system("scp datanode_core_site.py root@{}:/root/".format(ip))
					os.system("ssh root@{} python3 datanode_core_site.py".format(ip))
				elif choice2==("start" and "datanode"):
					
					os.system("ssh root@{} hadoop-daemon.sh start datanode".format(ip))
				elif choice2==("status" and "datanode"):
					
					os.system("ssh root@{} jps".format(ip))
				elif choice2==("report"):
					
					os.system("ssh root@{} hadoop dfsadmin -report".format(ip))
				else:
					print("please say correct input")
					pyttsx3.speak("Say correct input")
			elif choice1a==("configure" and "client"):
				os.system("tput setaf 1")
				os.system("tput setaf 2")
				print("""
				\n
				\t\tsay 1 :To configure the Hdfs-site file
				\t\tsay 2 :To configure the Core-site file
				""")
				with sr.Microphone() as source:
					os.system("tput setaf 6")
					print("Start Saying")
					pyttsx3.speak("start saying")
					audio = r.listen(source)
					print("I got it , plz wait....")
					pyttsx3.speak("I got it , please wait")

				choice3 = r.recognize_google(audio)
				print(choice3)
				choice3=choice3.lower()
				os.system("tput setaf 5")
				if choice3==("configure" and "hdfs"):
					ip= input("Enter IP of Client  which you want to configure :")
					os.system("scp client_hdfs_site.py root@{}:/root/".format(ip))
					os.system("ssh root@{} python3 client_hdfs_site.py".format(ip))
				elif choice3==("configure" and "core"):
					ip= input("Enter IP of client at which you want to configure :")
					os.system("scp client_core_site.py root@{}:/root/".format(ip))
					os.system("ssh root@{} python3 client_core_site.py".format(ip))
				else:
					print("please say correct input")
					pyttsx3.speak("Say correct input")
			elif choice1a==("exit"):
				break        
			else:
				print("please say correct input")
				pyttsx3.speak("Say correct input")

	elif choice==("docker" or "Docker"):
		while(True):
			os.system("tput setaf 4")
			print("""
	****************Welcome to Docker World**************************
			[0]Display Docker Version
			[1]Displaying Docker Images
			[2]Pull Docker Images
			[3]Display Docker Launched Containers
			[4]Launch a New Containers
			[5]Start a launched container
			[6]Attach started Container
			[7]Check Docker status
			[8]Removing a Container
			[9]Removing all containers
			[10]Removing a Image
			[11]Display Running containers
			[12]Stopping running container
			[13]To exit to main menu
			""")
			with sr.Microphone() as source:
				os.system("tput setaf 6")
				print("Start Saying")
				pyttsx3.speak("start saying")
				audio = r.listen(source)
				print("I got it , plz wait....")
				pyttsx3.speak("I got it , please wait")

			docker_input = r.recognize_google(audio)
			print(docker_input)
			docker_input=docker_input.lower()
			os.system("tput setaf 3")
			if (docker_input=="version" ):
				os.system("docker --version")
			elif (docker_input==("images" and "docker")):
				os.system("docker images")
			elif (docker_input==("pull" and "image" )):
				image=input("Enter image name u want to pull=")
				os.system("docker pull {}".format(image))
			elif (docker_input=="launched" and "container"):
				os.system("docker ps -a")
			elif (docker_input=="launched" and "new" and "container"):
				name=input("Enter name to launch container=")
				image=input("Enter name of Image u want to launch container=")
				os.system("docker run -it --name {} {}".format(name,image))
			elif (docker_input=="start" and "launched" and "container"):
				name=input("Enter name launhced container u want to start=")
				os.system("docker start {}".format(name))
			elif (docker_input==("attach" and "container")):
				name=input("Enter name of started container u want to attach=")
				os.system("docker attach {}".format(name))
			elif (docker_input==("status")):
				os.system("systemctl status docker")
			elif (docker_input==("remove" and "container")):
				name=input("Enter name of container u want to remove=")
				os.system("docker rm -f {}".format(name))
			elif (docker_input==("launched" and "all" and "containers")):
				os.system("docker rm -f $(docker ps -qa)")
			elif (docker_input==("remove" and "image")):
				image=input("Enter image name u want to remove=")
				os.system("docker rmi -f {}".format(image))
			elif (docker_input==("running" and "container")):
				os.system("docker ps")
			elif (docker_input==("stop" and "container")):
				name=input("Enter name of container u want to stop=")
				os.system("docker stop {}".format(name))
			elif (docker_input=="exit"):
				break
			else:
				print("Invalid Input")
				pyttsx3.speak("Say correct input")
	elif choice==("linux" or "Linux"):
		while(True):
			os.system("tput setaf 4")
			print("""
	****************Welcome to Linux World**************************
			[0]User
			[1]Present Directory
			[2]Date
			[3]calender
			[4]Ifconfig
			[5]Firefox
			[6]Chrome
			[7]To exit to main menu
			""")	
			with sr.Microphone() as source:
				os.system("tput setaf 6")
				print("Start Saying")
				pyttsx3.speak("start saying")
				audio = r.listen(source)
				print("I got it , plz wait....")
				pyttsx3.speak("I got it , please wait")

			l_input = r.recognize_google(audio)
			print(l_input)
			l_input=l_input.lower()
			os.system("tput setaf 3")
			if (l_input=="user"):
				os.system("whoami")
			elif (l_input=="present"):
				os.system("pwd")
			elif (l_input=="date"):
				os.system("date")
			elif (l_input=="calender"):
				os.system("cal")
			elif (l_input=="ifconfig"):
				os.system("ifconfig")
			elif (l_input=="firefox"):
				os.system("firefox")
			elif (l_input=="chrome"):
				os.system("google-chrome")
			elif (l_input=="exit"):
				break
			else:
				print("Invalid Input")
				pyttsx3.speak("Say correct input")
	elif choice==("exit" or "Exit"):
		print("""
		***Thank you***
		With regards....,
		Navaneeswar Reddy Challa
		Satish Reddy Medapati
		""")
		pyttsx3.speak("Thank you")
		pyttsx3.speak("With regards")
		pyttsx3.speak("Navaneeswar reddy challa")
		pyttsx3.speak("satish reddy medapati")
		break
	else:
		print("Invalid Input")
