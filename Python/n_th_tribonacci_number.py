# Problem Statement

##
# The Tribonacci sequence Tn is defined as follows: 
# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
# Given n, return the value of Tn.
##

class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n <= 2:
            return 1
        
        res_arr = [0]*(n+1)
        res_arr[1] = res_arr[2] = 1
        
        for i in range(n - 3 + 1):
            res_arr[i+3] = res_arr[i] + res_arr[i+1] + res_arr[i+2]
            
        return res_arr[n]