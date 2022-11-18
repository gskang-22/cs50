#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

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

    int k = atoi(argv[1]);
    string s = get_string("plaintext: ");
    int len = strlen(s);

    printf("ciphertext: ");
    for (int i = 0; i < len; i++)
    {
        char c = rotate(s[i], k);
        printf("%c", c);
    }
    printf("\n");
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
    if (!(isalpha(char1)))
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