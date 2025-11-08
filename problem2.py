def get_top_n_frequent(items, n):
    copy_of_items = items[:]
    copy_of_items.sort()
    high_frequency = 0
    frequent_item = ''
    high_frequent_items = []
    for _ in range(n):
        for item in copy_of_items:
            if copy_of_items.count(item) > high_frequency:
                high_frequency = copy_of_items.count(item)
                frequent_item = item
        if not frequent_item in high_frequent_items:
            high_frequent_items.append(frequent_item)
        for i in range(high_frequency):
            if frequent_item in copy_of_items:
                copy_of_items.remove(frequent_item)
        high_frequency = 0
    return high_frequent_items

votes = ['code', 'sleep', 'eat', 'code', 'repeat', 'eat', 'code', 'sleep']
n = 3
high_frequent_items = get_top_n_frequent(votes, n)
print(high_frequent_items)