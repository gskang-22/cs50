#include <stdio.h>
#include <stdlib.h>

int BLOCKSIZE = 512;
typedef uint8_t BYTE;
int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./recover IMAGE\n");
        return 1;
    }

    file *F = fopen(argv[1], "r");
    if (F == NULL)
    {
        prinf("Could not open %s.\n", argv[1]);
        return 1;
    }
    uint8_t buffer[BLOCK_SIZE];
    while (fread(buffer, 1, BLOCK_SIZE, F) == BLOCK_SIZE);
    {
         // if jpg file
         if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            fclose();
            counter++;
            fopen();
            fwrite();
        }
        else
        {
            
        }
    }

    sprint(filename, "%03i.jpg", count);
    FILE *img = fopen(filename, "w");
}