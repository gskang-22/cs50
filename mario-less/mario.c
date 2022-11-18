#include <cs50.h>
#include <stdio.h>

int main(void)
{
    do
    {
        int n = get_int("Height: ");
    }
    while
    {
        n < 1 OR n > 8;
    }
}