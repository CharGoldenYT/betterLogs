# Char's Better Logs (Classic Branch)

This is the last, non pip packaged, version of betterLogs!

This branch is not maintained and only serves to save people time from having to run `pip install chars-betterlogs` by including logs.py directly with your python project!

# USAGE

First drop logs.py somewhere in your folder and import it as you would a normal script (i.e. `from path.to.logs import Logging`) then do the following to set up the logger!

```python
logger:Logging = Logging("filename.extension", "<!-- This goes before the logs! -->", True)
# If you don't want it in the betterLogs-version folder make sure to do the following!:
logger._set_filename("path/to/filename.extension")
```

Tada! Now you have a competent logger that constantly writes to the same file

## IMPORTANT: ALWAYS RUN `logger.close()` BEFORE LETTING YOUR SCRIPT EXIT!