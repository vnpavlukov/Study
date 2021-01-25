// for (let i = 0; ; i++) {
//     if (i > 10) break;
//     if (i % 2 === 1) continue;
//     console.log(i);
// }

// let arr = [55, true, 1, null, null];
//
// for (let i = 0; i < arr.length; i++) {
//     console.log(arr[i]);
// }
//
// for (const key in arr) {
//     console.log(arr[key]);
// }
//
// for (const val of arr) {
//     console.log(val);
// }

let arr = [55, true, 1, null, null];
arr.forEach((item) => {
    console.log(item)
});