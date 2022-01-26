#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define max_n 2005
#define max_C 2005

int dp[max_n][max_C];

void print_dp() {
  int i, j;

  printf("Matrix best =\n");
  for (i = 0; i < 10; i++) {
    for (j = 900; j <= 1010; j++) {
      printf("%d\t", dp[i][j]);
    }
    printf("\n");
  }
}

int max(int a, int b) {
  return a > b ? a : b;
}

void walrus(int n, int* W) {
  int i, j, best, best_dist, dist;

  if (n == 1){
    printf("%d\n", W[i]);
    return;
  }

  for (i = 0; i <= n; i++)
    for (j = 0; j < max_C; j++)
      dp[i][j] = -1;

  best = 0;
  best_dist = 1000;

  for (i = 0; i <= n; i++)
    for (j = 0; j < max_C; j++)
    {
      if (i == 0 || j == 0)
        dp[i][j] = 0;

      else if (j >= W[i - 1])
        dp[i][j] = max(dp[i-1][j], dp[i-1][j - W[i-1]] + W[i-1]); // weight and value are the same

      else
        dp[i][j] = dp[i-1][j];

      dist = fabs(1000 - dp[i][j]);
      if (dist < best_dist ||
         (dist == best_dist && dp[i][j] > best))
      {
          best = dp[i][j];
          best_dist = dist;
      }
    }

    printf("%d\n", best);
}

int main() {
  int n, i;
  scanf("%d\n", &n);

  int* W = calloc(n, sizeof(int));

  for (i = 0; i < n; i++)
    scanf("%d\n", &W[i]);

  walrus(n, W);
  free(W);
}
