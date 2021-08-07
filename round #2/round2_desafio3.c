// Round #2 - Desafio 3 - FizzBuzz (com bônus)

#include <stdio.h>
#include <stdbool.h>

void main() 
{
  
  int count_3 = 0;
  int count_5 = 0;
  int limit = 101;
  char fizz[] = "Fizz";
  char buzz[] = "Buzz";
  bool flag = false;

  for(int i = 1; i < limit; i++)
  {
    flag = false;
    count_3++;
    count_5++;

    if (count_3 == 3) {
      printf(fizz);
      count_3 = 0;
      flag = true;
    }
    
    if (count_5 == 5) {
      printf(buzz);
      count_5 = 0;
      flag = true;
    }

    if (!flag)
    {
      printf("%d", i);
    }
    
    printf("\n");
  }
}
