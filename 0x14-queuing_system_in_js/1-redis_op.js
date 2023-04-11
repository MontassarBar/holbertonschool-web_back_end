const redis = require('redis')
const client = redis.createClient();

async () => await client.connect();
client.on('ready', () => {console.log('Redis client connected to the server')});
client.on('error', err => console.log('Redis client not connected to the server:', err));

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, function(err, reply) {
        redis.print(`Reply: ${reply}`);
      });
}
function displaySchoolValue(schoolName) {
    client.get(schoolName, function(err, reply) {
        console.log(reply)});
}


displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
