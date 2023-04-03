const readDatabase = require('../utils');

class StudentsController {
  static getAllStudents(request, response, database) {
    readDatabase(database)
      .then((data) => {
        const arr = [];
        arr.push('This is the list of our students');
        for (const key in data) {
          if (!key) {
            arr.push(`Number of students in ${key}: ${data[key].length}. List: ${data[key].join(', ')}`);
          }
        }
        response.status(200).send(arr.join('\n'));
      })
      .catch((error) => response.status(500).send(error.message));
  }

  static getAllStudentsByMajor(request, response, database) {
    if (request.path !== '/CS' || request.path !== '/SWE') {
      response.status(500).send('Major parameter must be CS or SWE');
    } else {
      readDatabase(database)
        .then((data) => {
          if (request.path === '/CS') {
            response.status(200).send(`List: ${data.CS}`);
          } else {
            response.status(200).send(`List: ${data.SWE}`);
          }
        })
        .catch((error) => response.status(500).send(error.message));
    }
  }
}

module.exports = StudentsController;
