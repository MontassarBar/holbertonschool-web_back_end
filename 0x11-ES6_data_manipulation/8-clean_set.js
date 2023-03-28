export default function cleanSet(set, startString) {
  let x = '';
  for (const elem of set) {
    if (startString && elem && elem.substring(0, startString.length) === startString) {
      const str = elem.substring(startString.length, elem.lenght);
      x += (str);
      x += '-';
    }
  }
  return x.slice(0, -1);
}
