# save function - saves dictionary into a file 
# loads - saves new information into given file 
import pickle 

def save_dict(dict, outputpath):
    with open(outputpath, 'wb') as saveinput:
        pickle.dump(dict, saveinput)
        

def load_dict(filepath):
    with open(filepath, 'rb') as savedinput:
        opendict = pickle.load(savedinput)
    return opendict 

