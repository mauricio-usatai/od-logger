from datetime import datetime
from od_logger.api import Api

class SingletonMeta(type):
  _instance = None

  def __call__(cls):
    if cls._instance is None:
      cls._instance = super().__call__()
    return cls._instance
  
  def get_instance(cls):
    return cls._instance
  
class Logger(metaclass=SingletonMeta):
  def config(self,
    service_name=None,
    host='localhost',
    port=8087):

    self.service_name = service_name
    self.api = Api(host, port)

  def log_to_server(self, level, log_message):
    data = {
      'service_name': self.service_name,
      'date': datetime.now().timestamp(),
      'level': level,
      'log_message': log_message,
    }

    self.api.post(data)

  def debug(self, log_message):
    self.log_to_server('debug', log_message)

  def info(self, log_message):
    self.log_to_server('info', log_message)

  def warning(self, log_message):
    self.log_to_server('warning', log_message)

  def error(self, log_message):
    self.log_to_server('error', log_message)
