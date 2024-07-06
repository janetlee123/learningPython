#To zip a list of file extentions from a directory to an outfile file path 
#REF https://www.tutorialspoint.com/How-to-create-a-zip-file-using-Python

import os 
from zipfile import ZipFile

def zip_files(directory_name, list_of_file_extensions,output_filepath):
    #creating a zipfile object named ZipFile
    with ZipFile(output_filepath, 'w') as zip_object:
        # using os.walk to go through all files in directory
        for folder_name, _, extension in os.walk(directory_name):
            real_path = os.path.relpath(folder_name, directory_name)
            #for each file under their respective folders, make new folder
            for filename in file_names:
                extension, file_names = os.path.splitext(filename)
                if extension.lower() in list_of_file_extensions:
                    zip_object.write(os.path.join(folder_name,file),arcname=os.path.join(real_path,file))
    
    if os.path.exists(output_filepath):
        print("ZIP file created")
    else: 
        print("ZIP file not created")
