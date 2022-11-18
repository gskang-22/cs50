#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

bool only_digits(string);
char rotate(char, int);
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
        string s = get_string("plaintext: ");
    }

    int k = (int)(argv[1][0]);
    int len = strlen(s);

    for (int i = 0; i < len; i++)
    {
        rotate(s[i], k);
    }

    printf("ciphertext: %s", s);
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

char rotate(char char1, int int1)
{
    if (isalpha(char1) == 0)
    {
        return char1;
    }
    else if (isupper(char1))
    {
        char1 = (char1 - 'A' + int1)%26;
        return char1;
    }
    else
    {
        char1 = (char1 - 'a' + int1)%26;
        return char1;
    }
}