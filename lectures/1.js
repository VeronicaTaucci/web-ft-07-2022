// function mul(a) {
//     return function (b) {
//         return function (c) {
//             return a * b * c;
//         };
//     };
// }
// console.log("output with normal function", mul(2)(4)(6));

//! reverse a string 
// function reverseString(str) {
//     var newString = "";
//     for (var i = str.length - 1; i >= 0; i--) {
//         newString += str[i];
//     }
//     return newString;
// }
// reverseString('hello');


// what will the output be?
// for (let i = 0; i < 5; i++) {
//     setTimeout(function () {
//         console.log(i);
//     }, i * 1000);
// }