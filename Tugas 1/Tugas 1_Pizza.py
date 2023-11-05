#Tampilan awal untuk menyambut pelanggan
print('==============================>')
print('SELAMAT DATANG DI PIZZA HUT')
print('Order Now! Delivery & Takeaway')
print('==============================>')

#Deklarasi dictionary dan list toping pizza didalam dictionary
toping_pizza = {
    1: 'Frankfurter BBQ',
    2: 'Meat Monsta',
    3: 'Super Supreme',
    4: 'Super Supreme Chicken',
    5: 'Meat Lovers',
    6: 'Chicken Lovers',
    7: 'Cheese Lovers',
    8: 'American Favourite'
}

#Deklarasi dictionary dan list crust pizza didalam dictionary
crust_pizza = {
    1: 'Pan',
    2: 'StuffedCrust Cheese',
    3: 'StuffedCrust Sausage',
    4: 'Cheesy Bites',
    5: 'Crown Crust'
}

#Deklarasi dictionary dan size toping pizza didalam dictionary
size_pizza = {
    1: 'Personal',
    2: 'Regular',
    3: 'Large'
}

#Menampilkan daftar pilihan toping pizza yang tersedia
print("Daftar Pilihan Topping Pizza:")
for key, value in toping_pizza.items(): #Melakukan perulangan dari semua list data yang berada didalam dictionary topping_pizza
    print(f"{key}: {value}") #Menampilkan pilihan toping pizza yang berada didalam dictionary

#Memasukkan input toping berupa integer
print('----------------------------------------------------------')
input_toping = int(input('Silahkan Memilih Toping Pizza Yang Anda Inginkan! (1-8): '))
print('----------------------------------------------------------')

#Menampilkan daftar pilihan crust pizza yang tersedia 
print("Daftar Pilihan Crust Pizza:")
for key, value in crust_pizza.items(): #Melakukan perulangan dari semua list data yang berada didalam dictionary crust_pizza
    print(f"{key}: {value}") #Menampilkan pilihan crust pizza yang berada didalam dictionary

#Memasukkan input crust berupa integer
print('---------------------------------------------------------')
input_crust = int(input('Silahkan Memilih Crust Pizaa yang Anda Inginkan! (1-5): '))
print('---------------------------------------------------------')

#Menampilkan daftar pilihan size pizza yang tersedia 
print("Daftar Pilihan Size Pizza:")
for key, value in size_pizza.items(): #Melakukan perulangan dari semua list data yang berada didalam dictionary size_pizza
    print(f"{key}: {value}") #Menampilkan pilihan size pizza yang berada didalam dictionary

#Memasukkan input size pizza berupa integer
print('--------------------------------------------------------')
input_size = int(input('Silahkan Memilih Size Pizaa yang Anda Inginkan! (1-3): '))
print('--------------------------------------------------------')
#Memasukkan input Y/N untuk menambah extra cheese
input_extra_cheese = input('Apakah Anda Ingin Menambahkan Extra Cheese? (Y/N) ')
print('---------------------------------------------------')

#Deklarasi harga awal yang berisi 0
harga = 0

#Menghitung harga crust nomor 1 menggunakan if elif dan else
if input_crust == 1: #inputan pan crust
    total_harga = 43637 # harga pan crust
    if input_size == 1: 
        total_harga += 0 #harga size personal
    elif input_size == 2:
        total_harga += 57273 #harga size regular
    else:
        total_harga += 89091 #harga size large

#Menghitung harga crust nomor 2 menggunakan if elif dan else
elif input_crust == 2: #inputan stuffedCrust Cheese
    total_harga = 55455 #harga stuffedCrust Cheese
    if input_size == 1:
        total_harga += 0 #harga size personal
    elif input_size == 2:
        total_harga += 65455 #harga size regular
    else:
        total_harga += 104545 #harga size large

#Menghitung harga crust nomor 3 menggunakan if elif dan else
elif input_crust == 3: #inputan StuffedCrust Sausage
    total_harga = 52728 #harga StuffedCrust Sausage
    if input_size == 1:
        total_harga += 0 #harga size personal
    elif input_size == 2:
        total_harga += 64545 #harga size regular
    else:
        total_harga += 102727 #harga size large

#Menghitung harga crust nomor 4 menggunakan if elif dan else
elif input_crust == 4: #inputan Cheesy Bites
    total_harga = 57273 #harga Cheesy Bites
    if input_size == 1:
        total_harga += 0 #harga size personal
    elif input_size == 2:
