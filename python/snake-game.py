import pygame
import time
import random

pygame.init()

blue = (50, 153, 213)
white= (255,255,255)
black= (0,0,0)
yellow = (255,255,102)
green= (0,255,0)
red = (213, 50, 80)

dis_width= 600
dis_height= 400
dis= pygame.display.set_mode((dis_width,dis_height))

pygame.display.set_caption('Snake game made by Sarthak')

clock= pygame.time.Clock()

snake_block= 10
snake_speed = 20

font_style =  pygame.font.SysFont("bahnschrift",25)
score_font= pygame.font.SysFont("comicsansms",35)

def Score(score):
	value= score_font.render("Your score: "+ str(score), True, yellow)
	dis.blit(value, [0,0])

def our_snake(snake_block, snake_list):
	for x in snake_list:
		pygame.draw.rect(dis, black, [x[0],x[1],snake_block,snake_block])

def message(msg, color):
	mes= font_style.render(msg, True, color)
	dis.blit(mes, [dis_width/6, dis_height/3])

def gameloop():

	gameover= False
	gameclose= False
	
	x1 = dis_width/2
	y1 = dis_height/2
	dx1 = 0
	dy1 = 0

	snake_list = []
	snake_length= 1

	foodx= round(random.randrange(0, dis_width - snake_block)/10.0)*10.0
	foody= round(random.randrange(0, dis_height - snake_block)/10.0)*10.0

	while not gameover:

		while gameclose== True:
			dis.fill(white)
			message("You lost! Press Q- quit or C-  play again", red)
			pygame.display.update()
			for event in pygame.event.get():
				if event.type== pygame.KEYDOWN:
					if event.key== pygame.K_q:
						gameover = True
						gameclose= False;
					if event.key== pygame.K_c:
						gameloop()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameover = True;
			if event.type == pygame.KEYDOWN :
				if event.key == pygame.K_LEFT :
					dx1 = -snake_block
					dy1 = 0
				elif event.key == pygame.K_RIGHT :
					dx1 = snake_block
					dy1 = 0
				elif event.key == pygame.K_UP :
					dx1 = 0
					dy1 = -snake_block
				elif event.key == pygame.K_DOWN :
					dx1 = 0
					dy1 = snake_block
		if x1>= dis_width or x1<0 or y1>= dis_height or y1<0:
			gameclose= True;
		x1 += dx1
		y1 += dy1	
		dis.fill(blue)		
		pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
		snake_head= []
		snake_head.append(x1)
		snake_head.append(y1)
		snake_list.append(snake_head)

		if len(snake_list)>snake_length:
			del snake_list[0]
		for x in snake_list[:-1]:
			if x== snake_head:
				gameclose= True
		our_snake(snake_block, snake_list)
		Score(snake_length-1)

		pygame.display.update()

		if x1==foodx and y1==foody:
			foodx= round(random.randrange(0, dis_width-snake_block)/10.0)*10.0
			foody= round(random.randrange(0, dis_height-snake_block)/10.0)*10.0
			snake_length+=1

		
		clock.tick(snake_speed)

	# message("You lost", red)
	# pygame.display.update()
	# time.sleep(2)
gameloop()

pygame.quit()
quit()

