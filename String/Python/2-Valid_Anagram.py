# VALID ANAGRAM

def validAnagram(input1 : str, input2 : str) -> bool:
    if( len(input1) != len(input2) ):
        return False
        
    ''' # BRUTE FORCE USING SORTING (TIME-O(nlogn), SPACE-O(1))
    input1 = sorted(input1)
    input2 = sorted(input2)
    if( input1 == input2 ):
        return True
    else:
        return False
    '''
    
    '''' # BETTER APPROCH 1 USING HASHMAP OR DICTIONARY (TIME-O(n), SPACE-O(1))
    #or dic = defaultdict(int) which will Initialize a defaultdict with int, which defaults to 0 
    dic = {}     
    for ch in input1:
        if(ch in dic):
            dic[ch] += 1
        else:
            dic[ch] = 1
    for ch in input2:
        if(ch in dic):
            dic[ch] -= 1
        else:
            dic[ch] = 1
    for ch in dic:
        if( dic[ch] != 0 ):
            return False
    return True
    '''
    
    # BETTER APPROCH 2 - USING FREQUENCY ARRAY (TIME-O(n), SPACE-O(1))
    arr = [0] * 26
    for ch in input1:
        arr[ord(ch) - ord('a')] += 1
    for ch in input2:
        arr[ord(ch) - ord('a')] -= 1
    for i in arr:
        if i != 0:
            return False
    return True
    
        
        
input1 = input("Enter Input String 1 : ")
input2 = input("Enter Input String 2 : ")

print(validAnagram(input1, input2))
    
