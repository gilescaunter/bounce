import pygame

pygame.init()

width, height = 800, 800
window = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()


class Ball:
    def __init__(self, x, y, r, mx, my):
        self.x = x
        self.y = y
        self.r = r
        self.mx = mx
        self.my = my

    def move(self):
        self.x += self.mx
        if self.x < self.r:
            self.x, self.mx = self.r, -self.mx
        if self.x > width-self.r:
            self.x, self.mx = width-self.r, -self.mx

        self.y += self.my
        if self.y < self.r:
            self.x, self.my = self.r, -self.my
        if self.y > height-self.r:
            self.y, self.my = height-self.r, -self.my

    def draw(self):
        pygame.draw.circle(window, (255, 0, 0),
                           (round(self.x), round(self.y)), self.r, 4)


b1 = Ball(200, 200, 50, 2, 0.5)
b2 = Ball(300, 200, 50, -1, -1.5)

balls = []

balls.append(b1)
balls.append(b2)

hit_count = 0
run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for ball in balls:
        ball.move()
#    b1.move()
#    b2.move()

    for i in range(len(balls)):
        for j in range(len(balls)):

            if i == j:
                break

            print("i: {},j: {}", str(i), str(j))

            ball1 = balls[i]
            ball2 = balls[j]

            v1 = pygame.math.Vector2(ball1.x, ball1.y)
            v2 = pygame.math.Vector2(ball2.x, ball2.y)
            if v1.distance_to(v2) < ball1.r + ball2.r - 2:
                hit_count += 1
                print("hit:", hit_count)

                nv = v2 - v1
                m1 = pygame.math.Vector2(ball1.mx, ball1.my).reflect(nv)
                m2 = pygame.math.Vector2(ball2.mx, ball2.my).reflect(nv)
                ball1.mx, ball1.my = m1.x, m1.y
                ball2.mx, ball2.my = m2.x, m2.y

    window.fill((127, 127, 127))
    for ball in balls:
        ball.draw()

    pygame.display.flip()
