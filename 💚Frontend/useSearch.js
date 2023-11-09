import * as React from 'react';
type Tuple<T> = [T[], string];

type KeyOfOrNever<T extends any[]> = T extends string[] ? never : keyof T[0];

interface ResultStruct<T> extends Tuple<T> {
  result: T[];
  search: string;
}

const isObject = (obj: any) => obj != null && obj.constructor.name === 'Object';

const useDebounce = (search: string, delay: number) => {
  const [debouncedValue, setDebounceValue] = React.useState(search);

  React.useEffect(() => {
    const timer = setTimeout(() => {
      setDebounceValue(search);
    }, delay);

    return () => clearTimeout(timer);
  }, [search]);

  return debouncedValue;
};

export const useSearch = <T extends any[]>(
  data: T,
  search: string,
  searchable?: KeyOfOrNever<T>
) => {
  if (searchable && !isObject(data[0]))
    throw new Error('searchable is only used for an array containing objects');

  const debounced = useDebounce(search, 3000);

  const result = React.useMemo(() => {
    // Or you can use this below but be aware it is not like above cause using regex letter order matters:
    // data.filter(item => `${item[searchable as string]}`.includes(search.toLowerCase())
    // regex: if you search typing 'a' it will return only the third item;
    // includes: if you search typing 'a' it will return third, fourth and fifth items;
    const regex = new RegExp(`^${search}`, 'i');
    const filtered = data.filter((item) =>
      regex.test(searchable ? item[searchable] : item)
    );
    const result =
      filtered.length > 0
        ? filtered
        : [searchable ? { [searchable]: 'No results' } : 'No results'];
    let resultStruct = [result, search] as ResultStruct<T[number]>;
    resultStruct.result = result;
    resultStruct.search = search;
    return resultStruct;
  }, [debounced]);

  return result;
};
