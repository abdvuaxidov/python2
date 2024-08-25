# son1 = float(input("BIrinch son krt\n>"))
# son2 = float(input("Ikinchi son krt\n>"))
# # qoshams = son1 + son2
# # qoshams2 = son1 - son2
# # qoshams3 = son1 * son2
# # qoshams4 = son1 / son2
# # print(qoshams)
# # print(qoshams2)
# # print(qoshams3)
# # print(qoshams4)
# # print(f"{son1} + {son2} = " ,son1+son2)
# # print(f"{son1} - {son2} = " ,son1-son2)
# # print(f"{son1} * {son2} = " ,son1*son2)
# # print(f"{son1} / {son2} = " ,son1/son2)



# s_odamlar = ['Abu bakr','Umab Ibn Xatob','Usmon','Ali']
# t_odamlar = ['Abudllox Domla','Matrudiy','Abu Xanifa','Buxoriy']
# print(f"Man saxobalardan {s_odamlar.pop(1).title()} va {s_odamlar.pop(0).title()} bn suxbat qlgm kevoti")
# print(f"Man tarixiy odamlardan {t_odamlar.pop(2).title()} va {s_odamlar.pop(1).title()} bn suxbat qlgm kevoti")



# dostlar = []
# dostlar.append('Abu Bakir As Sidiq')
# dostlar.append('Umar Ibn Xatob')
# dostlar.append('Usmon Ibn Affon')
# dostlar.append('Ali Ibn Abu Tolib')
# print(dostlar)



# davlatlar = ['Saudiya arabiston','Dubai','Makka',"America",'Canada']
# print(len(davlatlar))
# davlatlar.sort()
# print(davlatlar)
# davlatlar.sort(reverse=True)
# print(davlatlar)
# print(sorted(davlatlar))
# print(sorted(davlatlar , reverse=True))



# son = list(range(120,1200,10))
# print(sum(son))
# print(max(son)+min(son))




# ism = ['Abu bakr','Umab Ibn Xatob','Usmon','Ali','Abu Xanifa']
# for imomlar in ism:
#     print(f"Assalomu aleykum {imomlar}")
# print(f"ism {len(ism)} marta qaytarildi")

# oyla = ['adamla','oyimla','akam','man','sinm']
# for bzani_oyla in oyla:
#     print(f"bizani oyalada {bzani_oyla.title()} bor")
# print(f"ismilar {len(oyla)} marta qaytarldi")



# sonlar = list(range(11,100,2))
# for son in sonlar:
#     print(son**3)
# print(f"sonlarni uzunligi {len(sonlar)}")



# kinolar = []
# print("5 ta eng sevmli kinoin nma?")
# for film in range(5):
#     kinolar.append(input(f"{film+1} kino\n>"))
# print(f"sizninga en sevmli 5 ta kinoyis bu {kinolar}")



# odam = int(input('Bugun neshta odam bn suxbat qldn?\n>'))
# ismlar = []
# for ism in range(odam):
#     ismlar.append(input(f"{ism+1} suxbat qlgan odam kmidi?\n>"))
# print(ismlar)



# familiya = input("Familiyen?\n>")
# ism = input('Ismin?\n>')
# print(f"{familiya.title()} {ism.title()}")
# suxbat = int(input(f"Bugun neshta odam bn suxbat qldn {ism.title()}?\n>"))
# ismlar = []
# for suxbat_qlgan_odamlar in range(suxbat):
#     ismlar.append(input(f"{suxbat_qlgan_odamlar+1} suxbat qlgani odamlarini Ismi nmedi?\n>"))
# print(f"San suxbat qlgan odamlarni ismi {ismlar}")
# yosh = int(input("Ularni yoshi nechida\n>"))
# suxbatagi_odamlar = input('Ularni familiyasi\n>')
# tel = input('Telefon nomeri\n>')
# shaxar = input('Qata turadi ula?\n>')



# ism = input("Ismingizni krting:\n>")
# if ism.lower() !="asror" :
#     print(f"Uzr {ism.title()} biza Asror kutvomiz")
# else:
#     print("Salom Asror")

# ism = input("Ismini krt\n>")
# if ism.lower() == 'asror':
#     print('Salom Asror')
# elif ism.lower() == 'nodi':
#     print('Salom Nodi')
# else:
#     print(f"Uzur {ism.title()} biza Asror yoki Nodi kutvoms")



# javob = int(input("15x4 nechi boladi?\n>"))
# if javob != 60:
#     print("Notori")
# else:
#     print("Tori")



# login = input('Login krt\n>')
# if len(login) <=5:
#     print("Login 6 harftan kam bolshi mumkumas")
# elif len(login) >=12:
#     print("login 12 tadan kop bolshi mumkumas")
# else:
#     print("Login tori") 



# yil = int(input("Yilingizni krtng\n>"))
# yosh = 2024- yil
# if yosh <18:
#     qolgan_yil = 18-yosh
#     print(f"Sizning yoshingiz {yosh} da ekan")
#     print(f"{qolgan_yil} yildan kn harakat qlp koring")
#     print('Szga mumkunmas')
# elif yosh >65:
#     qolgan_yil = yosh - 65
#     print(f"Sizning yoshingiz {yosh} da ekan")
#     print(f"{qolgan_yil} yil oldn harakat qlp korshingiz keragidi")
#     print('Sznin yoshingiz kota szga mumkumas')
# else:
#     print('Yoshingiz tori keldi szga mumkun')



# email = input('Email kiriting:\n>')
# login = input("Login krting\n>")
# if login.lower() == 'admin':
#     print('Hush kelipsiz admin, royhati koraszmi?')
# elif login.lower() == 'asror':
#     print('Hush kelipsiz asror, royhati koraszmi?')
# elif login.lower() == 'nodi':
#     print('Hush kelipsiz nodi, royhati koraszmi?')
# else:
#     print(f"Hush kelpsz {login.title()}")



# yosh = int(input('Yoshingzni kriting:\n>'))
# if yosh <= 4:
#     print('Szga bepul')
# elif yosh <= 12:
#     print('Szga krsh 10 sum')
# elif yosh <=18:
#     print('Szga krsh 15')
# else:
#     print('Szga krsh 20')

# yosh = int(input('Yoshingizni krting:\n>'))
# if yosh <= 4:
#     narx = 'Bepul'
# elif yosh <=12:
#     narx = 10
# elif yosh <=18:
#     narx = 15
# else:
#     narx = 20
# print(f'Szga krish {narx}')



# kun = input('Bugun qanaqa kun?\n>')
# if kun.lower() == 'shanba' or kun.lower() == 'yakshanba':
#     print(f'Bugun {kun.title()} dam olshi kuni')
# elif kun.lower() == 'juma':
#     print(f'Bugun {kun.title()} jumaga borams')
#     print('Jumadan kn ishga')
# else:
#     print(f'BUgun {kun.title()} ish kuni')



menu = ['hot dog','gamburberg','pizza','lavash']
zakas = input('Nma zakas qlasz\n>')
if zakas.lower() in menu:
    print('Zakas olndi')
else:
    print('Bu taom yoq bzada')

print('hello')
