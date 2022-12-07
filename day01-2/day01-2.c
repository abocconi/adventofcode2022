#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(void)
{
char s[20];
int sum = 0;
int max_sum[3] = {0, 0, 0};
int max_pos[3] = {0, 0, 0};
int min_index = 0;
int line_count = 0;

FILE * f = fopen("input.txt", "r");

while (!feof(f))
{   
    if (fgets(s, 20, f) != NULL)
    {
        line_count++;

        if (strlen(s) > 1)
        {
            sum += atoi(s);
        }
        else
        {            
            // sostituisco eventualmente il minore
            if (sum > max_sum[min_index])
            {
                max_sum[min_index] = sum;
                max_pos[min_index] = line_count;

                // cerco il nuovo minore
                min_index = 0;
                int min_sum = max_sum[0];

                for (int i = 1; i < 3; i++)
                {
                    if (min_sum > max_sum[i])
                    {
                        min_sum = max_sum[i];
                        min_index = i;
                    }
                }

            }
            sum = 0;
        }

    }
}

printf("max sum = %d @%d, %d, %d\n", max_sum[0]+max_sum[1]+max_sum[2], max_pos[0], max_pos[1], max_pos[2]);
return 0;

}

