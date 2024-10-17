symbol=25
storing_one_symbol=4
symbol_in_string_= 50
symbol_in_page=100
megabytes=1.44
symbol_in_book=symbol * symbol_in_string_ * symbol_in_page
bytes_ = megabytes*1024*1024
book=bytes_/storing_one_symbol/symbol_in_book
book=round(book)
print("Количество книг, помещающихся на дискету:", book)
