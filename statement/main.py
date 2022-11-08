from statement import *

print('Расчет заработной платы')
print('='*50)
a = admin.Admin(1, 'Валерий Задорожный')
a.show_info()
print()
w = worker.Worker(2, 'Илья Кромин', 6)
w.show_info()
print()
m = manager.Manager(3, 'Николай Хорольский', 25)
m.show_info()
