# -*- coding: utf-8 -*-

#
#  WhereAmIAppDelegate.py
#  WhereAmI
#
#  Copyright Matt Jones 2010.
#
import json
import sys
import urllib2

from Foundation import *
from AppKit import *
from CoreLocation import *

YWSID = '<insert here>'

class WhereAmIAppDelegate(NSObject):
	locationManager = None

	def applicationDidFinishLaunching_(self, sender):
		self.locationManager = CLLocationManager.alloc().init()
		self.locationManager.setDelegate_(self)
		self.locationManager.startUpdatingLocation()

	def applicationWillTerminate_(self, notification):
		pass

	def locationManager_didUpdateToLocation_fromLocation_(self, manager, old_location, new_location):
		if new_location:
			lng, lat = new_location.coordinate().longitude, new_location.coordinate().latitude

			url = "http://api.yelp.com/business_review_search?num_biz_requested=5&category=bars&lat=%s&long=%s&radius=1.0&ywsid=%s" % (lat, lng, YWSID)
			
			response = json.loads(urllib2.urlopen(url).read())
			if response['message']['code'] != 0:
				print "Error: %s" % message['text']

			bizs = response['businesses']

			biz_names = [biz['name'] for biz in bizs]
			ratings = [biz['avg_rating'] for biz in bizs]
			addresses = ["%s" % biz['city'] for biz in bizs]
			distances = ["%.1f mi" % biz['distance'] for biz in bizs]

			biz_name_length = max(map(len, biz_names))
			address_length = max(map(len, addresses))

			for name, rating, address, distance in zip(biz_names, ratings, addresses, distances):
				stars = u'★' * int(rating)
				stars += u'☆' * (5 - int(rating))

				formatted = u"%(name)s (%(distance)s) %(stars)s" % locals()

				print formatted.encode('utf8')

			self.locationManager.stopUpdatingLocation()

			NSApplication.sharedApplication().terminate_(self)

	def locationManager_didFailWithError_(self, manager, error):
		NSLog("Location failure.")

