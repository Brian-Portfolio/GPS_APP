class GPS_Location:
	#instance variables assigned to x and y, representing location
	def __init__(self,x,y):
		self.x = x
		self.y = y
	
	#returns a string of the coordinates of both x and y
	def __str__(self):
		s = ''
		s = '(%d,%d)' % (self.x,self.y)
		return s
	
	#returns a string with following contents
	def __repr__(self):
		s = ''
		s = 'GPS_Location(%d,%d)' % (self.x,self.y)
		return s
	
	#returns True if coordinates x and y match instance variable other, or False if they
	#dont match	
	def __eq__(self,other):
		self.other = other
		if (self.x,self.y) == self.other:
			return True 
		else:
			return False	
	
	#Returns the calculated distance between two locations 
	def dist(self,other): 
		distance = 0
		x_coordinate = other.x - self.x
		y_coordinate = other.y - self.y
		distance = x_coordinate + y_coordinate
		return abs(distance)
		
class GPS_POI:
	#instance variables assigned to location, name, and kind
	def __init__(self,location,name,kind):
		self.location = location
		self.name = name
		self.kind = kind
	
	#returns a string using the following instance variables x,y,name,kind
	def __str__(self):
		string1 = '' 
		string1 = '(%d,%d): %s, %s' % (self.location.x,self.location.y,self.name,self.kind) 
		return string1
	
	#returns a recreated string using the same instance variables and the following 
	#contents
	def __repr__(self): 			
		string1 = '' 
		string1 = "GPS_POI(GPS_Location(%d,%d),'%s','%s')" % (self.location.x,self.location.y,self.name,self.kind)
		return string1		
		
class GPS:
	#instance variables assigned to route, map, and current.
	def __init__(self,current,map=None):
		self.route = [] 
		self.map = map
		self.current = current
		if self.map == None:
			self.map = []	 
		
	#accepts a location object, and change current value to this location value	
	def relocate(self,location):
		self.current = location
	
	#accepts a location object, and appends this value to the list route.
	def add_dest(self,location):
		self.route.append(location)
	
	#accepts a location object and removes the first occurence value from the list route 
	def drop_dest(self,location):
		flag = 1
		for i in self.route:
			if location == (i.x,i.y) and flag == 1:
				self.route.remove(i)
				flag = 0
		return self.route	
	
	#instance variable current updates to be the first value in location route and then 
	#removes that value from route. 	
	def arrive_first(self):
		self.current = self.route[0]
		self.route.remove(self.route[0])
	
	#returns a string of one POI value in map and ends with a newline. Returns an empty
	#string if there are no POI values			
	def display_map(self):
		if self.map == []:
			return ''
		string1 = ''
		for i in self.map:
			string1 += str(i)+'\n'
		return string1		 						
	
	#returns a string of representation of all locations in route, each preceded by a dash 	
	def display_route(self):
		if self.route == []:
			return ''
		string1 = ''
		string1 += str(self.current)+'-'	
		for i in self.route:
			string1 += str(i)+'-'
		return string1[:-1]		
		
	#calculates and returns the total Manhattan distance to travel according to the routes 
	#and current	
	def dist_to_travel(self):
		if self.route == []:
			return 0
		x_coord = self.current.x
		y_coord = self.current.y	
		distance = 0
		for i in self.route:
			x_coord	-= i.x
			y_coord -= i.y
		distance += x_coord +y_coord	
		return abs(distance)
		
	#finds all point of interest values in map that match the supplied name and kind 
	#arguments 	
	def search_name_kind(self,name,kind):
		if self.map == []:
			return []
		list1 = []	
		for i in self.map:
			if name == i.name and kind == i.kind:
				list1.append(i)
		return list1
	
	#Finds POI values from map, and checks whether any matching kind is equal to the object
	#kind from map. Also checks whether the distance between the object one from map and
	#current is less than the dist from given parameter. Any matching objects from map or
	#conditions that satisfy the distance criteria are returned in a list. 
	def search_within_dist(self,dist,kind=None):
		list1 = []	
		for i in self.map: 
			x_coord = i.location.x-self.current.x
			y_coord = i.location.y-self.current.y
			distance1 =  abs(x_coord + y_coord)
			if distance1>dist:
				return []
			elif kind == i.kind and  distance1 <= dist:
				list1.append(i)
		return list1
					
	#Finds all POI values from map, and matches any kind variable to the object values 
	#from map. Also checks whether the distance between current location and the object 
	#from map have the minimum distance. Then that object is appended to the list and 
	#returned.  				
	def closest_kind(self,kind):
		list1 = []
		for i in self.map:
			x_coord = i.location.x -self.current.x
			y_coord = i.location.y-self.current.y
			distance = abs(x_coord + y_coord)
			if kind == i.kind :
				list1.append(i)
		return list1						
				
