# Find x and y with these two equations:
# 3x + 4y = 24
# 4x + 3y = 22
  
#include <bits/stdc++.h> 
using namespace std; 
  
// Function to find the 
// values of X and Y 
void findValues(int a, int b) 
{ 
    // base condition 
    if ((a - b) % 2 == 1) { 
        cout << "-1"; 
        return; 
    } 
  
    // required answer 
    cout << (a - b) / 2 << " " << (a + b) / 2; 
} 
  
// Driver Code 
int main() 
{ 
    int a = 12, b = 8; 
  
    findValues(a, b); 
  
    return 0; 
} 
