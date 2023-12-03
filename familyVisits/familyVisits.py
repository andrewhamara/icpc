def main():
    n, d = [int(x) for x in input().split()]

    morningMesses, afternoonClean = [], []

    for _ in range(n):
        mess, clean = [int(x) for x in input().split()]
        morningMesses.append(mess)
        afternoonClean.append(clean)

    days = [int(input()) for _ in range(d)]

    mess = 0
    messesInMorning = [0]
    for i in range(n-1):
        mess = max(0, mess + morningMesses[i] - afternoonClean[i])
        messesInMorning.append(mess)

    # backtracking
    totalDays = 0
    for x in days:
        idx = x - 1
        totalDays += 1
        while messesInMorning[idx] != 0:
            totalDays += 1
            idx -= 1
    print(totalDays)

if __name__ == "__main__":
    main()
