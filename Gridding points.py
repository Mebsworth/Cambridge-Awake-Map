

import math




def degrees_to_radians(degrees):
	return degrees * math.pi /180;

def radians_to_degrees(radians):
	return radians  *  180 / math.pi


def compute_offset(startPoint, distance, bearing):
	lat = startPoint[0]
	lng = startPoint[1]

	# in miles. divide by 6371.01for kms
	distRatio = distance/ 3960

	distSine = math.sin(distRatio)
	distCosine = math.cos(distRatio)


	bearing = degrees_to_radians(bearing)
	startLatRad = degrees_to_radians(lat)
	startLngRad = degrees_to_radians(lng)
	startLatCos = math.cos(startLatRad)
	startLatSin = math.sin(startLatRad)

	endLatRads = math.asin((startLatSin * distCosine) + (startLatCos * distSine * math.cos(bearing)))
	endLonRads = startLngRad + math.atan((math.sin(bearing) * distSine * startLatCos)/(distCosine - startLatSin * math.sin(endLatRads)));


	finalLat = radians_to_degrees(endLatRads)
	finalLng = radians_to_degrees(endLonRads)


	

	return [finalLat, finalLng]


def makeGrid(center, gridWidth, gridHeight):
	grid = []
	cellWidth = 0.2
	numWidth = int(gridWidth/cellWidth)
	numHeight = int(gridHeight/cellWidth)

	startDist = math.sqrt((math.pow(gridWidth/2, 2)) + math.pow(gridWidth/2, 2))
	gridTopLeft = compute_offset(center, startDist, 315)
	

	pointer = gridTopLeft
	rowStart = gridTopLeft
	for i in range(numHeight):
		
		row = [pointer]
		for j in range(numWidth):
			next = compute_offset(pointer, 2*cellWidth, 90)
			row.append(next)
			pointer = next

		grid.append(row)

		pointer = compute_offset(rowStart, 2*cellWidth, 180)
		rowStart = pointer


	return grid, numWidth, numHeight

#Boston
#point = [42.360066,-71.059254]
point = [42.359559,-71.088507]
#Cambridge
#point = [42.385891,-71.137454]

print makeGrid(point,11,11)
# #top left corner
# (42.403843,-71.160582)






