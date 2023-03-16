export default function appendToEachArrayValue(array, appendString) {
  let array2 = [];
  for (const idx of array) {
    array2 = [...array2, appendString + idx];
  }
  return array2;
}
