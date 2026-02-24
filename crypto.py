from hashlib import md5
from string import ascii_lowercase
from time import time
import itertools
import logging

def sign(target: str) -> str:
  octets = bytes(target, "utf8")
  return md5(octets).hexdigest()

def brute_force(secret: str):
  for i in itertools.count(1):
    logging.debug(f"longueur: {i}")
    for tup in itertools.product(ascii_lowercase, repeat=i):
      word = "".join(tup)
      if sign(word) == secret:
        return word