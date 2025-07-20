let Roll_Numbers = [30, 1007, 10011, 1009, 10010];
console.log(Roll_Numbers.sort((a, b) => a - b));
console.log(Roll_Numbers.sort((a, b) => b - a));
console.log(Roll_Numbers.sort().reverse());

console.log(Math.ceil(-2.3));
console.log(Math.floor(-2.3));

console.log(Math.min.apply(null, Roll_Numbers));
