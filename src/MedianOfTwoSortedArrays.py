class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        length = len(nums1) + len(nums2)
        half = length / 2
        one = 0
        two = 0
        count = 0
        final = []
        for i in range(length):
            if (two >= len(nums2)):
                final.insert(count,nums1[one])
                one+=1
                count+=1
                continue
            if (one >= len(nums1)):
                final.insert(count,nums2[two])
                two+=1
                count+=1
                continue
            if (nums1[one] <= nums2[two]):
                final.insert(count,nums1[one])
                one+=1
            else:
                final.insert(count,nums2[two])
                two+=1
            count+=1

        if (half % 1 != 0):
            return float(final[int(half)])

        else:
            sum = final[int(half)] + final[int(half-1)]
            return float(sum/2)