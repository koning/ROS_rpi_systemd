# ROS_rpi_systemd

These systemd files are for starting roscore, a real time
clock  and a shutdown poller on Ubuntu for raspberry pi.

roscore.service    - Start roscore when pi starts
rtchwclock.service - Set time from a real time hwclock.
pishutdown.service - Run a python daemon to poll for a shutdown event.


Edit the roscore.default and roscore.service files to set the user, ROS
version and directories.

Edit the rtchwclock file to set your i2c device and address in the
DEVTYPE and DEVADDR variables. These are currently set for a ds3231
at the address 0x68.

Edit the shutdown_pi.py to set the GPIO pin for polling the shutdown signal.
Info of this file can be found at:
https://www.element14.com/community/docs/DOC-78055/l/adding-a-shutdown-button-to-the-raspberry-pi-b

## Copy the files to /etc:

cd ROS_rpi_systemd

sudo cp *.service *.py /etc/systemd/system

### Copy the roscore.default file to /etc/default:

sudo cp roscore.default /etc/default/roscore


# Enable the services

systemctl daemon-reload

sudo systemctl enable roscore.service

sudo systemctl enable rtchwclock.service

sudo systemctl enable pishutdown.service

# Start the services

sudo systemctl start roscore.service

sudo systemctl start rtchwclock.service

sudo systemctl start pishutdown.service
