#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// some how need to select the select the population with the largest
// "population/nbr of ballot boxes"

int max(int a, int b) {
  return a > b ? a : b;
}

void distribute(int N, int B) {
  int i, lo = 0, hi = 0, mid, M;
  int* a;

  a = calloc(N, sizeof(int));
  for (i = 0; i < N; i++) {
    scanf("%d\n", &a[i]);
    hi = max(a[i], hi);
  }

  while (lo < hi) {
    mid = (hi + lo) / 2;

    M = 0;
    for (i = 0; i < N; i++) {
      // M += ceil(a[i] / mid);
      M += (a[i] + mid - 1) / mid;
    }

    if (M > B)
      lo = mid + 1;
    else
      hi = mid;
  }

  printf("%d\n", lo);
  free(a);
}

int main() {
  // N = nbr of cities
  // B = nbr of ballots
  int N, B;

  scanf("%d %d\n", &N, &B);
  while(!(N == -1 && B == -1))
  {
    distribute(N, B);
    scanf("%d %d\n\n", &N, &B);
  }
}
