import requests

__author__ = "Griffith Asare Awuah (@gwuah)"

class ogma():
	"""Language Detection Library For Pythonistas"""

	def __init__(self, accessKey):
		self.payload = {'access_key': str(accessKey)} 

	def detect(self, phrase) :
		self.payload['query'] = str(phrase) 
		try :
			r = requests.get('http://apilayer.net/api/detect', self.payload)
			self.response = r.json()
			if (r.status_code == requests.codes.ok) and (self.response['success'] != False) :
				# connection successful! You were able to get meaningful data from the endpoint
				return "{}".format(self.response['results'][0]['language_name'])
			else :
				if r.status_code[0] == 4 :
					# couldn't connect to language layer due to no inetrnet access
					print("Detection wasn't sucessful. \nThere was an error from your side. \nCheck Your Internet Connection.")
				elif r.status_code[0] == 5 : 
					# Youre connected to a network, but theres no internet access
					print("Detection wasn't sucessful \nThere was an error from your server \nTry again later")
				elif (self.response['success'] == False) and (self.response['error']['code'] == 101) :
					# You didnt submit a correct payload probably
					return self.response['error']['info'][:-41]
				elif (self.response['success'] == False) and (self.response['error']['code'] == 210) :
					# You didnt submit a correct payload probably
					return self.response['error']['info'][:-43]
		except requests.exceptions.ConnectionError : 
				print("Detection wasn't sucessful. \nYou are not connected to the internet Connection.")