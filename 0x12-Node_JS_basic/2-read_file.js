const fs = require('fs');
const csv = require('fast-csv');

function countStudents(database) {
  const data = [];
  const fields = [];
  try {
    fs.readFileSync(database);
  } catch (err) {
    throw Error('Cannot load the database');
  }
  fs.createReadStream(database)
    .pipe(csv.parse({ headers: true }))
    .on('data', (row) => data.push(row))
    .on('data', () => data.forEach((student) => {
      if (fields.indexOf(student.field) === -1) {
        fields.push(student.field);
      }
    }))
    .on('end', () => {
      console.log(`Number of students: ${data.length}`);
      for (const field of fields) {
        const x = data.filter((student) => student.field === field);
        let firstnames = '';
        for (const st of x) {
          firstnames += `${st.firstname}, `;
        }
        console.log(`Number of students in ${field}: ${x.length}. List: ${firstnames.slice(0, -2)}`);
      }
    });
}
module.exports = countStudents;
