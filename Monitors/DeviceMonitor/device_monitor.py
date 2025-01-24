#pylint: disable=missing-docstring
#pylint: disable=unspecified-encoding
#pylint: disable=line-too-long
#pylint: disable=wrong-import-position
#pylint: disable=unnecessary-pass

import sys
sys.path.append('/home/pi/1.Repos/sxv-projects')

from Managers.LogManager.log_manager import LogManager
from Managers.NotificationManager.notification_manager import MyClient

#CPU Usage
#Memory Usage
#Disk Usage

#System Temp

#Bandwidth Usage
#Network Ping/Latency

#Power supply voltage
#
#Bonus:
#Scheduled CRON JOBS

class DeviceMonitor():
    """ Monitor the Raspberry Pi and other devices """

    def __init__(self):
        self.log = LogManager()
        self.notif = MyClient()

        self.device_log = '/home/pi/1.Repos/sxv-projects/docs/logs/device_log.txt'

    def get_device_info(self):
        """ Main method to bring everything together"""
        pass

    def get_usage(self):
        """ Get CPU, Memory, Disk , and Power Supply Usage """
        pass

    def get_network_usage(self):
        """ Get Bandwidth Usage and Network Ping """
        pass

    def get_network_ping(self):
        """ Return Network Ping/Latency """
        pass

    def get_scheduled_cron_jobs(self):
        """ Return Scheduled CRON JOBS """
        pass
