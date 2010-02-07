Simple CoreLocation / Yelp API mashup that shows 5 highly-rated nearby bars. You can configure a different category (coffee shops? Japanese restaurants? strip clubs?), adjust the search radius, or search for a specific text (kabob?).

Instructions:

* Open WhereAmIAppDelegate.py

* Replace the definition of YWSID with the value of your yelp api key (available at http://www.yelp.com/developers/retrieve_api_key)

* Build the app in xcode

For use from the command line, you can run (app path)/Contents/MacOS/WhereAmI

TODO

* Smarter logic about accuracy. Right now we just accept the first location update (which tends to be good enough, but it might not always be the case)

* Timeouts. It's just using urllib2.urlopen, which probably doesn't handle the not-connected case very well (although I'm not sure how CoreLocation would work in this case, either)

* Half-stars. The output is rounded down, so 4.5 star and 4 star bars show up the same.
