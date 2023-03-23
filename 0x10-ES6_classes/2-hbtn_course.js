export default class HolbertonCourse {
  constructor(name, length, students) {
    this.name = name;
    this.length = length;
    this.students = students;
  }

  set name(name) {
    if (typeof name !== 'string') {
      throw TypeError('Name must be a string');
    } else {
      this._name = name;
    }
  }

  get name() {
    return this._name;
  }

  set length(length) {
    if (typeof length !== 'number') {
      throw TypeError('Length must be a number');
    } else {
      this._length = length;
    }
  }

  get length() {
    return this._length;
  }

  set students(students) {
    if (students.every((student) => typeof student !== 'string')) {
      throw TypeError('Students must be an array of strings');
    } else {
      this._students = students;
    }
  }

  get students() {
    return this._students;
  }
}
