# Char's Better Python Logger

A project started to fix a problem I was having with the default python logging library

## USAGE

Simply put logs.py into the folder you run your main script from and import the library:
```python
from logs import Logging
```

then make a variable:
```python
#                         The Filename         String to add before the log        Whether to print the log (Defaults to True)
logger:Logging = Logging('filename.log', 'This gets added before the log starts!', False)
```

Tada you now have a callable logger!

### Example Script
```python
from logs import Logging
from datetime import datetime

logger:Logging = Logging('log_' + str(datetime.today().strftime('%d_%m_%Y-%H_%M_%S')) + '.log')

logging.log_info('yipee!')
logging.close() # Don't forget to end the log file before the script ends!
```