# flake8: noqa
from .main import *


# for logging errors on prod
DEBUG = False
ELASTIC_APM["DEBUG"] = True 

# DEBUG = True
# ELASTIC_APM["DEBUG"] = DEBUG 
