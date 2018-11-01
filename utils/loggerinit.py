import logging

class loggerInit(object):
    def __init__(self, criticalLog, informationLog):

        self.setup_logger('log_info', informationLog)
        self.setup_logger('log_crit', criticalLog)

    @staticmethod
    def setup_logger(self, logger_name, log_file, level=logging.INFO):
        log_setup = logging.getLogger(logger_name)
        formatter = logging.Formatter('%(levelname)s: %(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        fileHandler = logging.FileHandler(log_file, mode='a')
        fileHandler.setFormatter(formatter)
        streamHandler = logging.StreamHandler()
        streamHandler.setFormatter(formatter)
        log_setup.setLevel(level)
        log_setup.addHandler(fileHandler)
        log_setup.addHandler(streamHandler)

    def logger(self, msg, level, logfile):
        if logfile == 'info'  : self.log = logging.getLogger('log_info')
        if logfile == 'crit'  : self.log = logging.getLogger('log_crit')
        if level == 'debug'   : self.log.debug(msg)
        if level == 'info'    : self.log.info(msg)
        if level == 'warning' : self.log.warning(msg)
        if level == 'error'   : self.log.error(msg)
        if level == 'critical': self.log.critical(msg)

class logger(object):
    def __init__(self, criticalLog, informationLog):
        self.loggingUnit = loggerInit(criticalLog, informationLog)
    def debug(self,msg):    self.loggingUnit.logger(msg, "debug"   , "log_info")
    def info(self,msg):     self.loggingUnit.logger(msg, "info"    , "log_info")
    def warning(self,msg):  self.loggingUnit.logger(msg, "warning" , "log_crit")
    def critical(self,msg): self.loggingUnit.logger(msg, "critical", "log_crit")
    def error(self,msg):    self.loggingUnit.logger(msg, "error"   , "log_crit")
