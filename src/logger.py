import datetime

class Logger:
    def __init__(self, name):
        self.name = name

    def info(self, msg):
        self.do_print('INFO', msg)

    def error(self, msg):
        self.do_print('ERROR', msg)

    def do_print(self, level, msg):
        date = datetime.date.today()
        print('[{}][{}][{}] {}'.format(self.name, date, level, msg))