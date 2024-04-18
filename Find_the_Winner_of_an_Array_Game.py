class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        #T(C(N)==O(N)) and S(C(N)=O(1) as it requires non memory allocation iteratively
        if k==1:return max(arr[0],arr[1])#printing maximum array initial val indx element 
        if k>=len(arr):return max(arr)#printing highest array element
        curr_win=arr[0];consecutive_win=0#initalizing current and consecutive winner
        for i in range(1,len(arr)):#iterating throug array's length
            if curr_win>arr[i]:consecutive_win+=1#incrementing Consecutive winner
            else:curr_win=arr[i];consecutive_win=1#currenet winner position declare
            if consecutive_win==k:return curr_win#printing current winner from consecutive rounds
        return curr_win#printing current winner 
