const kue = require('kue')

const queue = kue.createQueue();

const obj = {
    phoneNumber: '4153518780',
    message: 'This is the code to verify your account',
  };

const job = queue.create('push_notification_code', obj).save(function(err){
    if( !err ) console.log(`Notification job created: ${job.id}`);
 });

 job.on('complete', () => console.log('Notification job completed'));
 job.on('failed', () => console.log('Notification job failed'));