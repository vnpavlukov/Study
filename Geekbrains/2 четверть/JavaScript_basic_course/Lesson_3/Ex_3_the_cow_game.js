function resetGame() {

    let generateNumbers = [];

    while (generateNumbers.length < 4) {
        const part = Math.floor(Math.random() * 10);
        if (!generateNumbers.includes(part)) generateNumbers.push(part);
    }
    console.log(generateNumbers);
}

function isValidAnswer() {

}

function startGame() {
    let attemptsCount = 0;

    while (true) {
        const answer = prompt('Guess 4 different numbers. For exit get -1.');

        if (answer === '-1') return alert('Games over!');

        if (!isValidAnswer(answer)) continue;

        attemptsCount++;


    }
}