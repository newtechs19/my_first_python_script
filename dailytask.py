import os
import commands
import subprocess
import sys

os.system('cls||clear')

def Nginx_status():
        p = subprocess.call(["systemctl", "status", "rh-nginx18-nginx.service"])
        print("Nginx Status Displayed")
        return p

def Unicorn_status():
        p = subprocess.Popen( 'ps -ax | grep puma', shell=True,
                         stdout=subprocess.PIPE)
        (output, err) = p.communicate()
        print "Command output : ", output
        print("Greping puma")
        return p

def Restart_nginx():
        p = subprocess.call(["systemctl", "restart", "rh-nginx18-nginx.service"])
        print("Nginx Restarted")
        return p

def Su_executer():
        p = subprocess.Popen( 'su executer', shell=True,
                         stdout=subprocess.PIPE)
        (output, err) = p.communicate()
        print "Command output : ", output
        return p

def Change_directory():
        p = os.chdir('/directory_name/')
        shell = os.environ.get('SHELL', '/bin/sh')
        os.execl(shell, shell)
        return p

def Kill_puma():
        p = subprocess.Popen( "ps -ax | grep puma | grep master | awk {'print $1 ,$6'}", shell=True,
                         stdout=subprocess.PIPE)
        (output, err) = p.communicate()
        print "Command output : ", output
        os.kill(input("Enter PID "), signal.SIGINT)
        print "puma Process Is Killed"
        return p


def Restart_puma():
        p = subprocess.Popen( 'Rails command', shell=True,
                        stdout=subprocess.PIPE)
        (output, err) = p.communicate()
        print "Command output : ", output
        return p


print "1: Nginx status"
print "2: puma status"
print "3: Restart nginx"
print "4: Su executer"
print "5: Change directory"
print "6: Kill puma"
print "7: Restart puma"
print "0: QUIT"

while True:

    Option = int(raw_input("ENTER THE OPTION "))

    if Option == 1:
        print "Nginx Status:"
        print Nginx_status()

    elif Option == 2:
        print "puma Status"
        print puma_status()

    elif Option == 3:
        print "Restart Nginx"
        print Restart_nginx()

    elif Option == 4:
        print "Change User To executer"
        print Su_executer()

    elif Option == 5:
        print "Change Directory"
        print Change_directory()

    elif Option == 6:
        print "Kill puma"
        print Kill_puma()

    elif Option == 7:
        print "Restart puma"
        print Restart_puma()

    elif Option == 0:
        exit()
    else:
print "The value Enter value from 1-7"
