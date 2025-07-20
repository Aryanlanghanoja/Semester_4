let colors = ["Red", "Green", "Blue"];
let removed = colors.splice(0,1); // Remove the first element
 
console.log(colors); // Prints: Green,Blue
console.log(removed); // Prints: Red (one item array)
console.log(removed.length); // Prints: 1
 
removed = colors.splice(1, 0, "Pink", "Yellow"); // Insert two items at position one
console.log(colors); // Prints: Green,Pink,Yellow,Blue
console.log(removed); // Empty array
console.log(removed.length); // Prints: 0
 
removed = colors.splice(1, 1, "Purple", "Voilet"); // Insert two values, remove one
console.log(colors); //Prints: Green,Purple,Voilet,Yellow,Blue
console.log(removed); // Prints: Pink (one item array)
console.log(removed.length); // Prints: 1

// Create One Arry which has values from 1 to 6 remove elements from the index 2 and 4 then add elements 100,200,300 at the beinings

let numbers = [1,2,3,4,5,6];
console.log(numbers);



