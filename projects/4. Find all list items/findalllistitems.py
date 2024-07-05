# idex all items in a list 
# input - list ot search, value to search for
# list of indices 

def index_all(itemsList, value): 
    indices = []
    for index, item in enumerate(itemsList):
        if item == value: 
            indices.append([index])
        elif isinstance(itemsList[index],list):
            for i in index_all(itemsList[index], value): 
                print(index, itemsList[index], i )
                indices.append([index]+i)

    print(indices)
    return indices

numlist = [[[1,2,3],2,[1,3]],[1,2,3]] 
index_all(numlist,2)
            
