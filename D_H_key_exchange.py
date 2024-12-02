# 判断一个数是否为素数
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# 求模指数
def mod_exp(base, exp, mod):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result


# 寻找原根
def find_primitive_root(p):
    if not is_prime(p):
        return None
    # 尝试从 2 到 p-1 中找到一个原根
    for g in range(2, p):
        if all(mod_exp(g, (p - 1) // f, p) != 1 for f in range(2, p)):
            return g
    return None


# 主函数实现DH密钥交换
def diffie_hellman(p, g):
    # Alice 选择私钥 a
    a = 45  # Alice 的私钥
    # Bob 选择私钥 b
    b = 56  # Bob 的私钥

    # Alice 计算公钥 A = g^a % p
    A = mod_exp(g, a, p)
    # Bob 计算公钥 B = g^b % p
    B = mod_exp(g, b, p)

    print(f"Alice 选择的私钥 a: {a}")
    print(f"Bob 选择的私钥 b: {b}")
    print(f"公钥 A (Alice): {A}")
    print(f"公钥 B (Bob): {B}")

    # Alice 使用 Bob 的公钥 B 计算共享密钥 sA = B^a % p
    sA = mod_exp(B, a, p)
    # Bob 使用 Alice 的公钥 A 计算共享密钥 sB = A^b % p
    sB = mod_exp(A, b, p)

    print(f"Alice 计算的共享密钥 sA: {sA}")
    print(f"Bob 计算的共享密钥 sB: {sB}")

    if sA == sB:
        print(f"成功！双方的共享密钥是: {sA}")
    else:
        print("共享密钥计算失败，检查公钥或私钥")


# 选择一个合适的素数 p 和原根 g (范围在 100 到 255 之间)
p = 211  # 素数 p
g = 2  # 原根 g

# 输出DH密钥交换的全过程
diffie_hellman(p, g)

'''
Alice 选择的私钥 a: 45
Bob 选择的私钥 b: 56
公钥 A (Alice): 12
公钥 B (Bob): 100
Alice 计算的共享密钥 sA: 1
Bob 计算的共享密钥 sB: 1
成功！双方的共享密钥是: 1
'''