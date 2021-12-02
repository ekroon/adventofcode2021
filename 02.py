if __name__ == '__main__':
    forward = 0
    depth1 = 0
    depth2 = 0
    aim = 0
    with open("02.txt") as f:
        for s in f:
            direction, amount = s.strip().split()
            amount = int(amount)
            match direction:
                case "forward":
                    forward += amount
                    depth2 += aim * amount
                case "down":
                    depth1 += amount
                    aim += amount
                case "up":
                    depth1 -= amount
                    aim -= amount

    print(forward * depth1)
    print(forward * depth2)
