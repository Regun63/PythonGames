import pygame,sys,random

def ball_anime():
      global ball_speed_x,ball_speed_y,gme_over,opponent_Score,player_Score,score_time
     
      if ball.right>=screen_width:
            
            opponent_Score+=10
            start.play()
            score_time=pygame.time.get_ticks()
      if ball.x<=0:
            
            player_Score+=10
            start.play()
            score_time=pygame.time.get_ticks()
          
            
      if ball.top<=0 or ball.bottom>=screen_height:
            ball_speed_y*=-1
      ball.x+=ball_speed_x
      ball.y+=ball_speed_y 
def restart():
      global ball_speed_x,ball_speed_y,score_time,player_Score,opponent_Score
       
      current_time=pygame.time.get_ticks()
      ball.center=(screen_width/2,screen_height/2)
      if  current_time-score_time<1000 and player_Score>opponent_Score:
            winner=game_font.render(f"{player_winner,player_Score}",True,"#FFB200")
            screen.blit(winner,(screen_width/2-200,screen_height/4))
            
            
      if  current_time-score_time<1000 and player_Score<opponent_Score:
            winner1=game_font.render(f"{opponent_winner,opponent_Score}",True,"#FFB200")
            screen.blit(winner1,(screen_width/2-200,screen_height/4))
           
            
      if  1000<current_time-score_time<2000:
            beep.play()
            winner2=style.render("3",True,"#ECFFE6")
            screen.blit(winner2,(screen_width/2-10,screen_height/4))
            
      if  2000<current_time-score_time<3000:
            
            beep.play()
            winner3=style.render("2",True,"#ECFFE6")
            screen.blit(winner3,(screen_width/2-10,screen_height/4))
            
      if  3000<current_time-score_time<4100:
            beep.play()
            winner4=style.render("1",True,"#ECFFE6")
            screen.blit(winner4,(screen_width/2-10,screen_height/4))
            player_Score,opponent_Score=0,0
       
           
      if current_time-score_time<4100:
        ball_speed_x,ball_speed_y=0,0
      else:
        ball_speed_x=7*random.choice((1,-1))
        ball_speed_y=7*random.choice((1,-1))
        score_time=False
                              
def player_anime():
      global ball_speed_x,player_Score,opponent_Score,ball_speed_y
      if player.top<=0 : 
            player.top=0
      if player.bottom>=screen_height:
            player.bottom=screen_height
            
      if ball.colliderect(player) : 
           
          if ball.right-player.left<10 and ball_speed_x>0:
            ping.play() 
            ball_speed_x*=-1
            
            player_Score+=10
            start.play()
          elif abs(ball.bottom-player.top<10) and ball_speed_y>0:
            ping.play() 
            ball_speed_y*=-1
          elif abs(ball.top-player.bottom<10) and ball_speed_y<0:
            ping.play() 
            ball_speed_y*=-1 
      if ball.colliderect(opponent): 
          if abs(ball.left-opponent.right)<10 and ball_speed_x<0: 
            ping.play() 
            ball_speed_x*=-1
            
            opponent_Score+=10
            start.play()
          elif abs(ball.bottom-opponent.top<10) and ball_speed_y>0:
            
            ping.play()
            ball_speed_y*=-1
          elif abs(ball.top-opponent.bottom<10) and ball_speed_y<0:
            ping.play()
            ball_speed_y*=-1 
               
def opponent_anime():
      if opponent.top<ball.top:
            opponent.y+=opponent_speed  
            
      if opponent.bottom>ball.bottom:
            opponent.y-=opponent_speed  
               
      if opponent.top<=0 : 
            opponent.top=0
      if opponent.bottom>=screen_height:
            opponent.bottom=screen_height
pygame.init()
screen_height=750
screen_width=1100
screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Pong Game")
clock=pygame.time.Clock()


ball=pygame.Rect(screen_width/2-15,screen_height/2-15,30,30)
player=pygame.Rect(screen_width-40,screen_height/2-70,20,140)
opponent=pygame.Rect(20,screen_height/2-70,20,140)

ball_speed_x=6 
ball_speed_y=6
player_spd=0
opponent_speed=7
player_txt="Player Score:"
opponent_txt="Opponent Score:"
player_Score=0
opponent_Score=0
gme_over=False
opponent_winner="Opponent WON!"
player_winner="You WON!"
tie="Match TIE! ;p"
score_time=False

game_font=pygame.font.Font("freesansbold.ttf",35)
style=pygame.font.Font("freesansbold.ttf",60)
song=pygame.mixer.Sound("song.mp3")
start=pygame.mixer.Sound("start.mp3")
ping=pygame.mixer.Sound("pop.mp3")
beep=pygame.mixer.Sound("beep.mp3")
ping.set_volume(1.0)
start.set_volume(0.2)
song.play()
while True:
      
      for event in pygame.event.get():
            if event.type==pygame.QUIT:
                  pygame.quit()
                  sys.exit()
            if event.type==pygame.KEYDOWN:
                  if event.key==pygame.K_DOWN:
                        player_spd+=8
                  if event.key==pygame.K_UP:
                        player_spd-=8
            if event.type==pygame.KEYUP:
                  if event.key==pygame.K_DOWN:
                        player_spd-=8
                  if event.key==pygame.K_UP:
                        player_spd+=8
      player.y+=player_spd 
      
        
      ball_anime()  
      player_anime() 
      opponent_anime()     
        
      screen.fill("#131842")
      pygame.draw.ellipse(screen,"#E4003A",ball)
      pygame.draw.rect(screen,"#C8ACD6",player)
      pygame.draw.rect(screen,"#C8ACD6",opponent)
      pygame.draw.aaline(screen,"#7776B3",(screen_width/2,0),(screen_width/2,screen_height))
      
      
      if score_time:
            restart()
      player_text=game_font.render(f"{player_txt}",True,(240,230,30))
      screen.blit(player_text,(screen_width/2+20,20))
      player_text=game_font.render(f"{player_Score}",True,(240,230,30))
      screen.blit(player_text,(screen_width/2+255,20))
      opponent_text=game_font.render(f"{opponent_Score}",True,(240,230,30))
      screen.blit(opponent_text,(screen_width/3+70,20))
      opponent_text=game_font.render(f"{opponent_txt}",True,(240,230,30))
      screen.blit(opponent_text,(screen_width/8,20))
      
      pygame.display.flip()
      clock.tick(60)