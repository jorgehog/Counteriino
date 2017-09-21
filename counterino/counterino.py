max = 15


def iterate(list, j=0):
    if list[j] == max:
        list[j] = 0
        return iterate(list, j + 1)
    else:
        list[j] += 1
        return list


def main():
    now = [13, 12, 5, 0, 12, 13, 14]
    end = [15, 15, 3, 1, 12, 13, 14]

    while now != end:
        now = iterate(now)
        print "new list", now

if __name__ == '__main__':
    main()
