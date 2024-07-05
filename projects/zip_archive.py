#To zip a list of file extentions from a directory to an outfile file path 
#REF https://www.tutorialspoint.com/How-to-create-a-zip-file-using-Python

import os 
from zipfile import ZipFile

def zip_files(directorypath, list_of_file_extensions,outputfilepath):
    #creating a zipfile object named ZipFile
    with ZipFile(outputfilepath, 'w') as zip_object:
        # using os.walk to go through all files in directory
        for folder_name, sub_folders, file_names in os.walk(directorypath):
            #for each file under their respective folders, make new folder
            for filename in file_names:
                if filename in os.path.basename(list_of_file_extensions):  
                    #Creating filepath for files in fileextention in directory 
                    file_path = os.path.join(folder_name,filename)
                    
                    # adding files to zip file 
                    zip_object.write(file_path, os.path.basename(file_path)) 
    
    if os.path.exists(outputfilepath):
        print("ZIP file created")
    else: 
        print("ZIP file not created")
