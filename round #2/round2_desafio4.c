#include <stdio.h>

void main()
{
  int n_cases = 0;

  scanf("%d\n", &n_cases);
  int results[n_cases];

  for (int i = 0; i < n_cases; i++)
  {
    int a, b, c;  

    scanf("%d", &a);
    scanf("%d", &b);
    scanf("%d", &c);

    int num = (a * b) + c;
    int digit_sum = 0;

    while (num > 0) {
      digit_sum += num % 10;
      num = num / 10;
    }
  
    results[i] = digit_sum;
  }

  for (int j = 0; j < n_cases; j++)
  {
    printf("%d ", results[j]);
  }

  printf("\n");
}
