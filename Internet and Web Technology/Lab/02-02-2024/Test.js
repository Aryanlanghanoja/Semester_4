var Array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
var Function = (Element) => Element % 2 == 0 ? Element * 5 : Element % 2;
var DoubleArray = Array.map(Function);
console.log(Array, Function);

