const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./ex.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\n");
let [N, K] = input[0].split(" ").map(Number);
input.shift();
const coins = input.map(Number);
let answer = 0;

for (let i = N - 1; i >= 0; i--) {
  answer += Math.floor(K / coins[i]);
  K = K % coins[i];
}

console.log(answer);
