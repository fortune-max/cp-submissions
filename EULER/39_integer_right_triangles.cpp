#include <bits/stdc++.h>
using namespace std;


int main(){
  vector<int> freqs(1001, 0);
  for (int p=12; p<1001; p++){
    for (int a=3; a<334; a++){
      for (int c=a+1; c<p-2*a+1; c++){
        int b_exp_sq = (p - a - c) * (p - a - c);
        int real_b_sq = c * c - a * a;
        if (b_exp_sq == real_b_sq) freqs[p]++;
      }
    }
  }
  int pos = max_element(freqs.begin(), freqs.end()) - freqs.begin();
  cout << pos << endl;
}
