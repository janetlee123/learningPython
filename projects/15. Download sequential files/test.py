import requests 
import re
import os  
from urllib.parse import urlparse 
import urllib.parse
from requests.compat import urljoin

def download_files(url,folder):
    #Make directory if doesn't already exist 
    if not os.path.exists(folder):
        os.makedirs(folder)

    o=urlparse(url)
    filename = os.path.basename(o.path) 
    file_path = os.path.join(str(folder),filename)

    r = requests.get(url)
    if r.status_code == 200:
        with open(file_path, 'wb') as f:
            f.write(r.content)
            print(f" {filename} downloaded")
    else:
        print("Completed")
        exit()

    #looping through urls 
    #getting the new URL
    getnum = re.findall(r'[0-9]+',filename)[-1]
    newnum = str(int(getnum)+1).zfill(len(getnum))
    filetype = filename.split(getnum[0],1)[0]
    ext = filename.split(getnum[len(getnum)-1])[-1]
    newpath = "../../"+filetype+newnum+ext
    newurl = urllib.parse.urljoin(url,newpath)
    download_files(newurl,folder)



    
    

    