import random

# 生成随机地图
def generate_map(rows, cols):
    map = []
    for row in range(rows):
        row_map = []
        for col in range(cols):
            if random.random() < 0.2:
                row_map.append('#')
            else:
                row_map.append('.')
        map.append(row_map)
    map[0][0] = 'S'
    map[rows-1][cols-1] = 'E'
    return map

# 人物类
class Player:
    def __init__(self):
        self.row = 0
        self.col = 0
        self.health = 100

    def move(self, row, col):
        self.row = row
        self.col = col
        if MAP[self.row][self.col] == '#':
            self.health -= 10

# 游戏类
class Game:
    def __init__(self):
        self.player = Player()
        self.game_over = False

    def run(self):
        while not self.game_over:
            self.display_map()
            self.get_input()
            self.check_game_over()

        if self.player.health <= 0:
            print('你输了！')
        else:
            print('你赢了！')

    def display_map(self):
        for row in range(len(MAP)):
            for col in range(len(MAP[row])):
                if row == self.player.row and col == self.player.col:
                    print('P', end=' ')
                else:
                    print(MAP[row][col], end=' ')
            print()

    def get_input(self):
        direction = input('请输入方向（上下左右）：')
        if direction == '上':
            self.player.move(self.player.row-1, self.player.col)
        elif direction == '下':
            self.player.move(self.player.row+1, self.player.col)
        elif direction == '左':
            self.player.move(self.player.row, self.player.col-1)
        elif direction == '右':
            self.player.move(self.player.row, self.player.col+1)

    def check_game_over(self):
        if MAP[self.player.row][self.player.col] == 'E':
            self.game_over = True
        elif self.player.health <= 0:
            self.game_over = True
            print('你的生命值耗尽了！')

# 生成地图
MAP = generate_map(10, 10)

# 开始游戏
game = Game()
game.run()
