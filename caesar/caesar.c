#include <cs50.h>
#include <stdio.h>

bool only_digits(string);
int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    else if (argc == 2)
    {
        return 0;
    }
}

bool only_digits(string string1)
{
    if (int strlen(string1) > 1)
    {
        return false;
    }
    else if not (isdigit(string1))
    {
        return false;
    }
    else
    {
        return true;
    }
}
