const numbers = [2, 4, 6];

const sum = numbers.reduce(function (sum, number) {
  const updatedSum = sum + number;
  return updatedSum;
}, 0);

const products = ["oranges", "apples"];

for (const [index, product] of products.entries()) {
  console.log(index, product);
}

const persons = [{ name: "John Smith" }, { name: "Jane Doe" }];

for (const { name } of persons) {
  console.log(name);
}
// 'John Smith'
// 'Jane Doe'

const names = new Map();
names.set(1, "one");
names.set(2, "two");

for (const [number, name] of names) {
  console.log(number, name);
}

console.log(map.has(2)); // output: true or false

console.log(2 in obj); // output: true or false
console.log(obj.hasOwnProperty(2)); // output: true or false

const search = " ";
const replaceWith = "-";

const result = "duck duck go".replaceAll(search, replaceWith);
const result2 = string.replace(/SEARCH/g, replaceWith);
console.log(result); // => 'duck-duck-go'
console.log(result2); // => 'duck-duck-go'
// If search argument is a non-global regular expression, then replaceAll() throws a TypeError exception.
