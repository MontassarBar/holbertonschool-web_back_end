/* eslint-disable  no-unused-vars */
export default function returnHowManyArguments(...args) {
  let x = 0;
  for (const arg of args) x += 1;
  return x;
}
