#pylint: disable=missing-docstring
#pylint: disable=unspecified-encoding
#pylint: disable=line-too-long
#pylint: disable=wrong-import-position
#pylint: disable=unnecessary-pass

import sys
sys.path.append('/home/pi/1.Repos/sxv-projects')
import os
from datetime import datetime, timedelta
import psutil

from Managers.LogManager.log_manager import LogManager
from Managers.NotificationManager.notification_manager import MyClient

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

    def get_system_temp(self):
        """ Get System Temperature """
        print('Getting System Temp...')
        with open('/sys/class/thermal/thermal_zone0/temp', 'r') as file:
            temp_celcius = int(file.read()) / 1000
            temp_fahrenheit = (temp_celcius * 9/5) + 32
            print(f'System Temp: {temp_celcius} C')
            print(f'System Temp: {temp_fahrenheit} F')
            file.close()
        return temp_celcius, temp_fahrenheit

    def get_network_usage(self):
        """ Get Bandwidth Usage and Network Ping """
        print('Getting Network Usage...')
        #Get Bandwidth Usage
        net_io = psutil.net_io_counters()
        print(f"Bytes Sent: {net_io.bytes_sent}, Bytes Received: {net_io.bytes_recv}")

        #Get Ping
        ping = os.system("ping -c 1 google.com")
        print(f'Ping: {ping}')
        print('Online' if ping == 0 else 'Offline')

        #Get Latency
        latency = os.system("ping -c 1 google.com | grep 'time='")
        print(f'Latency: {latency}')

        return net_io, ping, latency

    def get_uptime(self):
        """ Get System Uptime """
        print('Getting Uptime...')
        uptime = timedelta(seconds=int(psutil.boot_time()))
        print(f'Uptime: {uptime}')

        #Current Time
        current_time = datetime.now()

        return uptime, current_time

    def get_job_data(self):
        """ Return Scheduled CRON JOBS """
        print('Getting Scheduled CRON JOBS...')
        cron_jobs = os.system("crontab -l")
        print(f'CRON JOBS: {cron_jobs}')

        #Display top 3 Processes
        info = []
        for proc in sorted(psutil.process_iter(attrs=['pid', 'name', 'cpu_percent']), key=lambda p: p.info['cpu_percent'], reverse=True)[:3]:
            print(proc.info)
            info.append(proc.info)

        return cron_jobs, info


if __name__ == "__main__":
    test_instance = DeviceMonitor()
    test_instance.get_usage()
    test_instance.get_system_temp()
    test_instance.get_network_usage()
    test_instance.get_uptime()
    test_instance.get_job_data()
