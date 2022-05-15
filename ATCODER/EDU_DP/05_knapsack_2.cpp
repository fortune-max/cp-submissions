//
// Created by fme on 15/05/2022.
//

#include <bits/stdc++.h>
#define int long long
using namespace std;

signed main(){
    int N, W, w, v, ans=INT_MIN; cin >> N >> W;
    vector <pair<int, int> > wt_val;
    vector< pair<int, vector<int>> > value_members(100001, {LONG_LONG_MIN, vector<int>(N, 0)});
    for (int i=0; i<N; i++) cin >> w >> v, wt_val.emplace_back(w, v);
    for (int total_value=0; total_value<100001; total_value++){
        auto [min_weight, members] = value_members[total_value];
        for (int idx=0; idx<N; idx++){
            auto [wt, value] = wt_val[idx];
            if (members[idx] or min_weight + wt > W or (min_weight==LONG_LONG_MIN and total_value!=0)) continue;
            auto old_weight = value_members[total_value + value].first==LONG_LONG_MIN?LONG_LONG_MAX:value_members[total_value + value].first;
            auto new_weight = max(value_members[total_value].first, 0LL) + wt;
            if (new_weight < old_weight) {
                auto tmp_members = vector(members.begin(), members.end());
                tmp_members[idx]++;
                value_members[total_value + value].first = new_weight;
                value_members[total_value + value].second = tmp_members;
                if (value_members[total_value + value].first <= W) ans = max(ans, total_value + value);
            }
        }
    }

    cout << ans << endl;
}