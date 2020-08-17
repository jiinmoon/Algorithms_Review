/*
 * =====================================================================================
 *
 *       Filename:  calculator.cpp
 *
 *    Description:  Uses stack for postfix computation. 
 *
 *        Version:  1.0
 *        Created:  08/16/2020 10:20:35 PM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Ji-In Moon (jmoon), jmoon@jiinmoon.com
 *        Company:  
 *
 * =====================================================================================
 */

#include <iostream>
#include <string>

#include "arraystack.h"

using namespace std;

// curr char a digit?
bool isDigit (char c)
{
    // char is a unicode
    // '0' == 48, '1' == 49, ... , '9' == 57
    return (c >= '0' && c <= '9');
}

// curr char an operator?
bool isOp (char c)
{
    return (c == '+' || c == '-' || c == '*' 
            || c == '/' || c == '(' || c == ')');
}

// determine precedence
int getPrecedence (char c)
{
    switch (c)
    {
        case '+': 
        case '-':
            return 1;
        case '*':
        case '/':
            return 2;
        case '(':
        case ')':
            return 3;
        default:
            return -1;
    }
}

int operate (int v1, int v2, char op)
{
    if (op == '+') return v1 + v2;
    if (op == '-') return v1 - v2;
    if (op == '*') return v1 * v2;
    return (int) v1 / v2;
}

int evaluate (string s)
{
    stack<int> vals;
    stack<char> ops;

    int val = 0;
    size_t pos = 0;

    while (pos < s.length())
    {
        char curr = s[pos];
        if (isDigit(curr))
            val = (val * 10) + (int)(curr - '0');
        else if (isOp(curr))
        { 
            // edge case 1: open paren
            if (curr == '(')
            {
                ops.push(curr);
                val = 0;
            }
            // edge case 2: is first number?
            else if (vals.isEmpty())
            {
                vals.push(val);
                ops.push(curr);
                val = 0;
            }
            // edge case 3: closed paren
            else if (curr == ')')
            {
                // must have been open paren before
                vals.push(val); 
                while (ops.peek() != '(')
                {
                    curr = ops.pop();
                    val = vals.pop();
                    int prev = vals.pop();
                    val = operate(prev, val, curr);
                    vals.push(val);
                }
                ops.pop();
                vals.pop();
            }
            else
            {
                // new operator encountered at this point
                // compute previous operator
                char prev = ops.peek();
                // is current precedence higher?
                if (getPrecedence(curr) > getPrecedence(prev))
                {
                    vals.push(val);
                    ops.push(curr);
                    val = 0;
                }
                // now, we need to compute before curr can go on stk
                else
                {
                    int prevVal = vals.pop();
                    int prevOp = ops.pop();
                    prevVal = operate(prevVal, val, prevOp);
                    vals.push(prevVal);
                    ops.push(curr);
                    val = 0;
                }
            }
        }
        pos ++;
    }

    while (!ops.isEmpty())
    {
        int prev = vals.pop();
        char op = ops.pop();
        val = operate(prev, val, op);
    }
    return val;
}
