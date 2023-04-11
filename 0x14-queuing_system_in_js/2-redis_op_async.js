const { exitCode } = require('process');
const redis = require('redis')
const client = redis.createClient();
const util = require('util')
async () => await client.connect();
client.on('ready', () => {console.log('Redis client connected to the server')});
client.on('error', err => console.log('Redis client not connected to the server:', err));

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, function(err, reply) {
        redis.print(`Reply: ${reply}`);
      });
}

async function displaySchoolValue(schoolName) {
    const get = util.promisify(client.get).bind(client)
    const schoolname = await get(schoolName);
    console.log(schoolname)
}

async function exc() {
await displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
await displaySchoolValue('HolbertonSanFrancisco');
}
exc()
