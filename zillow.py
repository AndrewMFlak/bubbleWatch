#=================================================>
import os
from os.path import join, dirname
import dotenv
from dotenv import load_dotenv
dotenv_path=join(dirname(__file__),'.env')
load_dotenv(dotenv_path)
zipCode = os.getenv('placeholder')
zillowAPIkey = os.getenv('zillowAPIkey')
print(zipCode)
print(zillowAPIkey)