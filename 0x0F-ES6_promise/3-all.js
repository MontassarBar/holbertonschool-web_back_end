import { createUser, uploadPhoto } from './utils';

export default function handleProfileSignup() {
  Promise.all([uploadPhoto(), createUser()])
    .then((data) => console.log(data[0].body, data[1].firstName, data[2].lastName))
    .catch(() => console.log('Signup system offline'));
}
