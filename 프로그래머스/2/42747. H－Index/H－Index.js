function solution(citations) {
    var answer = 0;
    let filtered = citations = citations.filter((v) => {
        return v !== 0;
    })
    let sorted = filtered.sort((a,b) => a-b);
    console.log(sorted)
    // 3, 3, 3, 3, 4, 5, 6 => 3
    for (let i=1; i<sorted.length+1; i++) {
        let h = sorted.findIndex((v) => v >= i);
        if (h === -1 || sorted.length - h < i) {
            break;
        }
        answer = i;
    }
    return answer;
}