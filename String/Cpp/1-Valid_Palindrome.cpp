// Question Link -> "https://leetcode.com/problems/valid-palindrome/description/"

#include<bits/stdc++.h>
using namespace std;

bool validPalindrome(string input){
    if(input == " "){
        return true;
    }
    string ans;
    
    // first checking each character to eliminate non alpha-numeric characters & space and converting to lower case 
    for(char c : input){
        if(isalnum(c)){
            ans += tolower(c);
        }
    }
    
    // taking 2 pointers to compare each character from starting and ending to check palindrome
    int i = 0, j = ans.length()-1;
    
    while(i<j){
        if(ans[i] != ans[j]){
            return false;
        }
        i++;
        j--;
    }
    
    return true;
}


int main(){
    
    // TAKING INPUT STRING
    string input;
    cout << "Enter Input String : ";
    cin >> input;
    
    // CALLING FUNCTION
    if(validPalindrome(input)){
        cout << "true" << endl;
    }
    else cout << "false" << endl;
    
}
