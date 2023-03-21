import { uploadPhoto, createUser } from './utils';

export default async function asyncUploadUser() {
  try {
    const val1 = await uploadPhoto();
    const val2 = await createUser();
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
