//
// Created by fme on 14/05/2022.
//

#include <bits/stdc++.h>
#define int long long
using namespace std;

signed main(){
    int N, W, w, v, ans=INT_MIN; cin >> N >> W;
    vector <pair<int, int> > wt_val;
    vector <pair<int, vector<int>>> capacity_members(W+1, {0, vector<int>(N, 0)});
    for (int i=0; i<N; i++)
        cin >> w >> v, wt_val.emplace_back(w, v);

    for (int capacity=0; capacity<W; capacity++){
        auto [max_value, members] = capacity_members[capacity];
        for (int idx=0; idx<N; idx++){
            auto [wt, value] = wt_val[idx];
            if (members[idx] or capacity + wt > W) continue;
            if (capacity_members[capacity].first + value >= capacity_members[capacity + wt].first) {
                auto tmp_members = vector(members.begin(), members.end());
                tmp_members[idx]++;
                capacity_members[capacity + wt].first = capacity_members[capacity].first + value;
                capacity_members[capacity + wt].second = tmp_members;
                ans = max(ans, capacity_members[capacity].first + value);
            }
        }
    }

    cout << ans << endl;
}