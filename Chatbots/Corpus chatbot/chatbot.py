from chatterbot import ChatBot 
from chatterbot.trainers import ChatterBotCorpusTrainer 
 
bot = ChatBot('jp')
 
trainer = ChatterBotCorpusTrainer(bot)
 
trainer.train(
    "chatterbot.corpus.english"
)
 
print('Hi, and welcome! ask me something!\n')
 
while True:
  inp = input('\nYou:')
  if inp =='done':
    break
  else:
    response = bot.get_response(inp)
    print('\n\n\t\t\tBot:',response)
