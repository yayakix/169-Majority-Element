class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict = {}
        for x in range(len(nums)):
            if nums[x] in dict:
                dict[nums[x]] += 1
            else:
               dict[nums[x]] = 1
        # sort the dict and return the greatest count
        # Turn dict into array using .items()
        #use the sorted 
        arr_dict = dict.items()
        sorted_dict = sorted(arr_dict, key = lambda x: x[1], reverse= True)
        return sorted_dict[0][0]
