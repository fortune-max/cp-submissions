//
// Created by fme on 26/04/2022.
//

#include <bits/stdc++.h>
#define int long long
using namespace std;

signed main(){
    int n, ans = 0; cin >> n;
    vector<int> nums(n);
    for (int i=0; i<n; i++) cin >> nums[i];
    for (int i=0; i<n; i++){
        int sub_ans = 0;
        for (int j=i; j<n; j++){
            sub_ans += nums[j];
            if (sub_ans > 100 * (j-i+1)) ans = max(ans, j-i+1);
        }
    }
    cout << ans << endl;
}