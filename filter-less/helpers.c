#include "helpers.h"

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int x = (int)(image[i][j].rgbtRed + image[i][j].rgbtGreen + image[i][j].rgbtBlue) / 3.0;

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

            if (((int)(0.393 * x + 0.769 * y + 0.189 * z)) > 255)
            {
                image[i][j].rgbtRed = 255;
            }
            else
            {
                image[i][j].rgbtRed = ((int)(0.393 * x + 0.769 * y + 0.189 * z));
            }

            if (((int)(0.349 * x + 0.686 * y + 0.168 * z)) > 255)
            {
                image[i][j].rgbtGreen = 255;
            }
            else
            {
                image[i][j].rgbtGreen = ((int)(0.349 * x + 0.686 * y + 0.168 * z));
            }

            if (((int)(0.272 * x + 0.534 * y + 0.131 * z)) > 255)
            {
                image[i][j].rgbtBlue = 255;
            }
            else
            {
                image[i][j].rgbtBlue = ((int)(0.272 * x + 0.534 * y + 0.131 * z));
            }
        }
    }
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}
