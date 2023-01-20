
### Traversal

0. preorder, inorder, postorder
- preorder
```
    def preorder_traversal(root):
        res, stack = [], []
        cur = root
        while stack:
            while cur.left != null:
                res += [cur]
                cur = cur.left

```


- inorder
```
def inorder_traversal(root):
    res, stack = [], []
    cur = root
    while stack or cur:
        while cur:
            stack += [cur]
            cur = cur.left
        cur = stack.pop()
        res += [cur.value]
        cur = cur.right

```


- postorder


1. construct tree:
inorder[0] to be root, use this as root to construct left & right tree, recursively loop down

2. two pointer:

a. remove fron nth: tranverse  1st till k first, then move both till 2nd reach end

b. fast, slow: when fast = slow, rerun fast from head to get the intersaction
`2b + a + c = velocity division * (a + b) `
where a is beginning -> intersaction

![](pics/fastslow.png)
