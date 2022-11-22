#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int x = (int)round((image[i][j].rgbtRed + image[i][j].rgbtGreen + image[i][j].rgbtBlue) / 3.0);

            image[i][j].rgbtRed = x;
            image[i][j].rgbtGreen = x;
            image[i][j].rgbtBlue = x;
        }
    }
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int x = image[i][j].rgbtRed;
            int y = image[i][j].rgbtGreen;
            int z = image[i][j].rgbtBlue;

            if (round(0.393 * x + 0.769 * y + 0.189 * z) > 255)
            {
                image[i][j].rgbtRed = 255;
            }
            else
            {
                image[i][j].rgbtRed = round(0.393 * x + 0.769 * y + 0.189 * z);
            }

            if (round(0.349 * x + 0.686 * y + 0.168 * z) > 255)
            {
                image[i][j].rgbtGreen = 255;
            }
            else
            {
                image[i][j].rgbtGreen = round(0.349 * x + 0.686 * y + 0.168 * z);
            }

            if (round(0.272 * x + 0.534 * y + 0.131 * z) > 255)
            {
                image[i][j].rgbtBlue = 255;
            }
            else
            {
                image[i][j].rgbtBlue = round(0.272 * x + 0.534 * y + 0.131 * z) ;
            }
        }
    }
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j= 0; j < width / 2; j++)
        {
            RGBTRIPLE temp;
            temp = image[i][j];
            image[i][j] = image[i][width - j];
            image[i][width - j] = temp;
        }
    }
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp[height][width];
    for (int i = 1, i < height - 1; i++)
    {
        for (int j = 1; j < width - 1; j++)
        {
            for (int k = -1; k < 2; k++)
            {
                for (int l = -1; l < 2; l++)
                {
                    int totalr += image[i + k][j + l].rgbtRed;
                    int totalg += image[i + k][j + l].rgbtGreen;
                    int totalb += image[i + k][j + l].rgbtBlue;
                }
            }

            temp[i][j].rgbtRed = (int)round(totalr / 9.0);
            temp[i][j].rgbtGreen = (int)round(totalg / 9.0);
            temp[i][j].rgbtBlue = (int)round(totalb / 9.0);
        }
    }

    for (int i = 0, i < height; i++)
    {
        
    }
}
