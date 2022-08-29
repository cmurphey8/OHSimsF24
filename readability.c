#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

// function prototypes
int count_letters(string text);
int count_sentences(string text);
int count_words(string text);

// init counts
int sentences=0;
int words=1;
int letters=0;
int ch;

int main(void)
{
    // prompt user for input string
    string text = get_string("Text: ");

    // get counts
    count_letters(text);
    count_sentences(text);
    count_words(text);

    // compute index
    float L = letters * 100 / words;
    float S = sentences * 100 / words;

    float index = round( 0.0588 * L - 0.296 * S - 15.8);

    // compare index
    if(index < 1)
    {
        printf("Before Grade 1\n");
    }

    else if(index >= 1 && index < 16)
    {
        printf("Grade %.0f\n", index);
    }

    else
    {
        printf("Grade 16+\n");
    }
}

int count_words(string text)
{
    for(int i = 0; i < strlen(text); i++)
    {
        if(isspace(text[i]))
        {
            words++;
        }
    }
    return words;
}

int count_letters(string text)
{
    for(int i = 0; i < strlen(text); i++)
    {
        ch = text[i];
        if ((ch >= 65 && ch <= 90) || (ch >= 97 && ch <= 122))
        {
            letters++;
        }
    }
    return letters;
}

int count_sentences(string text)
{
    for(int i = 0; i < strlen(text); i++)
    {
        ch = text[i];
        if (ch == 33 || ch == 46 || ch == 63)
        {
            sentences++;
        }
    }
    return sentences;
}
