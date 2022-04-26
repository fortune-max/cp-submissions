//
// Created by fme on 26/04/2022.
//

#include <bits/stdc++.h>
using namespace std;

int main(){
    int a, b, c, d; cin >> a >> b >> c >> d;
    if (a > b) swap(a, b);
    if (c > d) swap(c, d);

    if (((c <= a) and (d <= b)) or (c+d <= b))
        cout << "YES" << endl;
    else
        cout << "NO" << endl;
}