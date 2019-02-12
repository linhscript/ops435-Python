#!/usr/bin/env python3

# Store one IPv4 address
class IPAddress:
    # You probably want to construct it as a string, but you may want to store it as the four octets separately:
    def __init__(self, address):
        self.address = str(address).split('.')
    # Is this address from a private subnet? e.g. starting with 192.168. or 10.
    def isPrivate(self):
    	if self.address[0] == '192':
    		if self.address[1] == '168':
    			return True
    		else:
    			return False
    	elif self.address[0] == '10':
    		return True
    	else:
    		return False		 
# Store information about a person, perhaps someone you'll be adding as a user to a system:
class Person:
    def __init__(self,name):
    	self.name = str(name)
    	self.name_list = []

    def add_person (self):
    	(self.name_list).append(self.name)
    	return self.name_list

# Store information about different models from a specific manufacturer. Perhaps how many seats they have and how much fuel they use and the price range:
# Doesn't have to be BMW, pick any car or bike manufacturer:
class BMWModel:
	def __init__(self,models):
		self.models = str(models)
    

# Store information about a specific car that someone owns.
# Spend some time thinking why this class is different than the one above, and whether it has to be different:
class Car: