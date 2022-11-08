from statement import *

a = admin.Admin(1, 'Валерий Задорожный')
a.show_info()

w = worker.Worker(2, 'Илья Кромин', 6)
w.show_info()

m = manager.Manager(3, 'Николай Хорольский', 25)
m.show_info()
