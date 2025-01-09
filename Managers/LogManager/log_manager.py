# pylint: disable=invalid-name
# pylint: disable=C0103
""" Log Manager: Writes to logs in a given location """
from datetime import datetime

# pylint: disable=invalid-name
class LogManager():
    """ A manager that when called, writes to a text file with the given argument """

    def write_to_file(self, source, log_location, log_message):
        """ Append the given message to the intended log file """

        source_name = source.__class__.__name__
        time = self.get_time()

        with open(log_location, "a", encoding="utf-8") as log_file:
            log_file.write(f'\nTIME: {time} | SOURCE: {source_name} | MESSAGE: {log_message}')
            log_file.close()

    def get_time(self):
        """ Get the time, format it, return it"""

        time_unfortmatted = datetime.now()
        current_time = time_unfortmatted.strftime("%m/%d/%Y %I:%M %p")

        return current_time

if __name__ == "__main__":
    instance = LogManager()
    TEST_LOCATION = '/home/pi/1.Repos/sxv-projects/Managers/LogManager/test_log.txt'

    instance.write_to_file(instance, TEST_LOCATION, "THIS IS A TEST")
