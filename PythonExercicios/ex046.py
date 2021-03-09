from time import sleep
from emoji import emojize
for c in range(10, 0, -1):
    sleep(1)
    print(c)
sleep(1)
print(emojize(':fireworks: \033[31mFELIZ ANO NOVO!\033[m :fireworks:'))
