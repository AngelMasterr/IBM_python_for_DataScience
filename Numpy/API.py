# API: Application Program Interfaces
# Una API permite que dos piezas de software se comuniquen entre sí.

from randomuser import RandomUser
import pandas as pd

# RandomUsers(): crea una lista de usuarios random
r = RandomUser()
some_list = r.generate_users(10)

# get_full_name(): crean nombnres para cada usuario
for user in some_list:
    print (user.get_full_name()," ",user.get_email())

# get_full_name(): crean fotos para cada usuario
for user in some_list:
    print (user.get_picture())
    
  