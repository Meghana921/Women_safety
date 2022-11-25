import telepot


bot = telepot.Bot('5540649911:AAFY95Ly6ZdUuVdFxnvRFw7h9YQU2aQGQG4')
bot.sendMessage('1056518640', str('Emergency at http://www.google.com/maps/?q={},{}'.format('13.0379','77.6190')))
bot.sendPhoto('1056518640', photo=open('frame.png', 'rb'))
