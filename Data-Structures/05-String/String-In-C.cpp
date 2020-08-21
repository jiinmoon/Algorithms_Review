/*
 * =====================================================================================
 *
 *       Filename:  String-In-C.cpp
 *
 *    Description:  Exercise of manipulating char[] in C.
 *
 *        Version:  1.0
 *        Created:  08/21/2020 10:04:51 AM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Ji-In Moon (jmoon), jmoon@jiinmoon.com
 *        Company:  
 *
 * =====================================================================================
 */

#include <stdio.h>


int lengthOfString(const char *s)
{
    int total (0);
    for (int i = 0; s[i] != '\0'; ++i)
        total++;
    return total;
}

void toUpper(char *s)
{
    for (int i = 0; s[i] != '\0'; ++i)
    {
        if (97 <= s[i] && s[i] <= 122)
            s[i] -= 32;
    }
}

int wordCount(char *s)
{
    int wc (1);
    for (int i = 0; s[i] != '\0'; ++i)
    {
        if (i > 0 && s[i] == ' ' && s[i-1] != ' ')
            wc++;
    }
    return wc;
}

void revString(char s[], int end)
{
    int start (0);
    while (start < end)
    {
        char temp = s[start];
        s[start++] = s[end];
        s[end--] = temp;
    }
}

bool isPalindrome(char s[], int end)
{
    int start(0);
    while (start <= end)
        if (s[start++] != s[end--])
            return false;
    return true;
}

int main()
{
    const char *pname = "Doomsday";
    printf("%s - %d\n", pname, lengthOfString(pname));    
    char name[] = "MFDoom";
    toUpper(name);
    printf("%s \n", name);
    char msg[] = "This   is a   great string";
    printf("%s -- %d\n", msg, wordCount(msg));
    revString(msg, lengthOfString(msg)-1);
    printf("Reversed : %s\n", msg);
    char pal1[] = "OtootO";
    //char pal2[] = "asdawf";
    if (isPalindrome(pal1, lengthOfString(pal1)-1))
        printf("It is palindrome\n");
    else
        printf("It is not palindrome\n");
    return 0;
}
