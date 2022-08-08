#Given an array A of integers return the smallest positive
#integer (greater than 0) that does not occur in A
#Example: A = [1,3,6,4,1,2], the function should return 5
#Example: A = [1,2,3], return 4
#Example: A = [-1,-3], return 1

from itertools import count, filterfalse


def solution(a):
    return(next(filterfalse(set(a).__contains__, count(1))))

#def solution(A):
#   length = len(A)
#   for i in range(1, length + 2)
#       found = False
#       for j in range(length)
#           if A[j] == i:
#               found = True

#def solution(A):
#   a = A
#    hash = set(a)
#    for i in range(1, len(A) + 2):
#        if i not in hash:
#            return i

A = [1,3,6,4,1,2]
print(solution(A))
