lst = ['madam', 'fire', 'tomato', 'book', 'kiosk', 'mom']

new_lst = list(filter(lambda item: item == item[::-1], lst))
print(new_lst)
