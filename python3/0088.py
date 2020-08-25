
from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
            return

        if n == 0:
            return

        ptr = m + n - 1
        p1, p2 = m - 1, n - 1
        while True:
            if nums1[p1] > nums2[p2]:
                nums1[ptr] = nums1[p1]
                p1 -= 1
            else:
                nums1[ptr] = nums2[p2]
                p2 -= 1
            ptr -= 1

            if p1 == -1 or p2 == -1 or ptr == -1:
                break
        
        if p1 == -1 and p2 != -1:
            while ptr >= 0:
                nums1[ptr] = nums2[p2]
                ptr -= 1
                p2 -= 1

        return


def testMerge():
    test_case = [
        {
            'nums1': [1,2,3,0,0,0],
            'm': 3,
            'nums2': [2, 5, 6],
            'n': 3
        },
    ]

    print('----------------- Test ------------------')
    solu = Solution()
    for v in test_case:
        solu.merge(v['nums1'], v['m'], v['nums2'], v['n'])
        print(v['nums1'])


if __name__ == '__main__':
    testMerge()
