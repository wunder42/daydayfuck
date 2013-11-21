# -*- coding:utf-8 -*-
import urllib, urllib2
import json
from xml.etree import ElementTree

class Weather:
	'''Get Recent Weather Info'''
	recent7_info = None
	error = False
	uri = "http://m.weather.com.cn/data/%s.html"
	raw_data = None
	### basic info ###
	city, cityid, data, index = None, None, None, None
	temp, weather, wind = [], [], []
	### end ###

	def __init__(self, raw_data = None, city_id = '101280101'):
		self.raw_data = raw_data
		self.uri =  self.uri % city_id

		if not self.raw_data:
			# self.get_request()
			self.raw_data = request2response(self.uri)

		self.parse_data()

	def get_request(self):
		try:
			request = urllib2.Request(self.uri)
			request.add_header('User-Agent', 'Mozilla/5.0')
			self.raw_data = urllib2.urlopen(request).read()
		except:
			self.raw_data = {'error':True}

	def parse_data(self):
		data = json.loads(self.raw_data).get("weatherinfo", None)
		if data:
			self.city = data.get('city', None)
			self.cityid = data.get('cityid', None)
			self.date = data.get('date_y', None)
			self.index = data.get('index48_d', None)
			self.temp, self.weather, self.wind = [], [], []
			for id in range(1,7):
				self.temp.append(data.get('temp%d' % (id,), None))
				self.weather.append(data.get('weather%d' % (id,), None))
				self.wind.append(data.get('wind%d' % (id,), None))
		else:
			self.error = True

class Bus:
	'''Get Bus Info'''
	
	uri = None
	raw_data = None
	city = None
	query_type = None
	### query type ###
	QUERY_TYPE = {'ROUTE':r'', 'TRANSFOR':r''}
	###

	def __init__(self, query_type = 'ROUTE', city='广州'):
		self.uri = self.QUERY_TYPE.get(query_type, None) % ()

	def parse_data(self):
		if 'ROUTE' == query_type:
			data = ElementTree.fromstring(self.raw_data)
			lines = data.getiterator('lines')
			for line in lines:
				print line
		elif 'TRANSFOR' == query_type:
			pass
		else:
			pass

class BaiduBus:
	'''Get BaiduBus Api'''
	''' http://api.map.baidu.com/direction/v1?mode=transit&origin=%E8%BD%A6%E9%99%82&destination=%E5%AE%A2%E6%9D%91&region=%E5%B9%BF%E5%B7%9E&output=json&ak=B35c8d42832c7b5065f8023890ad597b '''
	
	ak = 'B35c8d42832c7b5065f8023890ad597b'
	output = 'json'
	mode = 'transit'
	region='广州'
	uri = r'http://api.map.baidu.com/direction/v1?mode=%s&origin=%s&destination=%s&region=%s&output=%s&ak=%s'
	raw_data = None
	####
	routes = []
	####

	def __init__(self, origin, destination, mode='transit', output='json', region='广州'):
		self.uri = self.uri % (mode, urllib.quote(origin), urllib.quote(destination), urllib.quote(region), output, self.ak)
		self.parse_data()

	def parse_data(self):
		self.raw_data = request2response(self.uri)
		data = json.loads(self.raw_data)
		if data.get('message', None) == 'ok':
			data = data['result']['routes'] 
			print 'data %d' % len(data)
			for d in data:
				print d['scheme'][0]['distance'], d['scheme'][0]['duration']
				t, d = {}, d['scheme'][0]
				t['distance'] = d['distance']
				t['duration'] = d['duration']
				t['vehicle'] = []
				steps = d['steps']
				for step in steps:
					vehicle = step[0]
					if vehicle['vehicle']:
						t['vehicle'].append(vehicle['vehicle']['name'])
						print vehicle['vehicle']['name']
				# t.vehicle_end_name = 
				# t.vehicle_start_name = 
				# t.vehicle_name = 
				# t.vehicle_stop_num = 
				# print t['distance'], t['duration'], t['vehicle']





###### util: request2response()
def request2response(uri):
	try:
		request = urllib2.Request(uri)
		request.add_header('User-Agent', 'Mozilla/5.0')
		data = urllib2.urlopen(request).read()
	except:
		data = None
		print 'open %s error!' % (uri.encode('utf-8'), )
	return data


if __name__ == '__main__':
	weather = Weather()
	print weather.temp[0].encode('utf-8')
	print ' '.join(weather.weather).encode('utf-8')
	print ' '.join(weather.wind).encode('utf-8')
	print ' '.join(weather.index).encode('utf-8')

	# bus = BaiduBus('车陂', '客村')
	# print bus.uri.encode('utf-8')
	# print bus.raw_data.encode('utf-8')
	# print 'xx'
