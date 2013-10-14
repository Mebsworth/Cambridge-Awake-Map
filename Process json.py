import json

json_file = open("CAMBRIDGE ALL PLACES.json")

data = json.load(json_file)

days = ['sund','mon','tues','wed','thurs','fri','sat']
#Tuesday
times = ['0000','0100','0200','0300','0400','0500','0600','0700','0800','0900','1000','1100','1200','1300','1400','1500','1600','1700','1800','1900','2000','2100','2200','2300']
#print data[0]
#print data[0]["hours"][0]
always_open = []
always_open_ids=[]
counter=-1

f = open("Cambridge Map Data.js","a")

for r in data:
	if r["id"] not in always_open_ids:
		always_open_ids.append(r["id"])
		for p in r["hours"]:
			if int(p["day"])==0:
				if int(p["open"])==0000:
					if p.has_key("close"):
						if int(p["close"])==0000:
							point = str(r["lat"]) +', '+ str(r["lng"])
							always_open.append(point)
							print r["name"],"always open"
							print r["id"]
					else:
						point = str(r["lat"]) +', '+ str(r["lng"])
						always_open.append(point)
						print r["name"],"always open"
						print r["id"]


for i in range(len(days)):
	counter=counter+1
	f.write("\nvar "+days[i]+" = [")
	print days[i]
	for time in times:
		print time
		ids = []
		open_list = []
		for r in data:
			#print r["name"]
			if r["id"] not in ids:
				ids.append(r["id"])
				for p in r["hours"]:
					if int(p["day"]) == counter:
						#print p["day"]
						if p.has_key("close"):
							if int(time) > int(p["open"]):
								if int(time) < int(p["close"]):
									point = str(r["lat"]) +', '+ str(r["lng"])
									open_list.append(point)
									print r["name"]
									print r["id"]
							elif int(p["open"])-int(p["close"]) > 0:
								if int(time)< int(p["close"]) or int(time)>int(p["open"]):
									point = str(r["lat"]) +', '+ str(r["lng"])
									open_list.append(point)
									print r["name"]
									print r["id"]
						# else:
						# 	#print "else"
						# 	point = str(r["lat"]) +', '+ str(r["lng"])
						# 	open_list.append(point)
						# 	print r["name"]
						# 	print r["id"]
			
		open_list = open_list+always_open
		f.write(str(open_list)+',')
	f.write('];')
	#


#print len(data)

#print data[0]