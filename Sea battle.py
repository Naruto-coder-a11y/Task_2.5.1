import random
#Параметры доски
width = 9
height = 9


class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Ship:
    def __init__(self, ship_nose, length, orientation):
        self.ship_nose = ship_nose
        self.length = length
        self.orientation = orientation

    def dots(self):
        ship_coord = []
        try:
            if self.orientation == 1:
                for i in range(self.length):
                    if height > self.ship_nose.y + i > 0:
                        ship_coord.append([self.ship_nose.x, self.ship_nose.y + i])
                    else:
                        raise IndexError

            elif self.orientation == 2:
                for i in range(self.length):
                    if width > self.ship_nose.x + i > 0:
                        ship_coord.append([self.ship_nose.x + i, self.ship_nose.y])
                    else:
                        raise IndexError

            elif self.orientation == 3:
                for i in range(self.length):
                    if height > self.ship_nose.y - i > 0:
                        ship_coord.append([self.ship_nose.x, self.ship_nose.y - i])
                    else:
                        raise IndexError

            elif self.orientation == 4:
                for i in range(self.length):
                    if width > self.ship_nose.x - i > 0:
                        ship_coord.append([self.ship_nose.x - i, self.ship_nose.y])
                    else:
                        raise IndexError

            else:
                print('Вы неверно ввели направление корабля, снова введите координаты и направление')
                return False
        except IndexError:
            return False
        else:
            return ship_coord


class Board:
    def __init__(self, is_player):
        self.board = [['О' for i in range(width)] for j in range(height)]
        self.is_player = is_player
        self._coord = []
        self.set_board()


    def set_board(self):
        while True:
            for i in range(len(self.board)):
                self.board[0][0] = ' '
                self.board[0][i] = i
                self.board[i][0] = i
            # Создаем три обьекта класса Ship в случайной точке, неважно в какой, ведь дальше они будут менятся для каждого корабля
            #и нужны эти точки лишь для определения обьектов до обращения к ним
            x = Dot(random.randint(1, width-1), random.randint(1, height-1))
            ship1 = Ship(x, length=1, orientation=random.choice([1, 2, 3, 4]))
            ship2 = Ship(x, length=2, orientation=random.choice([1, 2, 3, 4]))
            ship3 = Ship(x, length=3, orientation=random.choice([1, 2, 3, 4]))
            try:
                while True:#один раз создаем и ставим корабль на 3 клетки
                    try:
                        if self.is_player:
                            print('Введите координату для корабля на 3 клетки')
                            for j in range(width):
                                print(*self.board[j])
                            x = Dot(int(input('Введите координату х - ')), int(input('Введите координату у - ')))
                            ship3 = Ship(x, length=3, orientation=(int(input('Введите направление корабля - '))))
                            if self.contour(ship3.dots()):
                                self.add_ship(ship3.dots())
                                for j in range(width):
                                    print(*self.board[j])
                                break
                        else:
                            if self.contour(ship3.dots()):
                                self.add_ship(ship3.dots())
                                break
                            else:
                                x = Dot(random.randint(1, width-1), random.randint(1, height-1))
                                ship3 = Ship(x, length=3, orientation=random.choice([1, 2, 3, 4]))
                    except ValueError or TypeError:
                        print('Вы ввели неверный формат данных')
                        continue
                for i in range(2):#два раза создаем и ставим корабль на 2 клетки
                    while True:
                        try:
                            if self.is_player:
                                print('Введите координату для корабля на 2 клетки')
                                x = Dot(int(input('Введите координату х - ')), int(input('Введите координату у - ')))
                                ship2 = Ship(x, length=2, orientation=(int(input('Введите направление корабля - '))))
                                if self.contour(ship2.dots()):
                                    self.add_ship(ship2.dots())
                                    for j in range(width):
                                        print(*self.board[j])
                                    break
                            else:
                                if self.contour(ship2.dots()):
                                    self.add_ship(ship2.dots())
                                    break
                                else:
                                    x = Dot(random.randint(1, width-1), random.randint(1, height-1))
                                    ship2 = Ship(x, length=2, orientation=random.choice([1, 2, 3, 4]))
                        except ValueError or TypeError:
                            print('Вы ввели неверный формат данных или же корабль вышел за границу игрового поля')
                            continue

                for i in range(4):#четыре раза создаем и ставим корабль на 1 клетку
                    while True:
                        try:
                            if self.is_player:
                                print('Введите координату для корабля на 1 клетку')
                                x = Dot(int(input('Введите координату х - ')), int(input('Введите координату у - ')))
                                ship1 = Ship(x, length=1, orientation=random.choice([1, 2, 3, 4]))
                                if self.contour(ship1.dots()):
                                    self.add_ship(ship1.dots())
                                    for j in range(width):
                                        print(*self.board[j])
                                    break
                            else:
                                if self.contour(ship1.dots()):
                                    self.add_ship(ship1.dots())
                                    break
                                else:
                                    x = Dot(random.randint(1, width-1), random.randint(1, height-1))
                                    ship1 = Ship(x, length=1, orientation=random.choice([1, 2, 3, 4]))
                        except ValueError or TypeError:
                            print('Вы ввели неверный формат данных или же корабль вышел за границу игрового поля')
                            continue
            except TypeError or IndexError:
                #ошибка выходит в том случае, когда координаты созданного корабля выходят за границы игрового поля
                #такая ошибка может возникать как при создании 1 корабля, так и послднего и цикл может уйти в бесконечность
                if self.is_player:
                    print('Корабль вышел за границы поля, все с начала')
                self.board = [['О' for i in range(width)] for j in range(height)]
                self._coord = []
                #поэтому в случае возникновения ошибки создаем поле заново
                continue

            else:
                break

    def add_ship(self, coordinate):
        for dot in coordinate:
            if self.is_player:
                self.board[dot[1]][dot[0]] = '■'
            self._coord.append(dot)

    def get_board(self, other):
        if self.is_player:
            for j in range(width):
                print(*self.board[j], '|', *other.board[j], end='\n')

    def get_coord(self):
        return self._coord

    def contour(self, coordinates):
        for dot in coordinates:  # Для каждой координаты предполагаемого места корабля проверяем наличие другого корабля
            try:
                if any([[dot[0] - 1, dot[1] - 1] in self._coord,
                        [dot[0] - 1, dot[1] + 1] in self._coord,
                        [dot[0] + 1, dot[1] - 1] in self._coord,
                        [dot[0] + 1, dot[1] + 1] in self._coord,
                        [dot[0] - 1, dot[1]] in self._coord,
                        [dot[0] + 1, dot[1]] in self._coord,
                        [dot[0], dot[1] + 1] in self._coord,
                        [dot[0], dot[1] - 1] in self._coord,
                        [dot[0], dot[1]] in self._coord]):
                    if self.is_player:
                        print('Выберите другое место для корябля, рядом стоит другой')
                    return False
            except IndexError or TypeError:
                return False
        return True

    def shot(self, x, y):
        try:
            if [x, y] in self._coord:
                if self.is_player:
                    print('Попал!')
                else:
                    print('По вам попали!')
                self._coord.pop(self._coord.index([x, y]))  # удаляем из списка кораблей координаты попадания
                self.board[y][x] = 'X'
                if not self._coord:
                    return False  # Все корабли уничтожены
                else:
                    return True
            elif self.board[y][x] == 'X' or self.board[y][x] == 'T':
                if self.is_player:
                    print('Вы уже стреляли сюда, выберите другое место')
                return True
            elif x == 0 or y == 0:
                if self.is_player:
                    print('Вы хотите выстрелить мимо поля, выберите другое место')
                return True
            else:
                if self.is_player:
                    print('Не попал!')
                else:
                    print('По вашим кораблям не попали')
                self.board[y][x] = 'T'
                return False
        except IndexError:
            print('Вы вышли за пределы игрового поля, повторите попытку')
            return True

