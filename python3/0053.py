
def max_subarr(nums):
    length = len(nums)
    rst = nums[0]
    curr_sum = nums[0]
    for i in range(1, length):
        if curr_sum > 0:
            curr_sum += nums[i]
        else:
            curr_sum = nums[i]
        
        if curr_sum > rst:
            rst = curr_sum
    
    return rst



if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(max_subarr(nums))