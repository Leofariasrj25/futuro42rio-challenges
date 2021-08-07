// problem: given a line of text, count how many vowels there are on the line. and display it
// what is the worst case scenario? the string has only one vowel at the end of string or it has no vowel
// either way we transversed the entire line to find the vowel.

// what type of characters will be given on the line?
// every single one of them
//
#include <stdio.h>

void main() 
{
  int n_lines = 0;  
  int vowel_count = 0;
  char sentence[256];
  char vowels[] = {'a', 'e', 'i', 'o', 'u', 'y'};

  scanf("%d\n", &n_lines);
  int results[n_lines]; 
  
  for(int i = 0; i < n_lines; i++)
  {
    fgets(sentence, 256, stdin);

    vowel_count = 0;
    int sentence_size = sizeof sentence / sizeof *sentence;
    int vowels_size = sizeof vowels / sizeof *vowels;

    for (int j = 0; j < sentence_size; j++)
    {
      
      for (int y = 0; y < vowels_size; y++)
      {

        if ((char) sentence[j] == (char) vowels[y])
        {
          vowel_count++; 
          break;
        }
      }
    }

    results[i] = vowel_count;
  }
  
  for (int i = 0; i < n_lines; i++) {
    printf("%d ", results[i]);
  }

  printf("\n");
}
