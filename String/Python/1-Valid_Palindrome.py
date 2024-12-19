# Question Link -> "https://leetcode.com/problems/valid-palindrome/description/"

def validPalindrome(string):
    if len(string) == 0 or len(string) == 1:
        return True
        
    ans = ''
    
    # first checking each char to elinimate non alphanumeric character & spaces and converting to lower case
    for char in string:
        if char.isalnum():
            ans += char.lower()
         
    # taking 2 pointers for comparing each character from start and end to check string is palindrome   
    i = 0
    j = len(ans)-1
    
    while(i < j):
        if ans[i] != ans[j]:
            return False
        i += 1
        j -= 1
        
    return True
    

string = input("Enter Input string : ")
print(validPalindrome(string))
