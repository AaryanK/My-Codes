# from buddha_air import BuddhaAir
# from yeti_air import YetiAir
# from shree_air import ShreeAir
# from saurya_air import SauryaAir
# from guna_air import GunaAir


# airlines={}
# b = BuddhaAir()
# b.base_login()
# airlines['BuddhaAir']=b
# b = YetiAir()
# b.base_login()
# airlines['YetiAir']=b
# b = ShreeAir()
# b.base_login()
# airlines['ShreeAir']=b
# b = SauryaAir()
# b.base_login()
# airlines['SauryaAir']=b
# b = GunaAir()
# b.base_login()
# airlines['GunaAir']=b

import new

a = new.search_for_flights('17','APR','2022','KTM','BIR')
print(a)