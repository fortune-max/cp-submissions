//
// Created by fme on 26/04/2022.
//

#include <bits/stdc++.h>
using namespace std;

int main(){
    int n, a, b, c, prev_a = 0, prev_b = 0, prev_c = 0, ans_a = 0, ans_b = 0, ans_c = 0; cin >> n;
    for (int i=0; i<n; i++){
        cin >> a >> b >> c;
        ans_a = max(a + prev_b, a + prev_c), ans_b = max(b + prev_a, b + prev_c), ans_c = max(c + prev_a, c + prev_b);
        prev_a = ans_a, prev_b = ans_b, prev_c = ans_c;
    }
    cout << max(ans_a, max(ans_b, ans_c)) << endl;
}