#include <bits/stdc++.h>
using namespace std;

string calc_pandigital(int n){
  string ans = "";
  int multiplier = 0;
  while (ans.length() < 9) {
    multiplier += 1;
    ans += to_string(n * multiplier);
    if (ans.length() >= 9){
      string ans_copy = ans;
      sort(ans_copy.begin(), ans_copy.end());
      if (ans_copy == "123456789") return ans;
      return "0";
    }
  }
  return "0";
}

bool is_achievable(string pandigital){
  for (int n_width=1; n_width<6; n_width++){
    int seed = stoi(pandigital.substr(0, n_width));
    if (calc_pandigital(seed) == pandigital) return true;
  }
  return false;
}

int main(){
  string pandigital_candidate = "987654321";
  do {
    if (is_achievable(pandigital_candidate)){
      cout << pandigital_candidate << endl;
      break;
    }
  } while (prev_permutation(pandigital_candidate.begin(), pandigital_candidate.end()));
}
