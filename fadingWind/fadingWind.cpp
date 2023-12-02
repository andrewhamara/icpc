#include <iostream>
#include <algorithm>

using namespace std;

int main() {
  int h,k,v,s;
  cout << "Enter the numbers: ";
  cin >> h >> k >> v >> s;

  int dist = 0;

  while (h > 0) {
    v += s;
    v -= max(1, v / 10);
    if (v >= k) { h++;}
    if (0 < v && v < k) {
      h--;
      if (h == 0) {v = 0;}
    }
    if (v <= 0) {h = 0; v = 0;}
    dist += v;
    if (s > 0) {s--;}
  }

  cout << dist << endl;
  return dist;
}
