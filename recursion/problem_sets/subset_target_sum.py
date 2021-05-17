"""
Problem Statement: Given a set of integers and a target value k, 
                    find a non-empty subset that sums up to k.
                    Return True if possible, False if not
"""

def target_sum(arr, k):

    result = []

    def helper(slate, pick, sum_):
        
        
        if sum_ == k and pick > 0:
            result.append(1)
            return

        # Base case
        if pick == len(arr):
            return

        for index in range(pick, len(arr)):
            slate.append(arr[index])
            helper(slate, index + 1, sum_ + arr[index])
            slate.pop()

    helper([], 0, 0)
    if any(result) == 1:
        return True
    return False

        

if __name__ == "__main__":
    arr = [2, 4, 6]
    k = 5
    print(target_sum(arr, k))