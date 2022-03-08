from ftplib import all_errors
import requests
import urllib

with open('url.csv', 'r') as source_file :
 outputfile = open('response.txt','w')
 for line in source_file :
   try :
    response = urllib.request.urlopen(line)
    status_code = response.getcode()
    print('URL',line,"Status code is",status_code,'\n', file=outputfile)
    print(line,"status code is",status_code,'\n')
   except requests.ConnectionError:
    print("failed to connect")
   except all_errors:
       print( line,"bad url",'\n')
       print('URL',line,"Bad URL please check your url",'\n', file=outputfile)
   except ValueError:
       print(line,"ValueError")
       print('URL',line,"ValueError", file=outputfile)