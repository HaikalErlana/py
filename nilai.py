# Fungsi Garis
def garis():
    print("===================")
# Input Nilai
a = int(input("Nilai A : "))
b = int(input("Nilai B : "))
c = int(input("Nilai C : "))
# Urut GPU YAHUD
urut = [a,b,c]
urut.sort()
asc = sorted(urut)
des = sorted(urut, reverse=True)
# Max min rata rata
jumlah = a+b+c
max = max(a,b,c)
min = min(a,b,c)
rata = jumlah/ len(urut)
# output
print("Urut nilai ascending : ", asc)
print("Urut nilai dascending : ", des)
print("nilai max : ",max)
print("nilai min : ",min)
print("nilai rata - rata : ",int(rata))