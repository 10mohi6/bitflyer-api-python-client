# coding: utf-8
import grequests
import time
import json
from sync import Client

class Async(Client):

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
			res = grequests.get(uri, headers=headers, timeout=self.timeout, params=params)
		else: #method == 'POST'
			res = grequests.post(uri, headers=headers, timeout=self.timeout, data=params)

		return res
