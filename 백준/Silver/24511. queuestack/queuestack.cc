#include <iostream>
#include <deque>

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
    
    int nDataStructure;
    // scanf("%d",&nDataStructure);
    std::cin >> nDataStructure;
    bool boolStack[nDataStructure]  = {false,};
    std::deque<int> dequeList;

    for (int ii = 0; ii < nDataStructure; ++ii) {
        int typeDataStructure;
        // scanf("%d",&typeDataStructure);
        std::cin >> typeDataStructure;
        if( typeDataStructure == 0){
            boolStack[ii]  =  true;
        }
    }    
    
    for (int ii = 0; ii < nDataStructure; ++ii) {
        int num;        
        // scanf("%d", &num);
        std::cin >> num;
        if( boolStack[ii] == true ){
            dequeList.push_back(num);
        }
    }
   
    int numInput;
    // scanf("%d", &numInput);
    std::cin >> numInput;
    for (int ii = 0; ii < numInput; ++ii) {
        int num;        
        // scanf("%d", &num);
        std::cin >> num;        
        dequeList.push_front(num);
        printf("%d ", dequeList.back());
        dequeList.pop_back();
    }        
    return 0;
}