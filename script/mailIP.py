import subprocess
import smtplib
import socket
import time
from email.mime.text import MIMEText
import datetime

# the receiver email 
receiver='[your_email]@gmail.com'

def sm(receiver, title, body):
        host = 'smtp.163.com'
        port = 25
        sender = '[your_email]@163.com'
        pwd = '[your_passwd]'

        msg = MIMEText(body, 'html')
        msg['subject'] = title
        msg['from'] = sender
        msg['to'] = receiver

        s = smtplib.SMTP(host, port)
        s.login(sender, pwd)
        s.sendmail(sender, receiver, msg.as_string())

        print 'The mail named %s to %s is sended successly.' % (title, receiver)

# Change to your own account information
today = datetime.date.today()
# Very Linux Specific
arg='ip route list'
p=subprocess.Popen(arg,shell=True,stdout=subprocess.PIPE)
data = p.communicate()
split_data = data[0].split()
ipaddr = split_data[split_data.index('src')+1]
my_ip = 'Your ip is %s' %  ipaddr
print my_ip
strcurtime = time.strftime('%Y-%m-%dT%H:%M:%S',time.localtime(time.        time()))
Subject = 'IP For RaspberryPi on %s' % strcurtime + ': ' + ipaddr
sm(receiver, Subject, my_ip);
