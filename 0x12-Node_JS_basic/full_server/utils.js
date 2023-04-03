const fs = require('fs');

async function readDatabase(database) {
  return new Promise((resolve, reject) => {
    const fields = [];
    let header = [];
    const obj = {};
    fs.readFile(database, 'utf-8', (err, data) => {
      if (err) {
        reject(new Error(err));
      } else {
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
        for (const field of fields) {
          const n = students.filter((student) => student.field === field);
          obj[field] = [];
          for (const std of n) {
            obj[field].push(std.firstname);
          }
        }
        resolve(obj);
      }
    });
  });
}

module.exports = readDatabase;
