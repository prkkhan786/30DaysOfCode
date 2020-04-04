

class Solutiion:
    '''

    Given a non-empty array of integers, every element appears twice except for one. Find that single one.

    Note:

    Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

    Example 1:

    Input: [2,2,1]
    Output: 1


    '''


    def singleNumber(self, nums):
        dictionary = {}
        for val in nums:
            if val not in d:
                dictionary[val] = 1
            else:
                dictionary[val] = dictionary.get(val) + 1
        for val in nums:
            if (dictionary.get(i) == 1):
                return val
        '''Another approach using xor
        
            """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for i in nums:
            a ^= i
        return a
        
        '''


    def isHappy(self,n):

        '''

        Write an algorithm to determine if a number is "happy".

        A happy number is a number defined by the following process: Starting with any positive integer,
        replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1
        (where it will stay), or it loops endlessly in a cycle which does not include 1.
        Those numbers for which this process ends in 1 are happy numbers.

        Input: 19
        Output: true
        Explanation:
        12 + 92 = 82
        82 + 22 = 68
        62 + 82 = 100
        12 + 02 + 02 = 1

        '''


        try:

            set_dictionary = []
            set_dictionary.append(n)
            while(n!=1):
                newdigit = 0
                digitString = str(n)
                digits = [int(digit) for digit in digitString]

                for i in digits:
                     newdigit = newdigit + (i * i)
                if(newdigit in set_dictionary):
                    return False
                set_dictionary.append(newdigit)
                n = newdigit
            return True
        except:
            return False




    def maxSubArray(self,nums):
        '''  Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

            Example:
            Input: [-2,1,-3,4,-1,2,1,-5,4],
            Output: 6
            Explanation: [4,-1,2,1] has the largest sum = 6.
        '''
        currentSum = nums[0]
        overallSum = nums[0]

        for i in range(1,len(nums)):

            if(currentSum<0):
                currentSum = nums[i]
            else:
                currentSum = currentSum + nums[i]

            if(overallSum<currentSum):
                overallSum = currentSum
        return overallSum






c = Solutiion()
print(c.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

