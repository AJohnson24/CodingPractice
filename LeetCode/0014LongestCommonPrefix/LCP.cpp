class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string prefix = "";
        bool first = true;
        int index;
        for (string s : strs){
            if (first){
                for (char c : s){
                    prefix += c;
                }
                first = false;
            }
            else {
                index = 0;
                for (char c : s){
                    if (c == prefix[index] && index < prefix.length()){
                        index++;
                        continue;
                    }
                    else {
                        prefix = prefix.substr(0,index);
                        break;
                    }
                }
                
                // in case string is shorter than prefix
                if (index < prefix.length() ){
                    prefix = prefix.substr(0,index);
                }
                
            }
            
        } // end of outer for
        
        return prefix;
    }
};
