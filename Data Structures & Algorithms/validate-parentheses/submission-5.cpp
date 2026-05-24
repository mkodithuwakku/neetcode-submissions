class Solution {
public:
    bool isValid(string s) {
         // Your implementation here

        // Create stack to hold left brackets
        stack<char> leftbracks;

        unordered_map<char,char> brackMap = {
            {')','('},
            {'}','{'},
            {']','['},
        };

        int count = 0;

        for (char c : s){
            if (c == '(' || c == '{' || c == '['){
                leftbracks.push(c);
            }

            if(leftbracks.empty() == true){return false;}

        
        
            if(c == ')' || c == '}' || c == ']'){
                count++;
        
                if(leftbracks.top() == brackMap[c]){
                    leftbracks.pop();
                    count--;
            
                    if(leftbracks.empty() == true && c == s[s.length()-1] && count == 0 ){
                        return true;
                    }
                }
            }
    
        } 

    return false;
        
    }
};
