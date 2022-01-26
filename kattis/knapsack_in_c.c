#include <stdio.h>
#include <stdlib.h>

#define max_C 2005
#define max_n 2005

int best[max_n][max_C];

void print_list(int* ls, int n) {
  for (int i = 0; i < n; i++)
    printf("%d ", ls[i]);
  printf("\n");
}

void print_best(int C, int n) {
  int i, j;

  printf("Matrix best =\n");
  for (i = 0; i < n+5; i++) {
    for (j = 0; j <= C+1; j++) {
      printf("%d\t", best[i][j]);
    }
    printf("\n");
  }
}

int max(int a, int b) {
  return a > b ? a : b;
}

void knapsack(int C, int n, int* V, int* W) {
  int i, j;

  for (i = 0; i < n; i++)
    scanf("%d %d\n", &V[i], &W[i]);

  for (i = 0; i <= n; i++)
    for (j = 0; j <= C; j++)
      best[i][j] = -1;

  for (i = 0; i <= n; i++)
    for (j = 0; j <= C; j++){
      if ( i == 0 ||j == 0 )
        best[i][j] = 0;
      else if (j >= W[i-1])
        best[i][j] = max(best[i-1][j], best[i-1][j - W[i-1]] + V[i-1]);
      else
        best[i][j] = best[i-1][j];
    }
}

void knapsack_construct(double c, int n) {
  int i, j, best_cap, ans_ind;

  int* V = calloc(n+5, sizeof(int));
  int* W = calloc(n+5, sizeof(int));

  int C = (int) c;
  knapsack(C, n, V, W);

  print_best(C, n);
  // printf("list V = "); print_list(V, n);
  // printf("list W = "); print_list(W, n);

  best_cap = C;
  ans_ind = 0;
  int ans[max_n];

  for (i = n; i > 0; i--) {
    if(best[i][best_cap] != best[i-1][best_cap]) {
      ans[ans_ind] = i-1;
      ans_ind++;
      best_cap -= W[i-1];
    }
  }

  printf("%d\n", ans_ind);
  for (i = 0; i < ans_ind; i++)
    printf("%d ", ans[i]);
  printf("\n");

  free(V);
  free(W);
}

int main() {
  double c;
  int n;
  while (scanf("%lf %d\n", &c, &n) != EOF)
    knapsack_construct(c, n);
  return 0;
}
