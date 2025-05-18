import csv
from datetime import datetime, timedelta

class Logger:
    def __init__(self, log_file='data/logs.csv'):
        self.log_file = log_file
        self.entries = []

    def log_entry(self, user_id):
        entry_time = datetime.now()
        self.entries.append({'user_id': user_id, 'entry_time': entry_time, 'exit_time': None, 'lounge_time': None, 'meeting_time': None})
        self._update_log_file()

    def log_exit(self, user_id):
        exit_time = datetime.now()
        for entry in self.entries:
            if entry['user_id'] == user_id and entry['exit_time'] is None:
                entry['exit_time'] = exit_time
                self._update_log_file()
                break

    def log_lounge_time(self, user_id, duration):
        for entry in self.entries:
            if entry['user_id'] == user_id:
                entry['lounge_time'] = duration
                self._update_log_file()
                break

    def log_meeting_time(self, user_id, duration):
        for entry in self.entries:
            if entry['user_id'] == user_id:
                entry['meeting_time'] = duration
                self._update_log_file()
                break

    def _update_log_file(self):
        with open(self.log_file, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['user_id', 'entry_time', 'exit_time', 'lounge_time', 'meeting_time'])
            writer.writeheader()
            for entry in self.entries:
                writer.writerow(entry)