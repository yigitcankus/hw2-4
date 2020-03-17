# ###########--1
# derece = input("Lütfen derece ya da fahrenheit giriniz:")
#
# derece_list = list(derece)
#
# c_list = []
# f_list = []
#
# if derece_list[len(derece_list)-1] == "C":
#     c_to_f = derece[0:len(derece)-1]
#     result = int((float(c_to_f) * 1.8) + 32)
#     print(result, end="F")
#
# if derece_list[len(derece_list)-1] == "F":
#     f_to_c = derece[0:len(derece)-1]
#     result = (int(f_to_c)-32)*(5/9)
#     print(round(result,1), end="C")
#
# #############--2
#
# x = input("Lütfen ters çevirmek için bir kelime yazınız:")
# print(x[::-1])
#
#
# ##########-3
# """
# 'den 50'ye kadar olan Fibonacci sayılarından oluşan birliste oluşturun.
#  İlk iki Fibonacci sayısı 1'dir. Sonraki sayılar, önceki iki sayının toplamıdır.
# """
# #1 1 2 3 8 11
# birinci = 1
# ikinci = 1
# list = [1,1]
#
# while ikinci<50:
#     temp = birinci + ikinci
#     birinci = ikinci
#     ikinci = temp
#     if ikinci<50:
#         list.append(ikinci)
# 
# print(list)
#
# ########-4
# """
# Girilen bir sayı için çarpım tablosunu yazdırın.
#
#  Örnek : Bir sayı girin : 6
#          6 x 1 = 6
#          6 x 2 = 12
#          6 x 3 = 18
#          6 x 4 = 24
#          6 x 5 = 30
#          6 x 6 = 36
#          6 x 7 = 42
#          6 x 8 = 48
#          6 x 9 = 54
#          6 x 10 = 60
# """
#
# sayi = int(input("sayi giriniz:"))
# for i in range(1,11):
#     print(sayi, "x", i, "=", sayi*i)
#
#
# ########----5
# """
# List comprehension kullanarak, 1'den 20'ye kadar tek sayıların karesini,
#                                 çift sayıların küpünü içeren bir liste oluşturun.
# """
#
# list= [x**2 if x%2==1 else x**3 for x in range (1,20)]
# print(list)
