
#         1
#        2 3
#       4 5 6
#     7  8 9 10
#   11 12 13 14 15
# 16 17 18 19 20 21
def row_sum_numbers(n):
    # return sum(range((n*2)-(n-(n-1)), n*(n-1)))
    return sum(range(n*(n-1)//2 + 1, n*(n+1)//2+1))
#     The range function in Python doesn't include the stop number in the sequence it generates.
#     So, to include the last number in the nth row (which is n*(n+1)//2),
#     you need to add 1 to the stop number in your range function.


print(row_sum_numbers(3))
print(row_sum_numbers(5))
print(row_sum_numbers(6))
