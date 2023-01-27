https://www.youtube.com/playlist?list=PLbhaS_83B97tFPucgkG5gL0OtMzD37lVE


而无益 三思瑶
时间复杂度


伊耳三吴

酒店预定


外星人字典


你为什么选择我们公司？
除了专业，还有什么可以激发你强烈兴趣？



warm up: 125
follow up: 336


题目1 是： 376
题目2是： 890



依依路路，多加了一个callback 方法，要求implement一个interface。



https://www.1point3acres.com/bbs/thread-954110-1-1.html


 伊尔伞舞 饵遥而


https://leetcode.com/problems/fraction-to-recurring-decimal/




class DataStore {
    constructor() {
        this.data = new Map();
        this.change = new Map();
        this.dataEvent = new Map();
    }

    add (name, val) {
        if (this.change.has(name)) {
            if (val != this.data.get(name)) {
                // change happens
                this.change.get(name).call(this, this.data.get(name), val, name);
            }
        }
        if (this.dataEvent.has(name)) {
            this.dataEvent.get(name).call(this, this.data.get(name), val, name);
        }

        this.data.set(name, val);
    }

    has(name) {
        if (this.data.has(name)) {
            return true;
        }
        return false;
    }

    on (event, callbackFn) {
        const p = event.indexOf(':');
        if (p != -1) {
            if (event.substring(0, p) == 'change') {
                this.change.set(event.substring(p+1), callbackFn);
            }
        } else {
            this.dataEvent.set(event, callbackFn);
        }
    }
}

//  test
const ds = new DataStore();
console.log(`ds.add('name', 'Joe')`);
ds.add('name', 'Joe');
console.log(`ds.has("name") = ${ds.has("name")}`);

console.log(`ds.add('age', 30)`);
ds.add('age', 30);
console.log(`ds.has("age") = ${ds.has("age")}`);

console.log(`Sub change:name event`);
ds.on('change:name', (oldVal, newVal, key) => {
    console.log(`The ${key} changes from ${oldVal} to ${newVal}`);
})

console.log(`ds.add('name', 'Tom')`);
ds.add('name', 'Tom');


console.log(`Sub name event`);
ds.on('name', (oldVal, newVal, key) => {
    console.log(`Set ${key} to ${newVal}. The old value is ${oldVal}`);
})

console.log(`ds.add('name', 'Nick')`);
ds.add('name', 'Nick');


https://leetcode.com/problems/flatten-nested-list-iterator/
