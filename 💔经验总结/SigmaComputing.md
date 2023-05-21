order clients join heap


https://www.1point3acres.com/bbs/thread-858712-1-1.html


实现一个spreadsheet，有finite column和infinite rows, 需要实现set, get和printFirstNLine, 如果没有赋值当做0，需要加unit test
Example:
spreadSheet = SpreadSheet("a","b","c")
spreadSheet.set(0,"a",1)
spreadSheet.set(0,"b",2)
spreadSheet.set(0,"c",3)
spreadSheet.set(1,"a",4)
spreadSheet.set(2,"b",5)
spreadSheet.set(3,"c",6)
|      | a | b | c |
|  0  | 1 | 2 | 3 |
|  1  | 4 | 5 | 6 |


spreadSheet.get(0,"c")‍‍‌‌‌‍‌‍‍‍‍‌‌‍‍‍‌ -> 3
spreadSheet.get(4,"c") -> 0
spreadShest.printFirstNLine(3)
0 -> 1 2 3
1 -> 4 5 6
2 -> 0 0 0


[(row, col)] = value





实现permission system （permssion 继承）
如果一个user 有 folder权限，同样拥有所有下级权限
实现
- grantPermission(item, user)
- hasPermiss‍‍‌‌‌‍‌‍‍‍‍‌‌‍‍‍‌ion(item, user)


root(user1)
|---foo(user2)
|---haha
那么user1就有root,foo,haha的权限，user2只有foo的权限。实现两个function
void grant_permission(dir,user)
boolean has_permission(dir,user)
第一个就用BFS，找到node，然后‍‍‌‌‌‍‌‍‍‍‍‌‌‍‍‍‌把用户加进去，第二个用DFS，找到path，然后看一下这个user在不在path里面

Trie



系统设计是给一个 服务 api是给path 回子path 设计一个job能高效得到‍‍‌‌‌‍‌‍‍‍‍‌‌‍‍‍‌所有子目录和文件在某个根目录上 有点像web crawler
