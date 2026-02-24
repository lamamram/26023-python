import logging

def error_logger(f):
  """
  decorateur qui capture certaines exceptions pour logger des erreurs
  """
  def wrapper(*args, **kwargs):
    try:
      return f(*args, **kwargs)
    except ValueError as e:
      logging.error(e)
  return wrapper