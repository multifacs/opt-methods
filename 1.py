import pandas as pd

x_options = [0, 100, 200, 300, 400, 500, 600, 700, 800, 900]

def P(x):
    vals = [0, 150, 280, 410, 540, 660, 780, 890, 1000, 1100]
    if int(x / 100) >= len(vals):
        return -1
    return vals[int(x / 100)]
def Q(x):
    vals = [0, 10, 20, 30, 50, 70, 100]
    if int(x / 100) >= len(vals):
        return -1
    return vals[int(x / 100)]

N = 3
delta = 100
E = 300
alpha = 300

x = [x for x in range(N + 1)]
u = [x + 1 for x in range(N)]

print(x)
print(u)

def S(k, x):
    if k == 0:
        return (0, 0)
    
    def get_lower(x):
        return max(alpha - x, 0)
    def get_upper(x):
        return min(k * alpha - x, alpha + E)
    def get_possible_u(x):
        possible_u = []
        # print(k, x, k * alpha - x, alpha + E, get_lower(x), get_upper(x))
        t = get_lower(x)
        while t <= get_upper(x):
            possible_u.append(t)
            t += delta
        return possible_u
    possible_S = []
    possible_u = get_possible_u(x)
    # print("possible u", possible_u)
    
    if len(possible_u) == 0:
        return (-1, 0)

    for u in possible_u:
        # print("{} + {}  + {}".format(P(u), Q(x), S(k-1, x + u - alpha)[0]))
        if Q(x) == -1:
            return (-1, 0)
        s = P(u) + Q(x) + S(k-1, x + u - alpha)[0]
        # print("{} + {} - {}".format(x, u, alpha))
        possible_S.append(s)
    # print("possible S", possible_S)
    u = []
    min_S = min(possible_S)
    for s in enumerate(possible_S):
        if s[1] == min_S:
            u.append(possible_u[s[0]])
    return (min_S, u)

k = 3

print("k =", k)
print("k + 1 = ", k+1)
print("x idx = ", N - k)
print("u idx = ", N - k + 1)
print("S prev idx = ", k - 1)
print()

s_str = " + S{}(x{} + u{} - alpha)".format(k - 1, N - k, N - k + 1) if k - 1 > 0 else ""
print("min{{P(u{}) + Q(x{}){}}}".format(N - k + 1, N - k, s_str))
print()

c1 = "x{}".format(N - k)
c2 = "S{}(x{})".format(k, N - k)
c3 = "u*{}({})".format(N - k + 1, N - k)

df = pd.DataFrame(columns=[c1, c2, c3])
for x in [0, 100, 200, 300, 400, 500, 600, 700]:
    min_S, u = S(k, x)
    if min_S == -1:
        break
    row = [x, min_S, u]
    df.loc[len(df)] = row

print(df)