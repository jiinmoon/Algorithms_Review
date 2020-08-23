/*
 * =====================================================================================
 *
 *       Filename:  main.cpp
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  08/21/2020 01:22:40 PM
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

using std::string;

class ListNode
{
    public:
        int val;
        ListNode *next;

        ListNode(int data=0);
};

ListNode::ListNode(int data)
{
    val = data;
    next = NULL;
};

class LinkedList
{
    private:
        ListNode *head;
        ListNode *tail;
        int listsize;
    public:
        LinkedList();
        LinkedList(const int A[], const int arraysize);
        ~LinkedList();

        void append(int val);
        int pop();

        int size();
        string toString();
};

/* default empty constructor */
LinkedList::LinkedList() {};

/* initialize with given int array */
LinkedList::LinkedList(const int A[], const int arraysize)
{
    if (arraysize != 0) 
    {
        head = new ListNode(A[0]);
        ListNode *curr = head;
        for (int i = 1; i < arraysize; ++i)
        {
            curr->next = new ListNode(A[i]);
            curr = curr->next;
        }
        listsize = arraysize;
    }
}

LinkedList::~LinkedList()
{
    while (head != NULL)
    {
       ListNode *t = head;
       head = head->next;
       delete t;
    }
}

void LinkedList::append(int val)
{
    if (listsize == 0)
    {
        head = new ListNode(val);
        tail = head;
    } else {
        tail->next = new ListNode(val);
        tail = tail->next;
    }
    listsize++;
}

int LinkedList::pop()
{
    if (listsize > 0)
    {
        ListNode *curr = head;
        while (curr->next != tail)
            curr = curr->next;
        ListNode *popNode = curr->next;
        curr->next = NULL;
        tail = curr;
        int res = popNode->val;
        delete popNode;
        listsize--;
        return res;
    }
    return -1;
}

string LinkedList::toString()
{
    string result = "";
    ListNode *curr = head;
    while (curr != NULL)
    {
        result += std::to_string(curr->val);
        if (curr->next != NULL)
        {
            result += ", ";
        }
        curr = curr->next;
    }
    return result;
}

int LinkedList::size() { return listsize; }


int main()
{
    int a[] = {1,2,3,4,5};
    ListNode node1;
    ListNode node2(10); 
    std::cout << node1.val << std::endl;
    std::cout << node2.val << std::endl;
    LinkedList l1(a, 5);
    std::cout << l1.toString() << std::endl;
    LinkedList l2;
    l2.append(5);
    l2.append(10);
    l2.append(22);
    std::cout << l2.toString() << std::endl;
    std::cout << l2.pop() << std::endl;
    l2.append(77);
    std::cout << l2.toString() << std::endl;

    return 0;
}
