from logs import Logging
import betterLogs
import globalDefs as chars_betterlogs_globalDefs
__all__ = ["Logging", "betterLogs", "getLogFile", "chars_betterlogs_globalDefs"]

def getLogFile(logging:Logging) -> str:
    rawXml = open(logging.filename, 'r')
    xml = rawXml.read(); rawXml.close()
    return xml