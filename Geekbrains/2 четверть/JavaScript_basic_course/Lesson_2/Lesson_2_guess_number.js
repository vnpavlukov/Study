let number;
let attempts;

function resetGame() {
    attempts = 0
    number = Math.floor(Math.random() * 100)    //рандом от 0 до 1, умножаем на 100 и делаем int
    console.log(number)
}

function tryGuessNumber() {
    const answer = parseInt(prompt('Угадайте число от 0 до 100 (выход:-1):'));  //parseInt преобразов в int

    if (answer === -1) return alert('Good by')

    if (Number.isNaN(answer) || 0 > answer > 100) {
        alert('Введите число от 0 до 100');
        tryGuessNumber();
        return
    }

    attempts++;

    if (answer > number) {
        alert('Слишком много))');
    } else if (answer < number) {
        alert('Маловато будет)');
    } else {
        alert(`Грац! Ты угадал число с ${attempts} попыток`)

        if (!confirm('Сыграем ещё?')) {
            alert('Адию!');
            return
        }
        resetGame();
    }

    tryGuessNumber();
}

resetGame();
tryGuessNumber();