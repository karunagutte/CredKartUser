import logging

class log_generator_class:
    @staticmethod
    def gen_log_method():
        log_file=logging.FileHandler(".\\Logs\\CredKart.log") #create log file in root
        #specify formats
        log_format=logging.Formatter('%(asctime)s - %(funcName)s - %(levelname)s - %(lineno)d - %(message)s')
        log_file.setFormatter(log_format) #set format in log_file
        logger=logging.getLogger() #craete object of logging class
        logger.addHandler(log_file) # keeps adding each log
        logger.setLevel(logging.INFO) #set level of log
        return logger  #returns log


