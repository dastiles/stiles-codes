class Logger(object):
    def __init__(self, filename):
        self.filename = filename

    def write_log(self, level, msg):
        with open(self.filename, 'a') as log_file:
            log_file.write("[{0}] {1}\n".format(level, msg))

    def critical(self, level, msg):
        self.write_log('CRITICAL', msg)

    def erorr(self, level, msg):
        self.write_log('ERROR', 'msg')

    def warn(self, level, msg):
        self.write_log('WARN', 'msg')

    def info(self,  msg):
        self.write_log('INFO', msg)

    def debug(self, level, msg):
        self.write_log('DEGUG', 'msg')
