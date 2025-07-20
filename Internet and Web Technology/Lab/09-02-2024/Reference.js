// // var arr = [1, 2, 4, 5, 7, 8];
// // // var myFun = (element) => (element % 2 == 0 ? 5 * element : 2 * element);
// // // var doubleArr = arr.map(myFun);
// // // console.log(arr, doubleArr);
// // let odd = arr.filter((e) => e % 2 != 0);
// // let even = arr.filter((e) => e % 2 == 0 && e > 3);
// // console.log(odd);
// // console.log(`even array ${even.join()}`);
// // console.log(Date.now());

// let persons = [
//   { name: "Harry", age: 14 },
//   { name: "Ethan", age: 30 },
//   { name: "Peter", age: 21 },
//   { name: "John", age: 21 },
//   { name: "Clark", age: 42 },
//   { name: "Alice", age: 16 },
// ];
// // task 1 find all persons with age > 18
// let adultPersons = persons.filter((person) => person.age > 18);
// console.log(adultPersons);

// // task 2 increase age +1 if age<18
// persons = persons.map((person) =>
//   person.age < 18 ? { ...person, age: person.age + 1 } : person
// );
// console.log(persons);
// // task 3 find and update person John to Johnwidth
// let message = persons.find((p) => p.name == "John")
//   ? persons.map((person) =>
//       person.name == "John" ? { ...person, name: "Johnwidth" } : person
//     )
//   : "John Is Not Present";

// console.log(message);
// console.log(persons.find((p) => p.name == "John"));
// //task 4 add new person
// persons = [{ name: "Arzoo", age: 35 }, ...persons];

// //task 5 arrange all person by age
// persons.sort((a, b) => a.age - b.age);
// console.log(persons);

// persons = persons.filter((person) => person.age > 18);
// console.log(persons);
function checkdate() {
  var dob = new Date(document.getElementById("txtDob").value);
  var ad = new Date(document.getElementById("txtAD").value);
  var lastDate = new Date(ad.getFullYear() + "-11-31");
  console.log(lastDate);
  var age = lastDate.getFullYear() - dob.getFullYear();
  if (lastDate.getMonth() < dob.getMonth()) {
    age--;
  }
  if (
    lastDate.getMonth() == dob.getMonth() &&
    lastDate.getDate() < dob.getDate()
  ) {
    age--;
  }
  if (age >= 17) {
    document.getElementById("msg").innerText = "Your are eligible";
  } else {
    document.getElementById("msg").innerHTML =
      "Your are not eligible, try on  year :" +
      (lastDate.getFullYear() + (17 - age)) +
      "!!!";
  }
  console.log("year/s", age);
  //   console.log("month", dob.getMonth());
  //   console.log("day", dob.getDay());
  //   console.log("date", dob.getDate());
}
