import pygame
import random

# 初始化Pygame
pygame.init()

# 游戏窗口宽高
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# 定义颜色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# 创建游戏窗口
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('滑雪大冒险')
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# 加载图像
player_image = pygame.image.load('player.png')
tree_image = pygame.image.load('tree.png')
rock_image = pygame.image.load('rock.png')
ski_image = pygame.image.load('ski.png')


# 定义游戏对象类
class GameObject:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        window.blit(self.image, (self.x, self.y))


# 定义游戏玩家类
class Player(GameObject):
    def __init__(self, x, y, image):
        super().__init__(x, y, image)
        self.speed = 5

    def move(self, direction):
        if direction == 'left':
            self.x -= self.speed
        elif direction == 'right':
            self.x += self.speed
        elif direction == 'up':
            self.y -= self.speed
        elif direction == 'down':
            self.y += self.speed

        # 碰撞检测
        self.check_collision()

    def check_collision(self):
        if self.x < 0:
            self.x = 0
        elif self.x > WINDOW_WIDTH - self.rect.width:
            self.x = WINDOW_WIDTH - self.rect.width

        if self.y < 0:
            self.y = 0
        elif self.y > WINDOW_HEIGHT - self.rect.height:
            self.y = WINDOW_HEIGHT - self.rect.height

    def check_collision_with_obstacles(self, obstacles):
        for obstacle in obstacles:
            if self.rect.colliderect(obstacle.rect):
                return True
        return False


# 定义游戏障碍物类
class Obstacle(GameObject):
    def __init__(self, x, y, image):
        super().__init__(x, y, image)
        self.speed = 2

    def move(self):
        self.y += self.speed

        # 重置位置
        if self.y > WINDOW_HEIGHT:
            self.y = -self.rect.height
            self.x = random.randint(0, WINDOW_WIDTH - self.rect.width)


# 随机生成障碍物
def generate_obstacles(count):
    def generate_obstacles(num_obstacles):
        obstacles = []
        for i in range(num_obstacles):
            obstacle_type = random.choice(OBSTACLE_TYPES)
            obstacle_image = OBSTACLE_IMAGES[obstacle_type]
            obstacle_x = random.randint(0, WINDOW_WIDTH - obstacle_image.get_width() - 10)
            obstacle_y = random.randint(-150, -50)
            obstacle_speed = random.randint(4, 8)
            obstacles.append(Obstacle(obstacle_type, obstacle_image, obstacle_x, obstacle_y, obstacle_speed))
        return obstacles


# 游戏主循环
def main_loop():
    # 初始化游戏对象
    player = Player(WINDOW_WIDTH // 2, WINDOW_HEIGHT - player_image.get_height(), player_image)
    obstacles = generate_obstacles(10)
    score = 0

    # 游戏循环标志
    is_game_over = False

    # 游戏循环
    while not is_game_over:
        # 处理事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.move('left')
                elif event.key == pygame.K_RIGHT:
                    player.move('right')
                elif event.key == pygame.K_UP:
                    player.move('up')
                elif event.key == pygame.K_DOWN:
                    player.move('down')

        # 移动障碍物
        for obstacle in obstacles:
            obstacle.move()

        # 绘制背景
        window.fill(WHITE)

        # 绘制玩家
        player.draw()

        # 绘制障碍物
        for obstacle in obstacles:
            obstacle.draw()

        # 绘制分数
        font = pygame.font.Font(None, 36)
        score_text = font.render('Score: ' + str(score), True, BLACK)
        window.blit(score_text, (10, 10))

        # 碰撞检测
        if player.check_collision_with_obstacles(obstacles):
            is_game_over = True

        # 更新分数
        score += 1

        # 更新窗口
        pygame.display.update()

    # 游戏结束
    font = pygame.font.Font(None, 72)
    game_over_text = font.render('Game Over', True, RED)
    window.blit(game_over_text, (
    WINDOW_WIDTH // 2 - game_over_text.get_width() // 2, WINDOW_HEIGHT // 2 - game_over_text.get_height() // 2))
    pygame.display.update()

    # 等待退出
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


# 启动游戏
main_loop()