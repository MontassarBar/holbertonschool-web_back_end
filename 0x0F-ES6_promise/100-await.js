import { uploadPhoto, createUser } from './utils';

export default async function asyncUploadUser() {
  let val1 = await uploadPhoto();
  let val2 = await createUser();
  try {
    return {
      photo: val1,
      user: val2,
    };
  } catch (error) {
    return {
      photo: null,
      user: null,
    };
  }
}
