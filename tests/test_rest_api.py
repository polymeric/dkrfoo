import json
import pytest
import requests


class TestRestApi(object):
  """
  Test a simple flask api
  """

  def test_get_store(self):
    """
    Make a simple get request to server
    """
    r = requests.get('http://127.0.0.1:5000/store')
    assert r.status_code == 200

  def test_add_store_entry(self):
    """
    Test new store creation
    """
    payload = {'name': "Victoria's Mad"}
    r = requests.post('http://127.0.0.1:5000/store', json=payload)
    assert u"Victoria's Mad" in json.loads(r.text)['name']

  def test_list_new_store_entry(self):
    """
    Test new store entry exists
    """
    r = requests.get('http://127.0.0.1:5000/store')
    assert "Victoria's Mad" in r.content and r.status_code == 200

if __name__ == '__main__':
    main()
'''
o 2110  curl -d '{"item":"baked-ham"}' -H "Content-Type: application/json" 'http://127.0.0.1:5000/store/blah' -X POST
 2111  curl -d '{"items":"baked-ham"}' -H "Content-Type: application/json" 'http://127.0.0.1:5000/store/blah' -X POST
 2112  curl -d '{"name":"baked-ham"}' -H "Content-Type: application/json" 'http://127.0.0.1:5000/store/blah' -X POST
 2113  curl -d '{"name":"baked-ham"}' -H "Content-Type: application/json" 'http://127.0.0.1:5000/store/blah/item' -X POST
 2114  grep '#' sources/app.py
 2115  curl 'http://127.0.0.1:5000/store'
 2116  curl -d '{"name":"baked-ham", "price":12}' -H "Content-Type: application/json" 'http://127.0.0.1:5000/store/blah/item' -X POST
 2117  curl 'http://127.0.0.1:5000/store'

#post /store data: {name :}
#get /store/<name> data: {name :}
#get /store
#post /store/<name> data: {name :}
#get /store/<name>/item data: {name :}

[{"items":[{"name":"my item","price":15.99}],"name":"My Store"}]



'''


