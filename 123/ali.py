#avtolar=['audi','bmw','volvo','kiya']
#
#for avto in avtolar:
#    if avto == 'bmw':
#        print(avto.upper())
#    else:
#        print(avto.title())




#ism=input('ismingiz nima?\n>>>')
#if ism.lower() != 'ali':
#       print(f"Uzr,{ism.title()} biz Alini kutyapmiz.")
#else:
#      print("salom, Ali")



#javob=float(input("12*9 nechiga teng?\n>>>"))
#if javob!=72:
#       print("Javop xato!")




#yosh=int(input("Yoshingiz nechida?\n>>>>>"))
#if yosh>=18:
#      print("hush kelibsz")
#else:
#      print("kirish mumkin emas!") 



#login=input("yangi login tanlang:")
#if len(login)<=5:
#     print("login 5 harfdan ko'proq bo;lishi shart!")




#yil=int(input("tug'ilgan yilingizni kiriting:"))
#if 2022-yil<18:
#        print(f"yoshingiz {2022-yil}da ekan.")
#        print("kirish mumkin emas!")
#else:
#         print("hush kelibsz!")



#yosh=int(input("yoshingiz nechida?>>>>"))
#if yosh>70: print("siz COVID-19 risk guruhuda ekansiz")


#x,y = 40,20
#print("x>y") if x>y else print("x<y")



#son=50
#if son<0:
#     print("manfiy son")
#else:
#     print("manfiy son")
      


#yosh=int(input('yoshingiz nechida? '))
#if yosh<=4:
#       print('sizga kirish bepul.')
#elif yosh<=10:
#       print('sizga kirish 5000 so\'m')
#else:
#       print('sizga kirish 10000so\'m') 





#yosh=int(input('yoshingiz nechida? '))
#if yosh<=4:
#       narh=0
#elif yosh<=10:
#       narh=8000
#else:
#       narh=10000 
#print(f"sizga kirish {narh} so'm")




#kun=input("bugun nma kun>>>")
#if kun.lower()=='shanba' or kun.lower()=='yakshanba':
#          print('bugun dam olish kuni.')
#else:
#          print('bugun ish kuni.')




#kun=input("bugun nma kun>>>")
#harorat=float(input("havo harorati qanday"))
#
#if (kun.lower()=='yakshanba' or kun.lower()=='shanba') and harorat>=30:
#          print('chomilgani ketdik')
#elif( kun.lower()=='yakshanba'or kun.lower()=='shanba') and harorat<30:          
#          print('uyda dam olamiz')




#narh =15000
#choy=t=True
#salat=True
#
#if choy and salat:
#      narh=narh+10000
#elif choy or salat:
#      narh=narh+5000
#print(f"Jami {narh} so'm")




#narh =15000
#choy=t=1
#salat=0
#non=1
#kompot=1
#assorti=1
#
#if choy:
#      print("mijoz choy oldi.")
#      narh=narh+3000
#if salat:
#      print("mijoz salat oldi.")
#      narh=narh+5000
#if non:
#      print("mijoz non oldi.")
#      narh=narh+2000
#if kompot:
#      print("mijoz kompot oldi.")
#      narh=narh+5000
#if assorti:
#      print("mijoz assorti oldi.")
#      narh=narh+15000

#print(f"jami {narh} so'm")



#menu=['osh','orama','shashlik','norin','somsa']
#ovqat=input('nima ovqat yeysz>>>')
#if ovqat.lower() not in menu:
#       print('afsuski bizda bunday ovqat yo\'q')
#else:
#       print('buyurtma qabul qlindi')
       



menu=['osh','orama','shashlik','norin','somsa']
buyurtmalar=["osh","somsa","monti","shashlik"]

if buyurtmalar:
  for taom in buyurtmalar:
      if taom in menu:
           print(f"menuda {taom} bor")
else:
           print(f"kechirasiz,menuda {taom} yo'q")








for n in range(10):
      print(n+1)
































