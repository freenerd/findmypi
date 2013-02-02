#!/usr/bin/env python2.7

# Copyright 2013
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import smtplib, string, subprocess, time, socket, re

# Import ./settings.py file
# If this fails for you, copy settings_example.py to settings.py and change the values
import settings

def get_ifconfig():
    output_if = subprocess.Popen(['ifconfig'], stdout=subprocess.PIPE).communicate()[0]
    
    # ifconfig will always have at least 'lo loopback' as match for inet addr
    # thus we want to find more than one interface with IP
    if (len(re.findall("inet addr", output_if)) > 1):
        return (True, output_if)
    else:
        return (False, None)

def send_mail(settings, BODY):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(settings.username, settings.password)
        server.sendmail(settings.fromaddr, settings.toaddr, BODY)
        server.quit()
    except socket.gaierror:
        print("Couldn't connect to SMTP, trying again in a minute ...")
        time.sleep(60)
        send_mail(settings, BODY)

ifconfig = get_ifconfig();
while (not ifconfig[0]):
    print("Could not determine IP, waiting to retry ...")
    time.sleep(1)
    ifconfig = get_ifconfig()

output_cpu = open('/proc/cpuinfo', 'r').read()

BODY = string.join((
"From: %s" % settings.fromaddr,
"To: %s" % settings.toaddr,
"Subject: Your RasberryPi just booted at " + time.ctime(),
"",
ifconfig[1],
output_cpu,
), "\r\n")

print("Sending email ...")
send_mail(settings, BODY)
