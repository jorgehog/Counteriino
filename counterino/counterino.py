def main():
    start = [13, 12,  5, 0, 12, 13, 14]
    end =   [15, 15,  3, 1, 12, 13, 14]
    max = 15

    def process(list, res):
        print "new list", list
        return res + 1

    def iterate(j, list, count):
        if list == end:
            return (True, list, count)

        if list[j] == max:
            list[j] = 0
            return iterate(j + 1, list, count)
        else:
            list[j] += 1
            new_count = process(list, count)
            return (False, list, new_count)


    count = process(start, 0)
    list = start
    done = False
    while not done:
        (done, list, count) = iterate(0, list, count)

    print count, "values parsed"

if __name__ == '__main__':
    main()