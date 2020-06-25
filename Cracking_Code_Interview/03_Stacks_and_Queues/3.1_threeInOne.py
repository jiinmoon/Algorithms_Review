""" 3.1 Three In One

Question:

    Describe how you could use a single array to implement three stacks.

---

There are different way to go about this but the idea is to divide the fixed
size array into three equal parts that are being kept in track by three
pointers. For example, stack1 will utilize the array cells from 0 to n/3; stack2
will occupify spaces n/3 to 2n/3; and ...

Then, we have a question of whether we wish to grow the stack sizes dynamically
or not. This will add to complexity as we will have to grow the size of the
array and then copying over the elements.

"""
