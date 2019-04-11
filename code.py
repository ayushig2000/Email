import smtplib 
  
gmail = smtplib.SMTP('smtp.gmail.com', 587) 
  
gmail.starttls() 
  
# Authentication 
gmail.login("ayushig4072@gmail.com", "Password") 
  
# message to be sent 
content = "Hi....This is Ayushi. I started myself from ESC101 and slowly developed interest in coding so here i am, applying for this project. Although i am not that much experienced but an enthusiastic newbie who wanna challenge herself. After learning C i was quite fascinated to code in some other language so i started with basic CPP and python. Honestly mene bahut socha ki me aisa 'Humourous' content kya likhu and i ended up desribing myself. PS Late submission hai....kaafi mehnat....so now i want this project. "
  
# sending the mail 
gmail.sendmail("ayushig4072@gmail.com", "kushgpt99@gmail.com", content) 
  

gmail.quit() 
