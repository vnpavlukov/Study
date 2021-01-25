var good = 'Apple'

switch (good) {
    case 'Bananas':
        console.log('50');
        break;      // если не поставить break, то выполнится весь код при выполнении условия
    case 'Mango':
        console.log('120');
        break;
    case 'Apple':   //т.к. у груш и яблок цена одинаковая, то убираем break и выполнится следующий кейс автоматом
    case 'Pears':
        console.log('80');
        break;
    default:        //выступает вместо else
        console.log('50');
}