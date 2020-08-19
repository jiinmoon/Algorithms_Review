/*
 * =====================================================================================
 *
 *       Filename:  Rectangle.c
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  08/18/2020 07:52:29 PM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Ji-In Moon (jmoon), jmoon@jiinmoon.com
 *        Company:  
 *
 * =====================================================================================
 */

#include "Rectangle.h"

Rectangle::Rectangle(int l, int w)
{
    length = l;
    width = w;
}

void Rectangle::setLength(int l) { length = l; }
void Rectangle::setWidth(int w) { width = w; }
int Rectangle::area() { return width * length; }
Rectangle::~Rectangle() {};
