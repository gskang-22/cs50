#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./recover IMAGE");
        return 1;
    }

    file *F = fopen(argv[1], "r");
    fread(###.jpg, 512, (sizeof(F)/512), F);
    if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
    {

    }
    sprint(filename, "%03i.jpg", count);
    FILE *img = fopen(filename, "w");
}