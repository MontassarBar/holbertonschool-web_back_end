const http = require('http');
const url = require('url');

const app = http.createServer((req, res) => {
  const urlParts = url.parse(req.url);
  if (urlParts.pathname === '/') {
    res.write('Hello Holberton School!');
    res.end();
  } else if (urlParts.pathname === '/students') {
    res.write('This is the list of our students');
    res.end();
  }
}).listen(1245);

module.exports = app;
