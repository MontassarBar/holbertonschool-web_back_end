export default function updateStudentGradeByCity(array, city, newGrades) {
  const array1 = array.filter((studentLocation) => studentLocation.location === city);
  const array2 = array1.map((student) => {
    const studentGrade = newGrades.find((grade) => grade.studentId === student.id);
    if (studentGrade) {
      return { ...student, grade: studentGrade.grade };
    }
    return { ...student, grade: 'N/A' };
  });
  return array2;
}
