phone_book = {"John":"123-4567","Jane":"234-5678","Max":"345-6789"}

def search():
    name = yield
    while True:
        if name in phone_book:
            phone_number = phone_book[name]
        else:
            phone_number = "Can't find your name"
        name = yield phone_number

search_coroutine = search()
next(search_coroutine)

result = search_coroutine.send("John")
print(result)

result = search_coroutine.send("Jane")
print(result)

result = search_coroutine.send("Sarah")
print(result)
