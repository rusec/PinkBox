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
        if n % x == 0:
            return x, n//x
        x += 1
    return -1, -1


def decrypt(c, n, e):
    p, q = crack(n)
    print(p)
    print(q)
    d = pow(e, -1, (p-1)*(q-1))
    return pow(c, d, n)


def rabin_miller(n):
    """From https://github.com/cheran-senthil/PyRival/blob/master/pyrival/algebra/is_prime.py
    
    Args:
        n (int): Number to check is prime (as long as n < 10^18)

    Returns:
        bool: True if number is prime, False otherwise
    """

    if n < 5 or n & 1 == 0 or n % 3 == 0:
        return 2 <= n <= 3
    s = ((n - 1) & (1 - n)).bit_length() - 1
    d = n >> s
    for a in [2, 325, 9375, 28178, 450775, 9780504, 1795265022]:
        p = pow(a, d, n)
        if p == 1 or p == n - 1 or a % n == 0:
            continue
        for _ in range(s):
            p = (p * p) % n
            if p == n - 1:
                break
        else:
            return False
    return True


if __name__ == "__main__":
    # I'm totally secure
    c = 3026652166741331435847380600243001521651933481703538038761373416170458492115216626684753037663102602269368885768206054958187835379100718051050974108451836747046958168613166245702137273175263210215995
    n = 6827333074796409187048722169958307275709115847453291993079299161676227524768620480124254197973943459494799743688407633160146403303534680933783743111588479639661405293177994274375474507585624742623801
    e = 19
    m = decrypt(c, n, e)
    print(l2b(m).decode())
