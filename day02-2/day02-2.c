#include <stdio.h>
#include <string.h>
#include <stdlib.h>

/*

A for Rock, B for Paper, and C for Scissors.
X for lose, Y for draw, and Z for win.

Your total score is the sum of your scores for each round. 
The score for a single round is the score for the shape you selected 
(1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome 
of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

points[move1-'A'][move2-'X']

A X 3 + 0 = 3
A Y 1 + 3 = 4
A Z 2 + 6 = 8

B X 1 + 0 = 1
B Y 2 + 3 = 5
B Z 3 + 6 = 9

C X 2 + 0 = 2
C Y 3 + 3 = 6
C Z 1 + 6 = 7

A Y 4
B X 1
C Z 7
*/

int main(void)
{
char s[10];
int sum;

int points[3][3] = {
{    3, 4, 8 },    //  AX AY AZ
{    1, 5, 9 },    //  BX BY BZ
{    2, 6, 7 }     //  CX CY CZ
};

FILE * f = fopen("input.txt", "r");
int line_count = 0;
while (!feof(f))
{   
    if (fgets(s, sizeof(s), f) != NULL)
    {
        sum += points[s[0]-'A'][s[2]-'X'];
        line_count++;
    }
}

printf("line_count = %d\n", line_count);
printf("sum = %d\n", sum);

fclose(f);

return 0;

}

