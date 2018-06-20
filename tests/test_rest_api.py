import json
import os
import pytest
import requests


class TestModelFiles(object):
  """
  Test access to files
  """

  @classmethod
  def setup_class(cls):
    try:
      with open('data/random.json','rb') as rj:
        cls.model_json = json.loads(rj.read().decode('utf-8'))
      rj.close()
    except IOError as e:
      print("ERROR: I/O err: random.json not found.{0}: {1}".format(e.errno, e.strerror))

  def testGetDockerVersion(self):
    docker_tag = self.model_json[0]['docker_tag']
    assert "dkrfoo_web:latest" in docker_tag 


class TestRestApi(object):
  """
  Test a simple flask api
  """

  @classmethod
  def setup_class(cls):
    if os.environ.get('is_docker'):
      cls.SERVER='dkrsrv'
    else:
      cls.SERVER="0.0.0.0"

  def test_get_store(self):
    """
    Make a simple get request to server
    """
    r = requests.get('http://{}:5000/store'.format(self.SERVER))
    assert r.status_code == 200

  def test_add_store_entry(self):
    """
    Test new store creation
    """
    payload = {'name': "Victoria's Mad"}
    r = requests.post('http://{}:5000/store'.format(self.SERVER), json=payload)
    assert u"Victoria's Mad" in json.loads(r.text)['name']

  def test_list_new_store_entry(self):
    """
    Test new store entry exists
    """
    r = requests.get('http://{}:5000/store'.format(self.SERVER))
    assert "Victoria's Mad" in r.content and r.status_code == 200

'''
o 2110  curl -d '{"item":"baked-ham"}' -H "Content-Type: application/json" 'http://dkrsrv:5000/store/blah' -X POST
 2111  curl -d '{"items":"baked-ham"}' -H "Content-Type: application/json" 'http://dkrsrv:5000/store/blah' -X POST
 2112  curl -d '{"name":"baked-ham"}' -H "Content-Type: application/json" 'http://dkrsrv:5000/store/blah' -X POST
 2113  curl -d '{"name":"baked-ham"}' -H "Content-Type: application/json" 'http://dkrsrv:5000/store/blah/item' -X POST
 2114  grep '#' sources/app.py
 2115  curl 'http://dkrsrv:5000/store'
 2116  curl -d '{"name":"baked-ham", "price":12}' -H "Content-Type: application/json" 'http://dkrsrv:5000/store/blah/item' -X POST
 2117  curl 'http://dkrsrv:5000/store'

#post /store data: {name :}
#get /store/<name> data: {name :}
#get /store
#post /store/<name> data: {name :}
#get /store/<name>/item data: {name :}

[{"items":[{"name":"my item","price":15.99}],"name":"My Store"}]



'''