class Player:
    def __init__(self, board):
        self.board = board

    def ask(self):
        pass

    def move(self):
        try:
            coordinate = self.ask()
            x = coordinate[0]
            y = coordinate[1]
            print(x, y)
            return self.board.shot(x, y)
        except TypeError:
            print('Вы ввели неправильный формат данных, повторите попытку')
            return True


class User(Player):
    def ask(self):
        try:
            print('Введите координаты выстрела')
            x, y = int(input('Введите координату x - ')), int(input('Введите координату y - '))
            return [x, y]
        except ValueError:
            return False

class AI(Player):
    def ask(self):
        x, y = random.randint(1, 8), random.randint(1, 8)
        return [x, y]

class Game():
    def __init__(self, user, ai):
        self.user = user
        self.ai = ai

    def greed(self):
        print('---------------МОРСКОЙ БОЙ-------------------\n'
              'Вы имеете поле размером 8 х 8 и 7 кораблей:\n'
              '1 корабль на 3 клетки\n'
              '2 корябля на 2 клетки\n'
              '4 корябля на 1 клетку\n'
              'При расстановки кораблей на карту используйте цифры от 1 до 8\n'
              'Также используйте цифры для определения поворота корабля\n'
              '1 - ↓\n'
              '2 - →\n'
              '3 - ↑\n'
              '4 - ←\n'
              'В ходе игры вы будете видеть перед собой две доски:\n'
              'Слева - ваша доска\n'
              'Справа - доска противника\n'
              'Игра продолжается до тех пор, пока у кого либо не закончатся корабли\n'
              'УДАЧИ!!!')

    def loop(self):
        self.ai.board.get_board(ai_board)
        while True:
            result = True
            while result:
                result = self.user.move()
                self.ai.board.get_board(user.board)
            if not self.user.board._coord:
                print('Вы уничтожили все корабли противника!!')
                break


            result = True
            while result:
                result = self.ai.move()
                self.ai.board.get_board(user.board)
            if not self.ai.board._coord:
                print('Противник уничтожил все ваши корабли')
                break


    def start(self):
        self.loop()

print('---------------МОРСКОЙ БОЙ-------------------\n'
              'Вы имеете поле размером 8 х 8 и 7 кораблей:\n'
              '1 корабль на 3 клетки\n'
              '2 корябля на 2 клетки\n'
              '4 корябля на 1 клетку\n'
              'При расстановки кораблей на карту используйте цифры от 1 до 8\n'
              'Также используйте цифры для определения поворота корабля\n'
              '1 - ↓\n'
              '2 - →\n'
              '3 - ↑\n'
              '4 - ←\n'
              'В ходе игры вы будете видеть перед собой две доски:\n'
              'Слева - ваша доска\n'
              'Справа - доска противника\n'
              'Игра продолжается до тех пор, пока у кого либо не закончатся корабли\n'
              'УДАЧИ!!!')

#Создаем доски игрока и компьютера
user_board = Board(True)
ai_board = Board(False)
#Создаем экземпляры игрока и компьютера, передаем им доски друг друга


user = User(ai_board)
ai = AI(user_board)

#Запускаем игру
game1 = Game(user, ai)
game1.start()

