
```
    left, res = 0, 0
    count = dict()
    for i in range(arr):
        char = arr[i]
        while (len(count) > k):
            char_remove = arr[left]
            if count[char_remove] == 0:
                count.remove(char_remove)
            left += 1
        res = max(res, i-left+1)
```
