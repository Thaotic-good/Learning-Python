def triangular_numb(n):
    # return sum(range(1, n+1))
    return n*(n+1)//2
#  how sum is done in maths: ∑i=m^n i = (n-m+1)(m+n)/2
    # ∑i=m^n i :       This is the notation for the sum of all integers i from m to n.
    # (n-m+1)(m+n)/2 : This is the formula to calculate that sum.
    # sum 3 to 5, we get (5-3+1)(3+5)/2 = 3*8/2 = 12, which is the correct sum (3 + 4 + 5 = 12)


print(triangular_numb(3))
print(triangular_numb(5))

# na com robime?
# The 1st triangular number is 1 (1)
# The 2nd triangular number is 3 (1+2)
# The 3rd triangular number is 6 (1+2+3)
# The 4th triangular number is 10 (1+2+3+4)
# The 5th triangular number is 15 (1+2+3+4+5)
# and so on...