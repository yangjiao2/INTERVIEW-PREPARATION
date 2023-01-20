是地里提到的allocation Id的题目，感觉没有地里描述的那么复杂， get() 和 free() 实现 【1 to N】， 也没要求有多随机。
第一问，就直接用queue （list），每次分配从尾部取最后一个移除出去，free就放回去，都是O（1）的操作
第二问，告诉你boolean 是1bit，integer 是8 bit，如何improve space，同时提示可以sacrifice一些time complexity； 开一个size = N的数组，linear scan； space从O（8n）降到了O(n), get的time 从O（1）变成了O（N）
第三问，希望能优化both time 和 complexity，space < O(8n), time 能优于O（N）； 一开始以为是要优化big O，轨迹慌忙地说要用binary search （这样有log N），但后来发现没有sorted order；然后面试官提示说不一定要big O的优化，可以比如说优化到O（N/2）这样。感觉是用bucket的提示，于‍‍‌‌‌‍‌‍‍‍‍‌‌‍‍‍‌是propose了用两个bucket 分配Id， 最后写完 debug完刚好时间到。
