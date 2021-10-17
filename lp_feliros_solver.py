# max_p min_q p*C*q^T = max_p min_j p*C*e_j^T

#max_p min{p1*c1_1 + p2*c2_1 + p3*c3_1, p1*c1_2 + p2*c2_2 + p3*c3_2, p1*c1_3 + p2*c2_3 + p3*c3_3}

# 0 <= p1, p2, p3
# p1 + p2 + p3 = 1
# t <= p1*c1_1 + p2*c2_1 + p3*c3_1
# t <= p1*c1_2 + p2*c2_2 + p3*c3_2
# t <= p1*c1_3 + p2*c2_3 + p3*c3_3
# max t

# ez easy lol

def column(matrix, i):
    return [row[i] for row in matrix]

def egyenlotlenseg(vektor):
    e = ""
    for c in vektor:
        e += f"{c}p{vektor.index(c)+1}"
        if c != vektor[-1]:
            e += "+"
    return e

def korlatok(C):
    for i in range(len(C)):
        print(f"t ≤ {egyenlotlenseg(column(C, i))}")

def pi(C):
    e = "0 ≤ "
    f = ""
    for i in range(len(C)):
        e += f"p{i+1}"
        f += f"p{i+1}"
        if i != len(C)-1:
            e += ", "
            f += "+"
    f += " = 1"
    return e, f

def solve(C):
    e, f = pi(C)
    print(e)
    print(f)
    korlatok(C)
    print("t -> max")


C = [
    [1, 2, 3],
    [4, 3, 5],
    [2, 3, 4]
    ]

solve(C)

