const express = require('express');
const routes = require('./routes/index');

const app = express();
const port = 1245;

routes(app);

app.listen(port);

export default app;
