const http = require('http');
const url = require('url');
const countStudents = require('./3-read_file_async');

const app = http.createServer((req, res) => {
  const urlParts = url.parse(req.url);
  if (urlParts.pathname === '/') {
    res.write('Hello Holberton School!');
    res.end();
  } else if (urlParts.pathname === '/students') {
    countStudents(process.argv[2])
      .then((result) => {
        res.write(`This is the list of our students\n${result}`);
        res.end();
      })
      .catch((error) => {
        res.write(`This is the list of our students\n${error.message}`);
        res.end();
      });
  }
}).listen(1245);

module.exports = app;
