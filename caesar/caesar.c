#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

bool only_digits(string);
int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    else if (!(only_digits(argv[1])))
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    else if (argc == 2)
    {
        return 0;
    }
    int k = (int)(argv[1][0]);
}

bool only_digits(string string1)
{
    int len = strlen(string1);
    if (len > 1)
    {
        return false;
    }
    else if (!(isdigit(string1[0])))
    {
        return false;
    }
    else
    {
        return true;
    }
}
