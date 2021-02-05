""" 231. Power of Two

Solution:

    To determine whether the number is power of two, firstly we could of course,
    check whether the number is even or odd. Then, in naive approach, we could
    repeatedly divide the number by 2. Or, it maybe possible to treat this as a
    binary search to help reduce time.

    But we can easily find out whether a number is even or not using bit
    operations. All the powers of two in binary format has a distinctive feature
    - that is in binary representation, power of twos have a single bit turned
      on. This is not surprsing since binary representation is essentially 2**n
      + 2**n-1 + ... + 2**0.

    Then, if the given number is the even, we can assume that by taking away 1
    from the given number, the number turns into odd number; in fact, this odd
    number will have all the bits turned on execpt the highest bit.

    Hence, the **even** given number has a single bit turned on at the highest
    position, whereas **odd** number has all bits turned on except at the
    highest position. Meaning that if the given number truly was even, then the
    AND bit operation between two should results in 0.

"""

class Solution:
    def isPowerOfTwo(self, n):
        if n <= 0:
            return False
        return not n & (n - 1)
