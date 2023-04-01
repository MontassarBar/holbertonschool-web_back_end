const fs = require('fs');

function countStudents(database) {
  try {
    const fields = [];
    let header = [];
    const data = fs.readFileSync(database, 'utf-8');
    const students = data.split('\n').map((student) => student.split(','));
    header = students.shift();
    for (let y = 0; y < students.length; y += 1) {
      for (let x = 0; x < students[y].length; x += 1) {
        students[y][header[x]] = students[y][x];
      }
      students[y].splice(0, 4);
    }
    students.pop();
    students.forEach((student) => {
      if (fields.indexOf(student.field) === -1) {
        fields.push(student.field);
      }
    });
    console.log(`Number of students: ${students.length}`);
    for (const field of fields) {
      const n = students.filter((student) => student.field === field);
      let firstnames = '';
      for (const st of n) {
        firstnames += `${st.firstname}, `;
      }
      console.log(`Number of students in ${field}: ${n.length}. List: ${firstnames.slice(0, -2)}`);
    }
  } catch (err) {
    throw Error('Cannot load the database');
  }
}
module.exports = countStudents;
