#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(void)
{
char s[20];
int sum = 0;
int max_sum = 0;
int max_pos = 0;
int line_count;

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
            if (max_sum < sum)
            {
                max_sum = sum;
                max_pos = line_count;
            }
            sum = 0;
        }

    }
}

printf("max sum = %d @ %d\n", max_sum, max_pos);
return 0;

}