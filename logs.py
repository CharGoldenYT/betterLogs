from datetime import datetime
from inspect import currentframe, getframeinfo
from io import TextIOWrapper

# Shortcuts for my Haxe self
false:bool = False
true:bool = True
null:None = None

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

class Logging:

    version:str = '3.1h'
    filename:str = f'betterLogs_{version.replace('.', '-')}/log.xml'
    allowPrinting:bool = False

    def __init__(self, filename:str, beforeBeginning:str = '', allowPrinting:bool = true):
        self.filename = f'betterLogs_{self.version.replace('.', '-')}/{filename}'
        self.createDir()
        self.write(beforeBeginning + f'\n<!-- Log Generator: "Better Logs V{self.version}" | Better Logs by Char @annyconducter on Discord | https://github.com/CharGoldenYT/betterLogs -->\n<!-- START OF LOG -->\n')
        return
    
    def createDir(self):
        import os
        
        try:
            os.makedirs('betterLogs')
        except OSError as e:
            if e.errno != 17:
                print(f'Could not create log directory! "{str(e)}" make sure you have write access')
                exit(1)

    def write(self, content:str):
        filename = self.filename
        logfile_lock = open(filename, 'a')
        logfile_lock.write(content)
        logfile_lock.close()

    def levelToString(level:str) -> str:
        level = level.lower()

        color = '[MISC    ]'
        if level == 'info':color = '[INFO    ]:'
        if level == 'warn' or level == 'warning':color = '[WARNING ]:'
        if level == 'err' or level == 'error':color = '[ERROR   ]:'
        if level == 'critical':color = '[CRITICAL]:'
        if level == 'fatal':color = '[FATAL   ]:'

        return color

    def log(self, log:str, level:str, includeTimestamp:bool = true, isHeader:bool = false, fileFrom:str = '', pos:int = 0):
        time = str(datetime.today().strftime('%d-%m-%Y %H:%M:%S'))
        timeString = '[' + time + ']: '

        color:str
        level = level.lower()
        if level == 'info':color = bcolors.OKBLUE + '[INFO    ]:'
        if level == 'warn' or level == 'warning':color = bcolors.WARNING + '[WARNING ]:'
        if level == 'err' or level == 'error':color = bcolors.FAIL + '[ERROR   ]:'
        if level == 'critical':color = bcolors.FAIL + '[CRITICAL]:'
        if level == 'fatal':color = bcolors.FAIL + '[FATAL   ]:'
        if isHeader: color = bcolors.HEADER + '[INFO    ]'

        if not includeTimestamp:
            timeString = ''

        fileString = ''

        if fileFrom != '':
            fileString = fileFrom + ':' + str(pos) + ':'

        logString = timeString + fileString + log

        if self.allowPrinting: print(color + logString)

        self.write('<!-- "' + logString + '" -->\n')

    def log_header(self, log:str, level:str, includeTimestamps:bool = true,  fileFrom:str = '', pos:int = 0):
        self.log(log, level, includeTimestamps, true, fileFrom, pos)

    def log_info(self, log:str, includeTimestamps:bool = true, fileFrom:str = '', pos:int = 0):
        self.log_header(log, 'info', includeTimestamps, fileFrom, pos)

    def log_error(self, log:str, includeTimestamps:bool = true, fileFrom:str = '', pos:int = 0):
        self.log(log, 'error', includeTimestamps, false, fileFrom, pos)

    def log_err(self, log:str, includeTimestamps:bool = true, fileFrom:str = '', pos:int = 0):
        print(bcolors.WARNING + '[WARNING ]:betterLogs.py:80:log_err() is deprecated! use log_error() instead')
        self.log_error(log, includeTimestamps, fileFrom, pos)

    def log_warning(self, log:str, includeTimestamps:bool = true, fileFrom:str = '', pos:int = 0):
        self.log(log, 'warn', includeTimestamps, false, fileFrom, pos)

    def log_warn(self, log:str, includeTimestamps:bool = true, fileFrom:str = '', pos:int = 0):
        print(bcolors.WARNING + '[WARNING ]:betterLogs.py:87:log_warn() is deprecated! use log_warning() instead')
        self.log_warning(log, includeTimestamps, fileFrom, pos)

    def log_critical(self, log:str, includeTimestamps:bool = true, fileFrom:str = '', pos:int = 0):
        self.log(log, 'critical', includeTimestamps, false, fileFrom, pos)

    def log_fatal(self, log:str, includeTimestamps:bool = true, fileFrom:str = '', pos:int = 0):
        self.log(log, 'fatal', includeTimestamps, false, fileFrom, pos)

    def close(self):
        self.write('<!--  END OF LOG  -->')