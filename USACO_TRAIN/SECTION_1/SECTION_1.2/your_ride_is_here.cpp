//
// Created by fme on 05/04/2022.
//

/*
ID: fortmax1
TASK: ride
LANG: C++
*/

#include <bits/stdc++.h>
using namespace std;

int main(){
    ofstream fout ("ride.out"); ifstream fin ("ride.in");
    string txt_1, txt_2; fin >> txt_1 >> txt_2;

    int total_1 = 1, total_2 = 1;
    for (auto c: txt_1) total_1 = (total_1 * (c - 'A' + 1)) % 47;
    for (auto c: txt_2) total_2 = (total_2 * (c - 'A' + 1)) % 47;

    fout << (total_1 == total_2 ?"GO":"STAY") << endl;
    return 0;
}