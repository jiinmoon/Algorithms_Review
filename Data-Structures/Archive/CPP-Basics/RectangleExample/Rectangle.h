/*
 * =====================================================================================
 *
 *       Filename:  Rectangle.h
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  08/18/2020 07:47:14 PM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Ji-In Moon (jmoon), jmoon@jiinmoon.com
 *        Company:  
 *
 * =====================================================================================
 */
#ifndef REACTANGLE_H
#define REACTANGLE_H

class Rectangle
{
    private:
        int length;
        int width;
    public:
        Rectangle() { length = width = 1; };
        Rectangle(int l, int w);
        void setLength(int l);
        void setWidth(int w);
        int area();
        ~Rectangle();   // deconstructor
}; 

#endif
