# import sys
# for line in sys.stdin:
#     a = line.split()
#     a, b = a[0], a[1]
#     c, d = int(a[::-1]), int(b[::-1])
#     Sum = c + d
#
#     print(str(Sum)[::-1].strip('0'))
#     # print(int(a[0]) + int(a[1]))


import sys
if __name__ == "__main__":
    def checkPossibility(nums):
        modified,prev=False,nums[0]
        for i in range(1,len(nums)):
            if prev>nums[i]:
                if modified:
                    return False
                if i-2<0 or nums[i-2]<=nums[i]:
                    prev=nums[i]
                modified=True
            else:
                prev=nums[i]
        return True
    # 读取第一行的n
    # n = int(sys.stdin.readline().strip())
    # ans = 0
    # for i in range(n):
    #     # 读取每一行
    #     line = sys.stdin.readline().strip()
    #     # 把每一行的数字分隔后转化成int列表
    #     values = list(map(int, line.split()))
    n = int(input())
    arr = [int(i) for i in input().strip().split()]
    tag=checkPossibility(arr)
    if tag==1:
        print('yes')
    else:
        print('no')

