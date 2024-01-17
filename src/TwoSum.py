class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num=sorted(nums)
        ans=list()
        i = 0
        j = len(nums)-1
        temp=0

        while i <= j:
            temp=i
            if (num[i] + num[j] == target):
                if (num != nums):
                    temp = nums.index(num[i])
                    if (num[i] == num[j]):
                        nums[temp]=-1
                    j = nums.index(num[j])
                ans.append(temp)
                ans.append(j)
                break
            elif (num[i] + num[j] < target):
                    i=i+1
            else:
                    j=j-1
        return ans