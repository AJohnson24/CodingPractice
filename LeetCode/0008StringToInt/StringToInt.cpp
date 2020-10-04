class Solution {
public:
    int myAtoi(string str) {
        // eliminate whitespace & find +/-
        bool negative = false;
        int index = 0;
        string trimmedString;
        for (char c : str){
            if (c == ' '){
                index++;
                continue;
            } else if (c == '+') {
                trimmedString = str.substr(index+1, string::npos);
                break;
            } else if (c == '-') {
                trimmedString = str.substr(index+1, string::npos);
                negative = true;
                break;
            } else {
               trimmedString = str.substr(index, string::npos);
                break;
            }
        } // end of for
        
        // construct int
        int newInt = 0;
        for (char c : trimmedString){
            if (c > 47 && c < 58){
                if (newInt > INT_MAX/10){
                    return INT_MAX;
                } else if (newInt < INT_MIN/10){
                    return INT_MIN;
                }
                newInt *= 10;
                if (negative){
                    if (newInt < (INT_MIN + (c-48) ) ){
                        return INT_MIN;
                    }
                    newInt -= c-48;
                }
                else {
                    if (newInt > (INT_MAX - (c-48) ) ){
                        return INT_MAX;
                    }
                    newInt += c-48;
                }
            }
            else {
                break;
            }
        }
        
        return newInt;
        
    }
};
