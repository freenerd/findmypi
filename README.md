findmypi
========

Send the local ip address of your Raspberry Pi via email

# Background

When you connect your Raspberry Pi to a network with DHCP, it is sometimes hard to find out the IP of the Pi. Ways to solve this include:

  * Connect a screen/keyboard and look up via 'ifconfig'
  * Look at the DHCP IP assignment table of the router
  * Set a static IP at the Pi
  * Tunnel the Pi through another computer
  * Try out all possible IPs
  * Have the Pi tell you it's IP ...

This script here is the last solution. On boot it will look if the Pi has an IP and send it to you via mail. Boom, you are in!

The repository lives at http://github.com/freenerd/findmypi

# Installation

Clone the repository

  ```bash
  cd ~
  git clone git://github.com/freenerd/findmypi.git
  cd findmypi
  ```

Copy and change the settings file

  ```bash
  cp settings_example.py settings.py
  nano settings.py
  ```

You can enter your own smtp server. The default is using Gmail.

Please note that your email password will be in the settings in plain text. If your RaspberryPi gets stolen, the attacker might gain access to your whole email account. The safest way is to create a dedicated email account. If you use Gmail, you can also use an 'application specific password'.

Once this is done, check if it works locally:

  ```bash
  python findmypi.py

  # check your email inbox for the email
  ```

You will probably want to have this script be executed on startup

  ```bash
  sudo nano /etc/rc.local

  # add to the bottom just before 'exit 0'
  python /home/pi/findmypi/findmypi.py
  ```

Restart your Pi and wait for the email

# Attribution

The code was initially created by Alex on http://raspi.tv/tag/locate-your-missing-raspberry-pi
Big ups for the work!
I only forked and extended it ...
