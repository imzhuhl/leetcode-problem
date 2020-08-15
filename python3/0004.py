"""
nums1 = [1, 4, 5, 9, 13, 15, 36, 54]
nums2 = [2, 3, 6, 7, 10]

result is 7.0

NOTE
    例如上述总共 13 个元素，中位数就是第 7 个数字，记为 k
    每次排除 k/2 个元素，然后更新 k 为 k/2，循环逼近

"""


from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        def getKthElem(k: int) -> float:
            n1_left, n2_left = 0, 0

            while True:
                if n1_left == len1:
                    return nums2[n2_left + k - 1]
                elif n2_left == len2:
                    return nums1[n1_left + k - 1]
                elif k == 1:
                    return min(nums1[n1_left], nums2[n2_left])

                idx1 = min(n1_left + k // 2 - 1, len1 - 1)
                idx2 = min(n2_left + k // 2 - 1, len2 - 1)

                if nums1[idx1] <= nums2[idx2]:
                    k = k - (idx1 - n1_left + 1)
                    n1_left = idx1 + 1
                else:
                    k = k - (idx2 - n2_left + 1)
                    n2_left = idx2 + 1


        len1, len2 = len(nums1), len(nums2)
        total_len = len1 + len2

        if total_len % 2 == 1:  # 元素个数是奇数
            return getKthElem((total_len + 1)//2)
        else:
            return (getKthElem(total_len // 2) + getKthElem(total_len//2 + 1)) / 2


def testFindMedianSortedArrays():
    test_case = [
        {
            'nums1': [1, 2],
            'nums2': [-1, 3],
        },
        {
            'nums1': [1, 3],
            'nums2': [2],
        },
        {
            'nums1': [1, 4, 5, 9, 13, 15, 36, 54],
            'nums2': [2, 3, 6, 7, 10],
        },
        {
            'nums1': [],
            'nums2': [1],
        },
        {
            'nums1': [],
            'nums2': [1,2,3,4],
        },
    ]

    print('----------------- Test ------------------')
    solu = Solution()
    for item in test_case:
        rst = solu.findMedianSortedArrays(item['nums1'], item['nums2'])
        print('{}\n{}\nresult = {}\n'.format(item['nums1'], item['nums2'], rst))
        


if __name__ == "__main__":
    testFindMedianSortedArrays()
    
