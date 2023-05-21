5 Ways to Deep Copy Objects in JavaScript
In JavaScript, we can perform a copy on objects using the following methods:

| Method	| Pros |	Cons|
|--|--|--|
shallow copy with `=` |	clear and direct, the default	| only shallow copies objects |
|`JSON.stringify()` and `JSON.parse()`|	deep copies nested objects	| doesn't copy functions |
|`Object.assign()` |	copies the immediate members of an object—including functions	| doesn't deep copy nested objects|
|the `...` spread operator |	simple syntax, the preferred way to copy an object	| doesn't deep copy nested objects|
| Lodash `cloneDeep()` |	clones nested objects including functions |	adds an external dependency to your project |
