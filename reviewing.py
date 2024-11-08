#basically me trying to understand this code, so ill be commenting my understanding on this copied code.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numToIndex = {}  # dictionary, with the {}, why? to store values and indices

        for i, num in enumerate(nums):  # looks into the list, enumerate allows you to loop within a sequence
            complement = target - num  # this looks for the complement, so 9-2 = 7, you add to to the dictionary numToIndex, then another iteration goes, so 9(target) - 7(number) = 2, so 7 is added to the dictionary again. It stops here since 2 and 7 already adds up to 9.  

            if complement in numToIndex: #is it in the dictionary? 
                return [numToIndex[complement], i] #t returns a list containing the index of the complement (from numToIndex[complement]) and the current index i. 

            numToIndex[num] = i  
        return [] #the solution is not there 