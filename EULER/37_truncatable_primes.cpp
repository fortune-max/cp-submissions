#include <bits/stdc++.h>
using namespace std;

int sum = 0;
vector<int> next_digits = {1, 3, 5, 7, 9};

bool is_prime(int n){
  if (n < 2) return false;
  for (int i = 2; i*i <= n; i++)
    if (n % i == 0) return false;
  return true;
}

bool is_truncatable_prime(int n){
  if (n < 10) return false;
  for (int i=1; i<=log10(n); i++){
    if (!is_prime(n % (int)pow(10, i))) return false;
    if (!is_prime(n / (int)pow(10, i))) return false;
  }
  return true;
}

void get_next(int root, int next_digit){
  int candidate = root * 10 + next_digit;
  if (is_prime(candidate)){
    if (is_truncatable_prime(candidate)) sum += candidate;
    for (auto next_digit: next_digits) get_next(candidate, next_digit);
  }
}

int main(){
  for (auto root: {2, 3, 5, 7})
    for (auto next_digit: next_digits)
      get_next(root, next_digit);
  cout << sum << endl;
}
