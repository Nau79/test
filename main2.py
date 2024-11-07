# TODO Найдите количество книг, которое можно разместить на дискете

volume_of_disk=1.44
count_of_pages=100
number_of_row=50
count_of_symbol=25
size_of_symbol=4
size_of_book=count_of_pages*50*25*4/1024/1024
count_of_books=int(volume_of_disk/size_of_book)

print("Количество книг, помещающихся на дискету:", count_of_books)
