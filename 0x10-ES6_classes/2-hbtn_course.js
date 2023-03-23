export default class HolbertonCourse {
  constructor(name, lenght, students) {
    this.name = name;
    this.lenght = lenght;
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

  set lenght(lenght) {
    if (typeof lenght !== 'number') {
      throw TypeError('Lenght must be a number');
    } else {
      this._lenght = lenght;
    }
  }

  get lenght() {
    return this._lenght;
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
