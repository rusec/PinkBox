from Crypto.Util.number import long_to_bytes as l2b

def modinv(n):
    for m in range(n):
        for i in range(n):
            if (m * i) % n == 1:
                print(f"{m} inverse = {i}")
                break
        else:
            print(f"{m} has NO inverse")


def crack(n):
    x = 2
    while x * x <= n:
        if (n / x) - (n // x) < 0.00001:
            return n//x, n//(n//x)
        x += 1
    return -1, -1


def decrypt(c, n, e):
    p, q = crack(n)
    print(p)
    print(q)
    d = pow(e, -1, (p-1)*(q-1))
    return pow(c, d, n)


if __name__ == "__main__":
    c = 3026652166741331435847380600243001521651933481703538038761373416170458492115216626684753037663102602269368885768206054958187835379100718051050974108451836747046958168613166245702137273175263210215995
    n = 6827333074796409187048722169958307275709115847453291993079299161676227524768620480124254197973943459494799743688407633160146403303534680933783743111588479639661405293177994274375474507585624742623801
    e = 19
    m = decrypt(c, n, e)
    print(l2b(m).decode())
