const fs = require('fs');

async function countStudents(database) {
  return new Promise((resolve, reject) => {
    const fields = [];
    let header = [];
    fs.readFile(database, 'utf-8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }
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
      const arr = [];
      arr.push(`Number of students: ${students.length}`);
      console.log(`Number of students: ${students.length}`);
      for (const field of fields) {
        const n = students.filter((student) => student.field === field);
        let firstnames = '';
        for (const st of n) {
          firstnames += `${st.firstname}, `;
        }
        arr.push(`Number of students in ${field}: ${n.length}. List: ${firstnames.slice(0, -2)}`);
        console.log(`Number of students in ${field}: ${n.length}. List: ${firstnames.slice(0, -2)}`);
      }
      const str = arr.join('\n');
      resolve(str);
    });
  });
}

module.exports = countStudents;
