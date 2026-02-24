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

# version paramétrée

def error_logger(*exc):
  """
  decorateur qui capture certaines exceptions pour logger des erreurs
  """
  def deco(f):
    def wrapper(*args, **kwargs):
      try:
        return f(*args, **kwargs)
      # le bloc peut utiliser une exception ou un tuple d'exceptions
      except exc as e:
        logging.error(e)
    return wrapper
  return deco