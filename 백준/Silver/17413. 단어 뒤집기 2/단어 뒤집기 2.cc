#include <iostream>
#include <string>
#include <sstream>

void reverseStr(std::string& str);
void operateStr(std::string str);

int main() {
    std::string inputString;
    std::getline(std::cin, inputString);

    operateStr(inputString);
    return 0;
}

void operateStr(std::string str){
    // printf("\nintEnd str: %ld", str.length());                
    // printf("\nstr: %s\n", str.c_str());                
    int intEnd = str.length();
    if (intEnd == 0){
        return;
    }
        
    if( str[0] != '<'){
        int ii;
        bool flagBracket = false;
        bool flagSpace   = false;
        for(ii = 0; ii < intEnd; ++ii){        
            if( str[ii] == '<' ){
                flagBracket = true;
                break;
            }
            if( str[ii] == ' ' ){
                flagSpace = true;
                break;
            }
        }

        if( flagBracket ){
            std::string tmpString = str.substr( 0, ii );        
            reverseStr( tmpString );
            printf("%s", tmpString.c_str());
            operateStr(str.substr( ii, intEnd ));
        }
        else if( flagSpace ){
            std::string tmpString = str.substr( 0, ii );        
            reverseStr( tmpString );
            printf("%s", tmpString.c_str());         
            printf(" ");
            operateStr(str.substr( ii+1, intEnd ));
        }
        else{     
            reverseStr( str );
            printf("%s", str.c_str());         
        }
    }
    else{
        bool flag = true;
        int tmpIdx1 = 0;
        for(int ii = 1; ii < intEnd; ++ii){        
   
            if( flag == true && str[ii] == '>'){
                printf("%s", str.substr( tmpIdx1, ii+1 ).c_str());
                operateStr(str.substr( ii+1, intEnd ));
                break;
            }
        }
    }
}

void reverseStr(std::string& str){
    int n = str.length();
    for( int ii = 0; ii < n/2; ++ii){
        std::swap(str[ii], str[n-ii-1]);
    }
}