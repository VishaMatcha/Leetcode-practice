class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:

        n = len(nums)

        res = []

        nums.sort()
        ctr = 0
        for i in range(n//3):
            temp = [nums[ctr]]
            ctr+=1
            for i in range(2):
                if nums[ctr] - temp[0]>k:
                    return []
                temp.append(nums[ctr])
                ctr+=1

            res.append(temp)

        return res