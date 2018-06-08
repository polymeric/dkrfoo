import unittest
import requests

#from sources import app

class TestRestApi(unittest.TestCase):
  """
  Test a simple flask api
  """

  def test_get_call(self):
    """
    Make a simple get request to server
    """
    r = requests.get('http://127.0.0.1:5000')
    self.assertTrue(len(r.text) > 0)


if __name__ == '__main__':
    unittest.main()
