let colors = ["Red", "Green", "Blue"];
 
console.log(colors.join()); // Prints: Red,Green,Blue
console.log(colors.join("")); // Prints: RedGreenBlue
console.log(colors.join("-")); // Prints: Red-Green-Blue
console.log(colors.join(", ")); // Prints: Red, Green, Blue

// Seprate Your Values of D Using Colon

let Numbers = [1, 2, 3, 4, 5, 6];
console.log(Numbers.join(":"));


let fruits = ["Apple", "Banana", "Mango", "Orange", "Papaya"];
let subarr = fruits.slice(1, 4);
console.log(subarr); // Prints: Banana,Mango
console.log(fruits);

// Create Array Which Contains Values of 1 to 10

let Array = [1,2,5,7];
let Ans = (Array.length % 2 == 0) ? (Array[(Array.length / 2) - 1] + " " + Array[Array.length / 2]) : (Array[Math.floor(Array.length / 2)]);
console.log(Array + "\n" + Ans);

// From the Given Array Create New Array Which Contains only Odd Values

let Number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
let odd = Number.filter(x => x % 2 != 0);
console.log(`Odd Numbers From Array :- ${Number.join()} Is ${odd.join()}`); // Prints: [1, 3, 5, 7, 9]

// Create Array from a Given Array all the values are even should be grater than 3
let Even = Number.filter(x => (x % 2 == 0 && x >= 3))
console.log(`Even Numbers And Greater Than 3 From Numbers From Array :- ${Number.join()} Is ${Even.join()}`);
console.log(Date.now()); 


    