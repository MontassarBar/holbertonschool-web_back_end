export default function getListStudentIds(array) {
  if (Array.isArray(array) === true) {
    return array.map((key) => key.id);
  }
  return [];
}
