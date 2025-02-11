import requests

#Check if status code is good
def check_status_code():
    #Get files from UCCS website
    res = requests.get("https://www.uccs.edu/") 

    #Determine if request is successful    
    return res.status_code == requests.codes.ok


print(check_status_code())
