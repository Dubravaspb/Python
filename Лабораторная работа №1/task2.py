disk = 1.44 * 1024 * 1024
page = 100
line = 50
symbol = 25
for_symbol = 4

lines_on_book = line * page
symbols_on_book = lines_on_book * symbol
weight_sym_on_book = symbols_on_book * for_symbol
max_books = disk // weight_sym_on_book

print("Количество книг, помещающихся на дискету:", int(max_books))
