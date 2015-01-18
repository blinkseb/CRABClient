"""
This module should be erased for March release.
"""
import logging
import inspect
from CRABClient.ClientUtilities import colors

def printModuleRetirementMsg():
    curframe = inspect.currentframe()
    calframe = inspect.getouterframes(curframe, 2)
    msg  = "The method %s is now available in the CRABClient.UserUtilities module." % (calframe[1][3])
    msg += " From 1 April 2015, loading %s from CRABClient.client_utilities" % (calframe[1][3])
    msg += " will not be possible anymore (CRABClient.client_utilities will be removed)."
    msg += " Please change your code accordingly before 1 April 2015."
    tblogger = logging.getLogger('CRAB3.all')
    tblogger.info("%sWarning%s: %s" % (colors.RED, colors.NORMAL, msg))


def getUsernameFromSiteDB():
    printModuleRetirementMsg()
    from CRABClient.UserUtilities import getUsernameFromSiteDB as getUsernameFromSiteDB_new
    return getUsernameFromSiteDB_new()


def basicConfig():
    printModuleRetirementMsg()
    from CRABClient.UserUtilities import basicConfig as basicConfig_new
    return basicConfig_new()
   

def getFileFromURL(url, filename = None):
    printModuleRetirementMsg()
    from CRABClient.UserUtilities import getFileFromURL as getFileFromURL_new
    return getFileFromURL_new(url, filename)
 
