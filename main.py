#
#  main.py
#  WhereAmI
#
#  Copyright Matt Jones 2010.
#

#import modules required by application
import objc
import Foundation
import AppKit

from PyObjCTools import AppHelper

# import modules containing classes required to start application and load MainMenu.nib
import WhereAmIAppDelegate

# pass control to AppKit
AppHelper.runEventLoop()
