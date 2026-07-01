def two_sum(arr:list[int], target:int)->list[int]:
    num_to_index = {} # this is going to store each number we see along with it index so we can look up at it later.

    for i , num in enumerate(arr):  # then we loop over the array, using enumerate, which gives us both the index I and current number.
        complement = target - num  # at each step we calculate the complement.The number well need to pair with num to hit the target.

        if complement in num_to_index: # if we have seen it .
            return [num_to_index[complement], i]

        num_to_index[num] = i # if we haven't seen it yet, we store the current num in the map with its index. so we can access later.
    return []
# by doing this we are looping through the array once and at each step we are doing constant lookups and inserts. Making the whole thing super efficient.

if __name__ == "__main__":
    arr = list(map(int, input().strip().split()))
    target = int(input())
    res = two_sum(arr, target)
    print("".join(map(str, res)))