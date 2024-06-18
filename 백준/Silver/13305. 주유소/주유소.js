const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./ex.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\n");
const N = input[0];
const road_len = input[1].split(" ").map(BigInt);
const oil_price = input[2].split(" ").map(BigInt);

// console.log(N, road_len, oil_price);

let cur_price = oil_price[0];
let cost = 0n;

for (let i = 0; i < N - 1; i++) {
  // 일단 가야 함.
  cost += cur_price * road_len[i];

  // 내가 더 비싸면 다음 거리는 다음 가게 가격으로 사자
  if (cur_price > oil_price[i + 1]) {
    cur_price = oil_price[i + 1];
  }
}

console.log(String(cost));
