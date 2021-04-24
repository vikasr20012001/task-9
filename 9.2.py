
## TASK 9.2
## Create a Web Menu Using Python-CGI and API



## Python - CGI Programming

## In the early days of World Wide Web (WWW), the web server used to serve only the static contents of web pages stored in document root folder of its local file system. Common Gateway Interface (CGI), one of the first and still popular technique by which a dynamic content can be rendered to client computer's web browser software.

## Common Gateway Interface (CGI) is a standard protocol for web servers to render output of console applications (also called command-line interface programs) in the form of dynamically generated web pages. Such programs are known as CGI scripts.

## The CGI script can be a Python Script, PERL Script, Shell Script, C or C++ program, etc. In this chapter we shall try to understand how a Python script can be used as CGI script and how it is executed on a web server.

## There are many web server products available. The most popular ones are Apache, IIS, nginx etc. CGI can be enabled on all these web server softwares. The examples in this chapter are based on WAMP which is a precompiled bundle of Apache web server, MySQL and PHP modules for use with Windows operating system. The WAMP installer can be downloaded

## Apache Configuration
## In order to enable CGI support on WAMP web server, certain modifications should be done to its configuration file 'httpd.conf' which is found in the 'conf' folder under Apache's installation folder. For example:

## C:\wamp64\bin\apache\apache2.4.35\conf\httpd.conf.

## First of all, ensure that httpd.conf grants permission to execute scripts in cgi-bin folder by adding following lines. Look for following block in the file:
```
<Directory "${INSTALL_DIR}/cgi-bin">
AllowOverride None
   Options None
   Require all granted
</Directory>

```
## Comment out above block and paste following lines below it:
```
<Directory "${INSTALL_DIR}/cgi-bin">
AllowOverride None
   Options ExecCGI
   Order allow,deny
   Allow from all
</Directory>```
## Secondly, locate following commented line in the file:

#AddHandlercgi-script .cgi
##Uncomment it and also add following line to let the server treat '*.py' file in 'cgi-bin' as CGI script.

##AddHandlercgi-script .cgi
##AddHandlercgi-script .py
##Hello World CGI script
##After getting configuration of Apache server according to above explanation, we now write first Python CGI script.

##First line in the '.py' file should have a shebang syntax. It actually is a commented line containing path to Python executable. This will let the server know that the mentioned executable is responsible for running the rest of the script. For example:

#!c:\python37\python.exe
##Next is the CGI header indicating the content type. It should be separated with rest of script with a blank line initiated by '\n'.

print ("Content-type:text/html\r\n\r\n")
##Subsequent part of the script renders HTML to the client browser through Python's print() statements.

print ("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Hello World - First CGI Program</title>")
print("</head>")
print("<body>")
print("</body>")
print ("</html>")
##Save following script as 'hello.py' in 'cgi-bin' directory under server's installation folder.

#!c:\python37\python.exe
print ("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Hello World - First CGI Program</title>")
print("</head>")
print("<body>")
print("</body>")
print ("</html>")
##Start WAMP server and enter following URL in web browser's address bar:

##http://localhost/cgi-bin/hello.py
##A nice Hello World message is displayed in the browser.

##CGI support modules
##Python's standard library consists of two module for CGI support. The cgi module defines number of utilities to be used by Python CGI script. The cgitb module is a traceback manager for CGI scripts. Normally both modules are imported in a Python script, enabling the traceback feature.

import cgi, cgitb
cgitb.enable()
##The client browser interacts with the web server using HTTP protocol. HTTP requests are sent to a server URL via either get or post methods. The get method sends the data from client in an unencrypted form, hence it is considered to be unsafe. The post method is normally used to send data in HTML form of the client. The HTTP header contains encrypted data of form.

##The cgi module defines a FieldStorage class. The data received from client request is collected in FieldStorage object. This is similar to Python's dictionary object consisting of form elements and their respective values. Once the form data is retrieved by FieldStorage object on server side, the Python script can perform required process and render HTML output back to the client browser.

#FieldStorage attributes:
#name	The field name  
#filename	Client side filename.
#value	The value as a string. For file uploads, reads the file and returns bytes
#file	The file(-like) object from which you can read the data as bytes
#type	The content-type
#headers	A dictionary(-like) object containing all headers
#FieldStorage methods:
#getfirst()	Return the first value received.
#getlist()	Return list of received values.
#getvalue()	Dictionary style get() method.
#keys()	Dictionary style keys() method.
#make_file()	Return a readable & writable file.
#HTML form 
#Let us now design a simple HTML form and send data entered by user in its elements to a Python script stored in cgi-bin directory on server.

#Following HTML produces a web page with a text box element, a group of two radio buttons, a dropdown element with two options and a TextArea element. The form’s 'action' attribute is set to 'htmlform.py' script which we shall put in cgi-bin folder. Form's method attribute is set to 'post'.

#Save following script as 'cgiform.html' in 'www' folder of WAMP's installation directory.
```
<html>
<body>
<form action="/cgi-bin/htmlform.py"  method="post"target="_blank">
Name : <input type="text" name="name"/></br>
Faculty : <input type = "radio" name = "faculty" value = "Arts" /> Arts
<input type = "radio" name = "faculty" value = "Commerce" /> Commerce</br>
Batch : <select name = "batch">
<option value = "Morning" selected>Morning</option>
<option value = "Evening">Evening</option>
</select ></br>
About yourself: </br>
<textarea name="about"cols="40"rows="4">
Type your text here...
</ textarea>
<input type="submit "value="Submit"/>
</form>
</body>
</html>
Assuming that WAMP server is running, open the browser and enter following URL in its address bar:

http://localhost/htmlform.html
Following Python script (named 'htmlform.py') must have been kept in 'cgi-bin' folder of installation directory.

#!c:\python37\python.exe
# Import modules for CGI handling
import cgi, cgitb
cgitb.enable()
# Create instance of FieldStorage
form = cgi.FieldStorage()
# Get data from fields
nm=form.getvalue('name')
f=form.getvalue('faculty')
b=form.getvalue('batch')
text = form.getvalue('about')
print "Content-type:text/html\r\n\r\n"
print("<html>")
print("<head>")
print("<title>CGI Script</title>")
print("</head>")
print("<body>")
print ("<h 2>Data received from client form</h 2>")
print("Name: {}".format(nm))
print ("</br>")
print("Faculty: {}".format(f))
print ("</br>")
print("Batch: {}".format(b))
print ("</br>")
print("Text : {}".format(text))
print ("</br>")
print("</body>")
print ("</html>")
Fill up data in the form as shown below:Python - CGI Programming

Hit the 'submit' button. Form data is sent to the cgi script mention in 'action' attribute of form tag. It will be retrieved by FieldStorage object. Python script renders it back to client browser. CGI script in Python ('htmlform.py') is given below:

#!c:\python37\python.exe
# Import modules for CGI handling
import cgi, cgitb
cgitb.enable()
# Create instance of FieldStorage
form = cgi.FieldStorage()
# Get data from fields
nm=form.getvalue('name')
f=form.getvalue('faculty')
b=form.getvalue('batch')
text = form.getvalue('about')
print "Content-type:text/html\r\n\r\n"
print("<html>")
print("<head>")
print("<title>CGI Script</title>")
print("</head>")
print("<body>")
print ("<h 2>Data received from client form</h 2>")
print("Name: {}".format(nm))
print ("</br>")
print("Faculty: {}".format(f))
print ("</br>")
print("Batch: {}".format(b))
print ("</br>")
print("Text : {}".format(text))
print ("</br>")
print("</body>")
print ("</html>")```
