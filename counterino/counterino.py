def main():
    start = [0, 0, 0, 0]
    max = 3

    def f(list, res):
        print "new list", list
        return res + 1

    def check(j, list):
        if j == len(list):
            return (True, list)

        if list[j] == max:
            list[j] = 0
            return check(j + 1, list)
        else:
            list[j] += 1
            return (False, list)

    def iterate(i, res, list):
        new_res = f(list, res)

        list[i] += 1
        if list[i] > max:
            list[i] = 0
            done, list = check(i + 1, list)
            if done:
                return new_res
            else:
                return iterate(0, new_res, list)
        else:
            return iterate(i, new_res, list)

    res = iterate(0, 0, start)

    print res, "=?", (max+1)**len(start)

if __name__ == '__main__':
    main()