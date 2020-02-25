#=================================================>
import os
from os.path import join, dirname
import dotenv
from dotenv import load_dotenv
dotenv_path=join(dirname(__file__),'.env')
load_dotenv(dotenv_path)
#=================EnvironmentVariables==================>
zipCodeGet = os.getenv('citystatezip')
zwsIdGet = os.getenv('zws-id')
addressGet = os.getenv('address')
# citystatezip = os.getenv('citystatezip')
# rentzestimate = False


#=================Workflow===============================>
# print(zipCode)
#print(zwsid)
#print(address)
#print(citystatezip)
# userZip = input("Enter the zipcode you would like to search:  ")
# print(userZip)
# start = ""
# workflowStart()
def importEnvironmentVariable():
    import os
    from os.path import join, dirname
    import dotenv
    from dotenv import load_dotenv
    dotenv_path=join(dirname(__file__),'.env')
    load_dotenv(dotenv_path)
    print(os.getenv('address'))
    print(os.getenv('citystatezip'))
    print(os.getenv('zws-id'))

def zillowApiCall(importEnvironmentVariable):
    importEnvironmentVariable
    from pyzillow.pyzillow import ZillowWrapper, GetDeepSearchResults
    address = os.getenv('address')
    print(address)
    print("address returned")
    zipcode = os.getenv('citystatezip')
    print(zipcode)
    print("zipcode returned")
    zillow_data = ZillowWrapper(os.getenv("zws-id"))
    deep_search_response = zillow_data.get_deep_search_results(address,zipcode)
    result = GetDeepSearchResults(deep_search_response)
    print(result.zillow_id) 
    print("Function Done")
# def zillowPropertyReturn(function):
    # zillow_id = 'YOUR ZILLOW ID'
    # ...
    # zillow_data = ZillowWrapper(YOUR_ZILLOW_API_KEY)
    # updated_property_details_response = zillow_data.get_updated_property_details(zillow_id)
    # result = GetUpdatedPropertyDetails(updated_property_details_response)
    # ...
    # result.rooms

    # number of rooms of the home

    # The following attributes are currently supported:
# importEnvironmentVariable()
zillowApiCall(importEnvironmentVariable())
print('workflow function completed')
#=====================Ended================================>
