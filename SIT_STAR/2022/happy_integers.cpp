//
// Created by fme on 26/04/2022.
//

#include <bits/stdc++.h>
using namespace std;

int main(){
    int n, ct = 0; cin >> n;
    for (int i=1; i<=n; i++){
        auto num = to_string(i);
        int last = -1, len = 0;
        for (auto n: num){
            if (n-'0' < last) break;
            last = n-'0', len++;
        }
        if (len == num.length()) ct++;
    }
    cout << ct << endl;
}