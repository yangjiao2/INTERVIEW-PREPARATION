

/*
Alien Dictionary App


Part 1.)
Given a list of objects in the form {word: <word_1>, definition: <definition_ 1>}. Write a function that sorts the list in either ascending or descending order. However we have a new alphabetical ordering system...

example:

orderingSystem = "worldabcefghijkmnpqstuvxyz"
wordsList = [
    {word: "word", definition: "Donec sagittis luctus iaculis" },
    {word: "world", definition: "faucibus porttitor non" },
    {word: "tesla", definition: "ibh ultricies elementum eget vel"},
    {word: "teslar", definition: "laoreet metus non mauris feugiat molestie"},
    {word: "apple", definition: ". Nullam a pretium elit. Ut ex odio, moles"},
    {word: "strawberry", definition: "Suspendisse in erat mi. Ut id lacinia metus. Prae"},
  ];
}

newList = alienSort(wordsList, "ascend");

newList = [
  {word: "world", definition: "faucibus porttitor non"}
  {word: "word",  definition: "Donec sagittis luctus iaculis"}
  {word: "apple", definition: "Nullam a pretium elit. Ut ex odio, moles"}
  {word: "strawberry", definition: "Suspendisse in erat mi. Ut id lacinia metus. Prae"}
  {word: "tesla", definition: "ibh ultricies elementum eget vel"}
  {word: "teslar", defintition: "laoreet metus non mauris feugiat molestie"}
];

You may use javscript's built in sort function.
Here is an example:

a = [4, 2, 1, 3]
const compareFn = (a,b) => {
  if (a > b) {
    return 1
  }
  if (a, < b) {
    return -1
  }
  return 0;
}
a.sort(compareFn) --> [1, 2, 3, 4]
*/

const orderingSystem = "worldabcefghijkmnpqstuvxyz";
const compareFn = (a_obj,b_obj) => {
  const a = a_obj["word"];
  const b = b_obj["word"];

  const min_length = Math.min(a.length, b.length);

  for (let index = 0; index <= min_length ; index++){
    const a_char = a[index];
    const b_char = b[index];

    const a_index = orderingSystem.indexOf(a_char)
    const b_index = orderingSystem.indexOf(b_char)

    if (a_index < b_index){
      return 1;
    } else if (a_index > b_index){
      return -1;
    }
  }
  if (a.length > b.length){
    return 1;
  } else if (a.length < b.length){
    return -1;
  }
  return 0;
}

const wordsList = [
  {word: "word", definition: "Donec sagittis luctus iaculis" },
  {word: "world", definition: "faucibus porttitor non" },
  {word: "tesla", definition: "ibh ultricies elementum eget vel"},
  {word: "teslar", definition: "laoreet metus non mauris feugiat molestie"},
  {word: "apple", definition: ". Nullam a pretium elit. Ut ex odio, moles"},
  {word: "strawberry", definition: "Suspendisse in erat mi. Ut id lacinia metus. Prae"},
];

wordsList.sort(compareFn)

console.log(wordsList);


const alienSort = (wordsList, ordering, system) => {
  let orderSystem = system;
  if (ordering === "ascend") {
    orderSystem = system.slice().reverse();
  }

  const wordsCopy = wordsList.slice();
  wordsCopy.sort(compareFn);
  return wordsCopy
}

console.log(alienSort(wordsList, "ascend", orderingSystem));

/*

|word        definition                                         |
|------------------------------------------------------------   |
|word        Donec sagittis luctus iaculis                      |
|world       faucibus porttitor non                             |
|tesla       ibh ultricies elementum eget vel                   |
|teslar      laoreet metus non mauris feugiat molestie          |
|apple       Nullam a pretium elit. Ut ex odio, moles           |
|strawberry  Suspendisse in erat mi. Ut id lacinia metus. Prae  |
            | neutral (0) -> ascend (1) -> descend (1) -> neutral|
*/


const App = () => {
  const [sortType, setSortType ] = useState(0);
  const [wordsList, setWordsList] = useState([]);

  const OnClick = () => {
    setSortType(prevState  => {
      if (prevState == 0){
        return 1;
      } else if (prevState == 1){
        return -1;
      } else { // prevState == -1
        return 0;
      }
    })
  }

  // fetch data
  let wordsListTmp = [...wordsList];
  // sort

  return (
    <table>
      <tr>
        <td>

          </td>
      </tr>
    </table>
    <button onClick={OnClick} > {
  sortType == 'neutral'
    }</button>
  );
}
