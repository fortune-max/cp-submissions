//
// Created by fme on 06/04/2022.
//

/*
ID: fortmax1
TASK: gift1
LANG: C++
*/

#include <bits/stdc++.h>
using namespace std;

int main(){
    ofstream cout ("gift1.out"); ifstream cin ("gift1.in");

    int NP; cin >> NP;
    vector<string> names(NP); map<string, int> gift_amt;
    for(int i=0; i<NP; i++)
        cin >> names[i], gift_amt[names[i]] = 0;

    for(int i=0; i<NP; i++){
        string name; cin >> name;
        int total_money, recv_ct; cin >> total_money >> recv_ct;
        gift_amt[name] -= total_money;
        for (int j=0; j<recv_ct; j++){
            string to_name; cin >> to_name;
            gift_amt[to_name] += int(total_money / recv_ct);
        }

        if (recv_ct) gift_amt[name] += total_money - (int(total_money / recv_ct) * recv_ct);
    }

    for (auto name: names)
        cout << name << " " << gift_amt[name] << endl;

    return 0;
}