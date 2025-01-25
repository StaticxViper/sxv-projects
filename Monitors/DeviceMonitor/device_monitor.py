#pylint: disable=missing-docstring
#pylint: disable=unspecified-encoding
#pylint: disable=line-too-long
#pylint: disable=wrong-import-position
#pylint: disable=unnecessary-pass

import sys
sys.path.append('/home/pi/1.Repos/sxv-projects')
import psutil

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

    def get_usage(self):
        """ Get CPU, Memory, Disk , and Power Supply Usage """
        print('Getting Usage...')
        #Get CPU Usage
        cpu_usage = psutil.cpu_percent(interval=1)
        print(f'CPU Usage: {cpu_usage}%')
        #Get Memory Usage
        memory_usage = psutil.virtual_memory()
        print(f'Memory Usage: {memory_usage.percent}%')
        #Get Disk Usage
        disk_usage = psutil.disk_usage('/')
        print(f'Disk Usage: {disk_usage.percent}%')

        return cpu_usage, memory_usage, disk_usage

    def get_network_usage(self):
        """ Get Bandwidth Usage and Network Ping """
        pass

    def get_network_ping(self):
        """ Return Network Ping/Latency """
        pass

    def get_scheduled_cron_jobs(self):
        """ Return Scheduled CRON JOBS """
        pass


if __name__ == "__main__":
    test_instance = DeviceMonitor()
    test_instance.get_usage()
    #test_instance.get_network_usage()
    #test_instance.get_network_ping()
    #test_instance.get_scheduled_cron_jobs()
