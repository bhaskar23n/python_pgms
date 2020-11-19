def max_sum_subarray(arr):
    size=len(arr)
    curr_sum=0
    max_so_far=arr[0]
    st=0;en=0;poi=0
    for i in range(0,size):
        curr_sum=curr_sum+arr[i]

        if(max_so_far<curr_sum):
            max_so_far=curr_sum
            st=poi
            en=i
        if(curr_sum<0):
            curr_sum = 0
            poi=i+1

    print("Maximum sum Subarray is",max_so_far)
    print("Start Index of window is",st)
    print("End Index of window is",en)
arr=[4,5,0,-2,-3,2,5,-6,-8,-4,-2,-9]
max_sum_subarray(arr)