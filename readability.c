// PROMPT: I'm passing all but one of my check50 tests. How is this even possible??!?!

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

// init vars
int i, ch;
float L, S, index;
string text;

int main(void)
{
    // prompt user for input string
    text = get_string("Text: ");

    // get counts
    count_letters(text);
    count_sentences(text);
    count_words(text);

    // compute index
    L = letters * 100 / words;
    S = sentences * 100 / words;

    index = round( 0.0588 * L - 0.296 * S - 15.8);

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

int count_words(string tmp)
{
    for(i = 0; i < strlen(tmp); i++)
    {
        if(isspace(tmp[i]))
        {
            words++;
        }
    }
    return words;
}

int count_letters(string tmp)
{
    for(i = 0; i < strlen(tmp); i++)
    {
        ch = tmp[i];
        if ((ch >= 65 && ch <= 90) || (ch >= 97 && ch <= 122))
        {
            letters++;
        }
    }
    return letters;
}

int count_sentences(string tmp)
{
    for(i = 0; i < strlen(tmp); i++)
    {
        ch = tmp[i];
        if (ch == 33 || ch == 46 || ch == 63)
        {
            sentences++;
        }
    }
    return sentences;
}
