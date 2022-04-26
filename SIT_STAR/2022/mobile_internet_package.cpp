//
// Created by fme on 26/04/2022.
//

#include <bits/stdc++.h>
#define int long long
using namespace std;

signed main(){
    int s, c1, c2, p;
    cin >> s >> c1 >> c2 >> p;
    cout << c1 + max(0LL, p-s) * c2 << endl;
}