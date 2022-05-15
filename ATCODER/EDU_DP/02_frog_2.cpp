//
// Created by fme on 26/04/2022.
//

#include <bits/stdc++.h>
using namespace std;

int main(){
    int n, k; cin >> n >> k;
    vector<int> nums(n), dp(n, INT_MAX);
    for (int i=0; i<n; i++) cin >> nums[i];
    dp[0] = 0;
    for (int i=1; i<n; i++)
        for (int j=i-1; i-j<=k and j>=0; j--)
            dp[i] = min(dp[i], dp[j] + abs(nums[j] - nums[i]));
    cout << dp.back() << endl;
}