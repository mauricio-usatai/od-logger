import requests

class Api:
  def __init__(self, host, port):
    self.url = f'http://{host}:{port}'

  def post(self, data):
    try:
      requests.post(f'{self.url}/log', json=data)
    except Exception as err:
      print(err)