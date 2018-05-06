# coding: utf-8
import hashlib
import requests
import time
import hmac
import json

class Client(object):

	def __init__(self, **kwargs):
		self.origin = kwargs.get('origin', 'https://api.bitflyer.jp')
		public_key = kwargs.get('public_key', None)
		if public_key is None:
			raise Exception('public key is absent.')
		self.public_key = public_key
		private_key = kwargs.get('private_key', None)
		if private_key is None:
			raise Exception('private key is absent.')
		self.private_key = private_key
		self.timeout = kwargs.get('timeout', None)

	def _request(self, path, method='GET', params=None):
		uri = '{0}{1}'.format(self.origin, path)
		timestamp = str(time.time())
		text = timestamp + method + path
		if len(params) > 0:
			text += json.dumps(params)
		headers = {
			'ACCESS-KEY': self.public_key,
			'ACCESS-TIMESTAMP': timestamp,
			'ACCESS-SIGN': self._signature(text),
			'Content-Type': 'application/json'
			}
		if method == 'GET':
			res = requests.get(uri, headers=headers, timeout=self.timeout, params=params)
		else: #method == 'POST'
			res = requests.post(uri, headers=headers, timeout=self.timeout, data=params)

		return res

	def _signature(self, params):
		sign = hmac.new(self.private_key.encode('utf-8'), params.encode('utf-8'), hashlib.sha256).hexdigest()
		return sign

	def markets(self, **kwargs):
		path = '/v1/markets'
		params = kwargs

		data = self._request(path, params=params)

		return data

	def board(self, **kwargs):
		path = '/v1/board'
		params = kwargs

		data = self._request(path, params=params)

		return data

	def ticker(self, **kwargs):
		path = '/v1/ticker'
		params = kwargs

		data = self._request(path, params=params)

		return data

	def executions(self, **kwargs):
		path = '/v1/executions'
		params = kwargs

		data = self._request(path, params=params)

		return data

	def getboardstate(self, **kwargs):
		path = '/v1/getboardstate'
		params = kwargs

		data = self._request(path, params=params)

		return data

	def gethealth(self, **kwargs):
		path = '/v1/gethealth'
		params = kwargs

		data = self._request(path, params=params)

		return data

	def getchats(self, **kwargs):
		path = '/v1/getchats'
		params = kwargs

		data = self._request(path, params=params)

		return data

	def getpermissions(self, **kwargs):
		path = '/v1/me/getpermissions'
		params = kwargs

		data = self._request(path, params=params)

		return data

	def getbalance(self, **kwargs):
		path = '/v1/me/getbalance'
		params = kwargs

		data = self._request(path, params=params)

		return data

	def getcollateral(self, **kwargs):
		path = '/v1/me/getcollateral'
		params = kwargs

		data = self._request(path, params=params)

		return data

	def getcollateralaccounts(self, **kwargs):
		path = '/v1/me/getcollateralaccounts'
		params = kwargs

		data = self._request(path, params=params)

		return data

	def getaddresses(self, **kwargs):
		path = '/v1/me/getaddresses'
		params = kwargs

		data = self._request(path, params=params)

		return data

	def getcoinins(self, **kwargs):
		path = '/v1/me/getcoinins'
		params = kwargs

		data = self._request(path, params=params)

		return data

	def getcoinouts(self, **kwargs):
		path = '/v1/me/getcoinouts'
		params = kwargs

		data = self._request(path, params=params)

		return data

	def getbankaccounts(self, **kwargs):
		path = '/v1/me/getbankaccounts'
		params = kwargs

		data = self._request(path, params=params)

		return data

	def getdeposits(self, **kwargs):
		path = '/v1/me/getdeposits'
		params = kwargs

		data = self._request(path, params=params)

		return data

	def withdraw(self, **kwargs):
		path = '/v1/me/withdraw'
		params = kwargs

		data = self._request(path, method='POST', params=params)

		return data

	def getwithdrawals(self, **kwargs):
		path = '/v1/me/getwithdrawals'
		params = kwargs

		data = self._request(path, params=params)

		return data

	def sendchildorder(self, **kwargs):
		path = '/v1/me/sendchildorder'
		params = kwargs

		data = self._request(path, method='POST', params=params)

		return data

	def cancelchildorder(self, **kwargs):
		path = '/v1/me/cancelchildorder'
		params = kwargs

		data = self._request(path, method='POST', params=params)

		return data

	def sendparentorder(self, **kwargs):
		path = '/v1/me/sendparentorder'
		params = kwargs

		data = self._request(path, method='POST', params=params)

		return data

	def cancelparentorder(self, **kwargs):
		path = '/v1/me/cancelparentorder'
		params = kwargs

		data = self._request(path, method='POST', params=params)

		return data

	def cancelallchildorders(self, **kwargs):
		path = '/v1/me/cancelallchildorders'
		params = kwargs

		data = self._request(path, method='POST', params=params)

		return data

	def getchildorders(self, **kwargs):
		path = '/v1/me/getchildorders'
		params = kwargs

		data = self._request(path, params=params)

		return data

	def getparentorders(self, **kwargs):
		path = '/v1/me/getparentorders'
		params = kwargs

		data = self._request(path, params=params)

		return data

	def getparentorder(self, **kwargs):
		path = '/v1/me/getparentorder'
		params = kwargs

		data = self._request(path, params=params)

		return data

	def getexecutions(self, **kwargs):
		path = '/v1/me/getexecutions'
		params = kwargs

		data = self._request(path, params=params)

		return data

	def getpositions(self, **kwargs):
		path = '/v1/me/getpositions'
		params = kwargs

		data = self._request(path, params=params)

		return data

	def getcollateralhistory(self, **kwargs):
		path = '/v1/me/getcollateralhistory'
		params = kwargs

		data = self._request(path, params=params)

		return data

	def gettradingcommission(self, **kwargs):
		path = '/v1/me/gettradingcommission'
		params = kwargs

		data = self._request(path, params=params)

		return data
