const settings = {
    maxX: 10,
    maxY: 10,
    startPositionX: 0,
    startPositionY: 0,
};

const player = {
    x: null,
    y: null,

    init(startX, startY) {
        this.x = startX;
        this.y = startY;
    },

    move(direction) {
        switch (direction) {
            case 2:
                this.y++;
                break;
            case 4:
                this.x--;
                break;
            case 6:
                this.x++;
                break;
            case 8:
                this.y--;
        }
    },
};


const game = {
    settings: settings,         // эту запись можно сократить просто написав settings
    player: player,

    run() {
        this.player.init(this.settings.startPositionX, this.settings.startPositionY);

        while (true) {
            this.render();

            const direction = this.getDirection();

            if (direction === -1) return alert('Good by');

            this.player.move(direction);

        }

    },

    render() {
        let map = '';

        for (let row = 0; row < this.settings.maxX; row++) {
            for (let col = 0; col < this.settings.maxX; col++) {
                if (this.player.y === row && this.player.x === col) {
                    map += '0 ';
                } else {
                    map += 'x ';
                }
            }
            map += '\n';
        }

        console.clear();
        console.log(map);
    },

    getDirection() {
        const availiableDirections = [-1, 2, 4, 6, 8];

        while (true) {
            const direction = parseInt(prompt('Give me the number where need to go, -1 for exit:'));

            if (!availiableDirections.includes(direction)) {
                alert('give me: ${availiableDirections.join(', ')}.');
                continue;
            }
            return direction;
        }
    }
}

game.run()