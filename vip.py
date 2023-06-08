import random

# 定义游戏地图和角色代码
MAP_WIDTH = 20
MAP_HEIGHT = 10
EMPTY = 0
TREE = 1
ROCK = 2
PLAYER = 3

# 定义角色移动方向代码
LEFT = 0
DOWN_LEFT = 1
DOWN = 2
DOWN_RIGHT = 3
RIGHT = 4
UP_RIGHT = 5
UP = 6
UP_LEFT = 7

# 定义角色移动速度和初始位置
MOVE_SPEED = 1
STARTING_ROW = 0
STARTING_COL = MAP_WIDTH // 2

class SkiGame:
    def __init__(self):
        self.map_data = []
        self.player_row = STARTING_ROW
        self.player_col = STARTING_COL
        self.score = 0
        self.game_over = False
        self.populate_map()

    def populate_map(self):
        # 随机生成游戏地图
        for row in range(MAP_HEIGHT):
            new_row = []
            for col in range(MAP_WIDTH):
                if row == 0:
                    # 第一行全为空地
                    new_row.append(EMPTY)
                else:
                    # 其他行随机生成障碍物
                    if random.randint(1, 10) == 1:
                        new_row.append(TREE)
                    elif random.randint(1, 10) == 1:
                        new_row.append(ROCK)
                    else:
                        new_row.append(EMPTY)
            self.map_data.append(new_row)

    def move_player(self, direction):
        # 根据方向代码移动角色
        if direction == LEFT:
            self.player_col -= MOVE_SPEED
        elif direction == DOWN_LEFT:
            self.player_row += MOVE_SPEED
            self.player_col -= MOVE_SPEED
        elif direction == DOWN:
            self.player_row += MOVE_SPEED
        elif direction == DOWN_RIGHT:
            self.player_row += MOVE_SPEED
            self.player_col += MOVE_SPEED
        elif direction == RIGHT:
            self.player_col += MOVE_SPEED
        elif direction == UP_RIGHT:
            self.player_row -= MOVE_SPEED
            self.player_col += MOVE_SPEED
        elif direction == UP:
            self.player_row -= MOVE_SPEED
        elif direction == UP_LEFT:
            self.player_row -= MOVE_SPEED
            self.player_col -= MOVE_SPEED

        # 判断是否触碰到障碍物或边界
        if self.player_row < 0:
            self.player_row = 0
        elif self.player_row >= MAP_HEIGHT:
            self.game_over = True
            print("游戏结束！")
        elif self.player_col < 0:
            self.player_col = 0
        elif self.player_col >= MAP_WIDTH:
            self.player_col = MAP_WIDTH - 1

        if self.map_data[self.player_row][self.player_col] == TREE:
            self.score += 10
            print("撞到了一棵树，加10分！")
            self.map_data[self.player_row][self.player_col] = EMPTY
        elif self.map_data[self.player_row][self.player_col] == ROCK:
            self.score -= 10
            print("撞到了一块石头，扣10分！")
            self.map_data[self.player_row][self.player_col] = EMPTY

    def print_map(self):
        # 打印游戏地图和角色位置
        for row in range(MAP_HEIGHT):
            for col in range(MAP_WIDTH):
                if row == self.player_row and col == self.player_col:
                    print("P", end="")
                else:
                    if self.map_data[row][col] == EMPTY:
                        print(" ", end="")
                    elif self.map_data[row][col] == TREE:
                        print("T", end="")
                    elif self.map_data[row][col] == ROCK:
                        print("*", end="")
            print()

# 创建游戏实例并运行游戏循环
game = SkiGame()
while not game.game_over:
    game.print_map()
    print("得分：", game.score)
    print("方向：左（a），下左（z），下（s），下右（x），右（d），上右（c），上（w），上左（q）")
    direction = input("请输入方向代码：")
    if direction == "a":
        game.move_player(LEFT)
    elif direction == "z":
        game.move_player(DOWN_LEFT)
    elif direction == "s":
        game.move_player(DOWN)
    elif direction == "x":
        game.move_player(DOWN_RIGHT)
    elif direction == "d":
        game.move_player(RIGHT)
    elif direction == "c":
        game.move_player(UP_RIGHT)
    elif direction == "w":
        game.move_player(UP)
    elif direction == "q":
        game.move_player(UP_LEFT)
print("最终得分：", game.score)
