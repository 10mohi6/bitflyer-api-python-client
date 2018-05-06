# bitflyer-client

[![PyPI version](https://badge.fury.io/py/bitflyer-client.svg)](https://badge.fury.io/py/bitflyer-client) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

bitflyer-client is a python client (sync/async) library for bitflyer api

## Installation

    $ pip install bitflyer-client

## Usage

```python
#
# sync
#
from bitflyer_client.sync import Client

client = Clinet(public_key='your api key', private_key='your api secret')
response = client.markets()
print(response.status_code, response.json())

#
# async
#
import grequests
from bitflyer_client.async import Async

client = Async(public_key='your api key', private_key='your api secret')
reqs = [client.markets(), client.board(), client.ticker(), ...]
response = grequests.map(reqs)
for r in response:
	print(r.status_code, r.json())

#
# /v1/markets
#
client.markets()
# [{ "product_code": "BTC_JPY" },{ "product_code": "FX_BTC_JPY" },{ "product_code": "ETH_BTC" },{"product_code": "BTCJPY28APR2017","alias": "BTCJPY_MAT1WK"},{"product_code": "BTCJPY05MAY2017","alias": "BTCJPY_MAT2WK"}]

#
# /v1/board
#
client.board()
# {"mid_price": 33320,"bids": [{"price": 30000,"size": 0.1},{"price": 25570,"size": 3}],"asks": [{"price": 36640,"size": 5},{"price": 36700,"size": 1.2}]}

#
# /v1/ticker
#
client.ticker()
# {"mid_price": 33320,"bids": [{"price": 30000,"size": 0.1},{"price": 25570,"size": 3}],"asks": [{"price": 36640,"size": 5},{"price": 36700,"size": 1.2}]}

#
# /v1/executions
#
client.executions()
# [{"id": 39287,"side": "BUY","price": 31690,"size": 27.04,"exec_date": "2015-07-08T02:43:34.823","buy_child_order_acceptance_id": "JRF20150707-200203-452209","sell_child_order_acceptance_id": "JRF20150708-024334-060234"},{"id": 39286,"side": "SELL","price": 33170,"size": 0.36,"exec_date": "2015-07-08T02:43:34.72","buy_child_order_acceptance_id": "JRF20150708-010230-400876","sell_child_order_acceptance_id": "JRF20150708-024334-197755"}]

#
# /v1/getboardstate
#
client.getboardstate()
# {"health": "NORMAL","state": "RUNNING",}{"health": "NORMAL","state": "MATURED","data": {"special_quotation": 410897}}

#
# /v1/gethealth
#
client.gethealth()
# {"status": "NORMAL"}

#
# /v1/getchats
#
client.getchats()
# [{"nickname": "User1234567","message": "Hello world!","date": "2016-02-16T10:58:08.833"},{"nickname": "ビット太郎","message": "サンプルメッセージ","date": "2016-02-15T10:18:06.67"}]

#
# /v1/me/getpermissions
#
client.getpermissions()
# ["/v1/me/getpermissions","/v1/me/getbalance","/v1/me/getcollateral","/v1/me/getchildorders","/v1/me/getparentorders","/v1/me/getparentorder","/v1/me/getexecutions","/v1/me/getpositions"]

#
# /v1/me/getbalance
#
client.getbalance()
# [{"currency_code": "JPY","amount": 1024078,"available": 508000},{"currency_code": "BTC","amount": 10.24,"available": 4.12},{"currency_code": "ETH","amount": 20.48,"available": 16.38}]

#
# /v1/me/getcollateral
#
client.getcollateral()
# {"collateral": 100000,"open_position_pnl": -715,"require_collateral": 19857,"keep_rate": 5.000}

#
# /v1/me/getcollateralaccounts
#
client.getcollateralaccounts()
# [{"currency_code": "JPY","amount": 10000},{"currency_code": "BTC","amount": 1.23}]

#
# /v1/me/getaddresses
#
client.getaddresses()
# [{"type": "NORMAL","currency_code": "BTC","address": "3AYrDq8zhF82NJ2ZaLwBMPmaNziaKPaxa7"},{"type": "NORMAL","currency_code": "ETH","address": "0x7fbB2CC24a3C0cd3789a44e9073381Ca6470853f"}]

#
# /v1/me/getcoinins
#
client.getcoinins()
# [{"id": 100,"order_id": "CDP20151227-024141-055555","currency_code": "BTC","amount": 0.00002,"address": "1WriteySQufKZ2pVuM1oMhPrTtTVFq35j","tx_hash": "9f92ee65a176bb9545f7becb8706c50d07d4cee5ffca34d8be3ef11d411405ae","status": "COMPLETED","event_date": "2015-11-27T08:59:20.301"}]

#
# /v1/me/getcoinouts
#
client.getcoinouts()
# [{"id": 500,"order_id": "CWD20151224-014040-077777","currency_code": "BTC","amount": 0.1234,"address": "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa","tx_hash": "724c07dfd4044abcb390b0412c3e707dd5c4f373f0a52b3bd295ce32b478c60a","fee": 0.0005,"additional_fee": 0.0001,"status": "COMPLETED","event_date": "2015-12-24T01:40:40.397"}]

#
# /v1/me/getbankaccounts
#
client.getbankaccounts()
# [{"id": 3402,"is_verified": true,"bank_name": "三井住友銀行","branch_name": "アオイ支店","account_type": "普通","account_number": "1111111","account_name": "ビットフライヤータロウ"}]

#
# /v1/me/getdeposits
#
client.getdeposits()
# [{"id": 300,"order_id": "MDP20151014-101010-033333","currency_code": "JPY","amount": 10000,"status": "COMPLETED","event_date": "2015-10-14T10:10:10.001"}]

#
# /v1/me/withdraw
#
client.withdraw(bank_account_id=1234, amount=12000, code=012345)
# {"message_id": "69476620-5056-4003-bcbe-42658a2b041b"}

#
# /v1/me/getwithdrawals
#
client.getwithdrawals()
# [{"id": 700,"order_id": "MWD20151020-090909-011111","currency_code": "JPY","amount": 12000,"status": "COMPLETED","event_date": "2015-10-20T09:09:09.416"}]

#
# /v1/me/sendchildorder
#
client.sendchildorder(price=30000, size=0.1)
# 200 OK

#
# /v1/me/cancelchildorder
#
client.cancelchildorder(child_order_id='JOR20150707-055555-022222')
# 200 OK

#
# /v1/me/sendparentorder
#
client.sendparentorder()
# 200 OK

#
# /v1/me/cancelparentorder
#
client.cancelparentorder()
# 200 OK

#
# /v1/me/cancelallchildorders
#
client.cancelallchildorders()
# 200 OK

#
# /v1/me/getchildorders
#
data = client.getchildorders()
print(data)
# [{"id": 138398,"child_order_id": "JOR20150707-084555-022523","product_code": "BTC_JPY","side": "BUY","child_order_type": "LIMIT","price": 30000,"average_price": 30000,"size": 0.1,"child_order_state": "COMPLETED","expire_date": "2015-07-14T07:25:52","child_order_date": "2015-07-07T08:45:53","child_order_acceptance_id": "JRF20150707-084552-031927","outstanding_size": 0,"cancel_size": 0,"executed_size": 0.1,"total_commission": 0},{"id": 138397,"child_order_id": "JOR20150707-084549-022519","product_code": "BTC_JPY","side": "SELL","child_order_type": "LIMIT","price": 30000,"average_price": 0,"size": 0.1,"child_order_state": "CANCELED","expire_date": "2015-07-14T07:25:47","child_order_date": "2015-07-07T08:45:47","child_order_acceptance_id": "JRF20150707-084547-396699","outstanding_size": 0,"cancel_size": 0.1,"executed_size": 0,"total_commission": 0}]

#
# /v1/me/getparentorders
#
client.getparentorders()
# [{"id": 138398,"parent_order_id": "JCO20150707-084555-022523","product_code": "BTC_JPY","side": "BUY","parent_order_type": "STOP","price": 30000,"average_price": 30000,"size": 0.1,"parent_order_state": "COMPLETED","expire_date": "2015-07-14T07:25:52","parent_order_date": "2015-07-07T08:45:53","parent_order_acceptance_id": "JRF20150707-084552-031927","outstanding_size": 0,"cancel_size": 0,"executed_size": 0.1,"total_commission": 0},{"id": 138397,"parent_order_id": "JCO20150707-084549-022519","product_code": "BTC_JPY","side": "SELL","parent_order_type": "IFD","price": 30000,"average_price": 0,"size": 0.1,"parent_order_state": "CANCELED","expire_date": "2015-07-14T07:25:47","parent_order_date": "2015-07-07T08:45:47","parent_order_acceptance_id": "JRF20150707-084547-396699","outstanding_size": 0,"cancel_size": 0.1,"executed_size": 0,"total_commission": 0}]

#
# /v1/me/getparentorder
#
client.getparentorder(parent_order_id=4242)
# {"id": 4242,"parent_order_id": "JCO20150925-046876-036161","order_method": "IFDOCO","minute_to_expire": 10000,"parameters": [{"product_code": "BTC_JPY","condition_type": "LIMIT","side": "BUY","price": 30000,"size": 0.1,"trigger_price": 0,"offset": 0}, {"product_code": "BTC_JPY","condition_type": "LIMIT","side": "SELL","price": 32000,"size": 0.1,"trigger_price": 0,"offset": 0}, {"product_code": "BTC_JPY","condition_type": "STOP_LIMIT","side": "SELL","price": 28800,"size": 0.1,"trigger_price": 29000,"offset": 0}],"parent_order_acceptance_id": "JRF20150925-060559-396699"}

#
# /v1/me/getexecutions
#
client.getexecutions()
# [{"id": 37233,"child_order_id": "JOR20150707-060559-021935","side": "BUY","price": 33470,"size": 0.01,"commission": 0,"exec_date": "2015-07-07T09:57:40.397","child_order_acceptance_id": "JRF20150707-060559-396699"},{"id": 37232,"child_order_id": "JOR20150707-060426-021925","side": "BUY","price": 33470,"size": 0.01,"commission": 0,"exec_date": "2015-07-07T09:57:40.397","child_order_acceptance_id": "JRF20150707-060559-396699"}]

#
# /v1/me/getpositions
#
client.getpositions()
# [{"product_code": "FX_BTC_JPY","side": "BUY","price": 36000,"size": 10,"commission": 0,"swap_point_accumulate": -35,"require_collateral": 120000,"open_date": "2015-11-03T10:04:45.011","leverage": 3,"pnl": 965,"sfd": -0.5}]

#
# /v1/me/getcollateralhistory
#
client.getcollateralhistory()
# [{"id": 4995,"currency_code": "JPY","change": -6,"amount": -6,"reason_code": "CLEARING_COLL","date": "2017-05-18T02:37:41.327"},{"id": 4994,"currency_code": "JPY","change": 2083698,"amount": 0,"reason_code": "EXCHANGE_COLL","date": "2017-04-28T03:05:07.493"},{"id": 4993,"currency_code": "BTC","change": -14.69001618,"amount": 34.97163164,"reason_code": "EXCHANGE_COLL","date": "2017-04-28T03:05:07.493"}]

#
# /v1/me/gettradingcommission
#
client.gettradingcommission(product_code='BTC_JPY')
# {"commission_rate": 0.001}
```

## Contributing

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request