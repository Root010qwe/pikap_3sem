def field(items, *args):
    assert len(args) > 0
    c_i = len(items)
    c_a = len(args)
    for i in range(c_i):
        for j in range(c_a):
            if args[j] in items[i] and args[j] is not None:
                yield items[i][args[j]]


if __name__ == '__main__':
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
    ]

    for ii in field(goods, 'title'):
        print(ii)
    print('\n')
    for jj in field(goods, 'title', 'price'):
        print(jj)
