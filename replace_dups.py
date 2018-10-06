# Remove duplicates in string in-place
# use hash table with all characters in alphabet

NO_OF_CHARS = 256
def toMutable(string):
    List = []
    for i in string:
        List.append(i)
    return List

def remove_dups(str):
    bin_hash = [0] * NO_OF_CHARS
    inplace_index = 0
    result_index = 0 
    res_list = toMutable(str) # you can write a seperate function for the string
    while inplace_index != len(res_list):
        # check if the current character is set in the hash list
        # if its not set
        if bin_hash[ord(res_list[inplace_index])] == 0:
            bin_hash[ord(res_list[inplace_index])] = 1
            res_list[result_index] = res_list[inplace_index]
            result_index+=1
        inplace_index+=1
    return "".join(res_list)[0:result_index]

string = "geeksforgeeks"
print(remove_dups(string))
            
            
        
