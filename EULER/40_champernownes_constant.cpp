#include <bits/stdc++.h>
using namespace std;

int num_length(int num){
  return to_string(num).length();
}

int count_digits(int stop, int start=1){
  if (num_length(start) == num_length(stop))
    return (stop - start + 1) * num_length(start);
  int next_10_pow = pow(10, num_length(start));
  return count_digits(next_10_pow - 1, start) + count_digits(stop, next_10_pow);
}

int get_digits(int n){
  int low(1), high(190000);
  while (high - low > 1){
    int mid = (high + low) / 2;
    if (count_digits(mid) > n) high = mid;
    else low = mid;
  }
  int extra = n - count_digits(low);
  string cat = to_string(low%10) + to_string(high);
  return stoi(cat.substr(extra, 1));
}

int main(){
  int ans = 1;
  for (int i=0; i<7; i++) ans *= get_digits(pow(10, i));
  cout << ans << endl;
}
