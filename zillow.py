#=================================================>
import os
from os.path import join, dirname
import dotenv
from dotenv import load_dotenv
dotenv_path=join(dirname(__file__),'.env')
zipCode = os.getenv('placeholder')
print(zipCode)