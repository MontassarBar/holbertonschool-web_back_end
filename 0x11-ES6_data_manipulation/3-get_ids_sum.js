export default function getStudentIdsSum(array) {
  const initialValue = 0;
  const sumWithInitial = array.reduce(
    (accumulator, currentValue) => accumulator + currentValue.id,
    initialValue,
  );
  return sumWithInitial;
}
