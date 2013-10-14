import urllib
import urllib2
import requests
#import xlrd
from collections import OrderedDict
import json as json

import xml.etree.cElementTree as et
import math


# https://maps.googleapis.com/maps/api/place/nearbysearch/xml?&location=42.385891,-71.137454&radius=200&types=grocery_or_supermarket&sensor=false&key=AIzaSyCCvClLiYPof6klI8iMVYO-WfYjtc16hd4

def search1(latlng):
	#NEARBY SEARCH
	latlng1 = str(latlng)[1:-1]
	latlng2 = latlng1.replace(" ","")
	#print "point " +latlng2
	url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/xml?&location='+latlng2+'&radius=330&types=shoe_store&sensor=false&key=AIzaSyCeGd25WDa3-bo3WdBZLNAY5uB_0EoDvN0'
	result = requests.get(url)

	# print result.content

	parsed_xml = et.XML(result.content)

	restaurants = parsed_xml.findall("result")

	for r in restaurants:
		# print "name of restaurant: "+r.find("name").text
		v = r.find("vicinity").text
		v1 = v.split(", ")
		# print "town: "+v1[len(v1)-1]
		town = v1[len(v1)-1]
		if town == "Cambridge":
			# print "restaurant "+r.find("name").text+" is in Cambridge"
			ref = r.find("reference").text
			search2(ref)


def search2(ref):
	url = 'https://maps.googleapis.com/maps/api/place/details/xml?key=AIzaSyCeGd25WDa3-bo3WdBZLNAY5uB_0EoDvN0&reference='+str(ref)+'&sensor=false'
	result = requests.get(url)

	parsed_xml = et.XML(result.content)

	r = parsed_xml.find("result")

	
	rest = OrderedDict()
	#print r.find("name").text
	rest['name'] = r.find("name").text
	#print r.find("geometry").find("location").find("lat").text
	rest['lat'] = r.find("geometry").find("location").find("lat").text
	#print r.find("geometry").find("location").find("lng").text
	rest['lng'] = r.find("geometry").find("location").find("lng").text
	rest['id'] = r.find("id").text
		

	p_list = []

	for element in r.findall("opening_hours"):

		for period in element.findall("period"):
			#print p.find("open").find("time").text
			p = OrderedDict()
			p['day'] = period.find("open").find("day").text
			p['open'] = period.find("open").find("time").text 
			if period.findall("close"):
				p['close'] = period.find("close").find("time").text
			p_list.append(p)
		rest['hours'] = p_list
		
	if len(p_list) != 0:
		place_list.append(rest)
		print r.find("name").text


place_list = []

points = [[42.400357162618235, -71.13353535727407],[42.39457051085982, -71.15704721425573],[42.394570244008065, -71.14921065133547],[42.394569977156316, -71.14137408844857],[42.394569710304566, -71.13353752559493],[42.39456944345283, -71.12570096277466],[42.388783058383744, -71.15704721425573],[42.38878279158613, -71.14921137389592],[42.38878252478851, -71.14137553356937],[42.38878225799089, -71.13353969327613],[42.388781991193284, -71.1257038530162],[42.38878172439568, -71.11786801278959],[42.38299560590768, -71.15704721425573],[42.382995339164175, -71.14921209624316],[42.382995072420684, -71.14137697826385],[42.382994805677185, -71.13354186031785],[42.38299453893369, -71.1257067424051],[42.38299427219019, -71.11787162452566],[42.37720788674223, -71.1492128183773],[42.37720762005283, -71.14137842253211],[42.37720735336344, -71.13354402672024],[42.37720708667405, -71.12570963094163],[42.377206819984664, -71.11787523519627],[42.37720655329528, -71.11004083948421],[42.37141990104967, -71.1335461924836],[42.37141963441437, -71.12571251862607],[42.3714193677791, -71.1178788448018],[42.37141910114381, -71.11004517101077],[42.37141883450853, -71.102211497253],[42.371418567873256, -71.09437782352848],[42.37141830123797, -71.08654414983715],[42.37141803460269, -71.07871047617914],[42.371417767967415, -71.07087680255438],[42.365632715317076, -71.14138130979075],[42.365631648992284, -71.11004950125954],[42.365631382411095, -71.10221654920986],[42.3656311158299, -71.09438359719343],[42.3656308492487, -71.0865506452102],[42.36563058266753, -71.07871769326022],[42.35984419684068, -71.11005383023115],[42.35984393031356, -71.10222159967668],[42.35984366378645, -71.09438936915541],[42.35984339725933, -71.08655713866739],[42.35984313073223, -71.07872490821256],[42.35405674468904, -71.110058157926],[42.354056478215995, -71.10222664865398],[42.35405621174295, -71.0943951394151]]

def search(points):
	for point in points:
		search1(point)

search(points)

# point = "(42.400357162618235, -71.13353535727407)"
# search1(point)

# point = [42.385891,-71.137454]

# grid = makeGrid(point,3,2)

# Serialize the list of dictionaries to JSON
j = json.dumps(place_list)

#print(error_list)

# Write to file
#with open('Cambridge Restaurants.json','w') as f:
with open('CAMBRIDGE SHOE_STORE.json','w') as f:
	f.write(j)



