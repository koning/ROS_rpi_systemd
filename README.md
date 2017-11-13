#ROS_rpi_systemd

These systemd files are for starting roscore, a real time
clock  and a shutdown poller on Ubuntu for raspberry pi.

Edit the rtchwclock file to set your i2c device and address in the
DEVTYPE and DEVADDR variables. These are currently set for a ds3231
at the address 0x68.

Edit the shutdown_pi.py to set the GPIO pin for polling the shutdown signal.
Info of this file can be found at:
https://www.element14.com/community/docs/DOC-78055/l/adding-a-shutdown-button-to-the-raspberry-pi-b

Copy these files to /etc/systemd/system:

cd ROS_rpi_systemd

sudo cp *.service *.py /etc/systemd/system

Copy the roscore.defaults file to /etc/defaults:

sudo cp roscore.defaults /etc/defaults/roscore


Enable the services:

systemctl daemon-reload

sudo systemctl enable roscore.service

sudo systemctl enable rtchwclock.service

sudo systemctl enable pishutdown.service

 Start the services:

sudo systemctl start roscore.service

sudo systemctl start rtchwclock.service

sudo systemctl start pishutdown.service
