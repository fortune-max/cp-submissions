//
// Created by fme on 26/04/2022.
//

#include <bits/stdc++.h>
using namespace std;

signed main(){
    int n; cin >> n;
    vector<int> nums(n), dp(n, 0);
    for (int i=0; i<n; i++) cin >> nums[i];
    dp[1] = abs(nums[1] - nums[0]);
    for (int i=2; i<n; i++)
        dp[i] = min(dp[i-2] + abs(nums[i] - nums[i-2]), dp[i-1] + abs(nums[i] - nums[i-1]));
    cout << dp.back() << endl;
}