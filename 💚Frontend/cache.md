const priceListsCacheMap: Map<string, Promise<APIAnswer>> = new Map();

export const getPriceListByZipcode = (zipcode: string): Promise<APIAnswer> => {
 if (!priceListsCacheMap.has(zipcode)) {
   priceListsCacheMap.set(zipcode, getPriceList(zipcode));
 }
 return priceListsCacheMap.get(zipcode);
};