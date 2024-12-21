// VALID ANAGRAM

#include<bits/stdc++.h>
using namespace std;

bool validAnagram(string input1, string input2){
    if(input1.length() != input2.length()){
        return false;
    }
    
    /* // BRUTE FORCE APPROCH USING SORTING (TIME-O(nlogn), SPACE-O(1))
    sort(input1.begin(), input1.end());
    sort(input2.begin(), input2.end());
    if(input1 == input2) return true;
    else return false;
    */
    
    /* // BETTER APPROCH 1 - USING HASHMAP OR DICTIONARY (TIME-O(n), SPACE-O(1))
    unordered_map<char, int> mpp;
    for(char c : input1){
        mpp[c]++;
    }
    for(char c : input2){
        mpp[c]--;
    }
    for(auto it : mpp){
        if(it.second != 0) return false;
    }
    return true;
    */
    
    // BETTER APPROCH 2 - USING FREQUENCY ARRAY (TIME-O(n), SPACE-O(1))
    int arr[26] = {0};
    for(char c : input1){
        arr[c - 'a']++;
    }
    for(char c : input2){
        arr[c - 'a']--;
    }
    for(char indx : arr){
        if(indx != 0) return false;
    }
    return true;
}

int main(){
    
    // taking input string from user
    string input1, input2;
    cout << "Enter Input String 1 : ";
    cin >> input1;
    cout << "Enter Input String 2 : ";
    cin >> input2;
    
    // calling function
    bool ans = validAnagram(input1, input2);
    
    // output
    if(ans) cout << "true" << endl;
    else cout << "false" << endl;
    
}
