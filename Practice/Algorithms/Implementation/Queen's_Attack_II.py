coorg = '''
48 36
38 46
60 24
70 14
54 36
54 24
60 30
48 30
71 50
14 97
47 31
29 68
90 10
36 85
63 24
32 13
64 57
45 57
86 19
43 86
68 72
29 25
48 59
38 78
45 16
40 92
76 85
40 10
65 16
71 18
90 40
65 45
10 37
19 82
42 56
46 60
94 14
34 36
95 49
78 67
86 23
28 12
95 57
38 19
61 49
67 42
28 25
38 28
91 20
90 86
81 19
18 43
29 69
36 20
72 75
39 50
17 92
48 25
20 79
82 57
58 50
94 70
17 19
73 20
45 12
19 89
45 12
59 74
63 71
32 23
67 85
24 25
18 61
97 50
70 37
30 10
39 90
75 58
58 34
47 62
28 28
79 34
73 80
93 36
25 45
48 75
42 13
18 69
35 21
18 87
57 19
26 92
94 34
84 48
61 95
62 89
59 74
50 40
36 37
95 62
'''
tu = []

for i in coorg.strip().split("\n"):
    k, l = i.split()
    tu.append([int(k), int(l)])

# print(tu)
# print(len(tu))

def queensAttack(n, k, r_q, c_q, obstacles):
    
    num = 0
    steps = []
    if k:
        obs = tuple(tuple(i) for i in obstacles)
    else:
        obs = ((0,0))
    print(obs)



    #one step in all possible directions
    hor_right = True
    hor_left = True
    ver_high = True
    ver_low = True
    diag_1 = True
    diag_2 = True
    diag_3 = True
    diag_4 = True

    i=1

    while hor_right or hor_left or ver_high or ver_low or diag_1 or diag_2 or diag_3 or diag_4:
        #horizontal,  row if fixed
        if hor_right:
            step = (r_q, c_q+i)
            if step in obs or (n - (c_q + i) < 0):
                hor_right = False
            else:
                num+=1

        if hor_left:
            step = (r_q,c_q-i)

            if step in obs or i == c_q:
                hor_left = False
            else:
                num+=1
        #vertical, column is fixed
        if ver_high :
            step = (r_q+i, c_q)
            if step in obs or (n - (r_q + i) < 0):
                ver_high = False
            else:
                num+=1

        if ver_low:
            step = (r_q-i, c_q)
            if step in obs or i == r_q:
                ver_low = False
            else:
                num+=1
        # diagonal
        #high, high
        if diag_1:
            step = (r_q + i, c_q+i)
            if step in obs or (n - (r_q + i) < 0) or (n - (c_q + i) < 0):
                diag_1 = False
            else:
                num += 1
        #low, low
        if diag_2:
            step = (r_q - i, c_q-i)
            if step in obs or i == r_q or i == c_q:
                diag_2 = False
            else:
                num += 1
        #diagonal
        #row high, column low
        if diag_3:
            step = (r_q + i, c_q - i)
            if step in obs or (n - (r_q + i) < 0) or i == c_q:
                diag_3 = False
            else:
                num += 1
        #row low, column high
        if diag_4:
            step = (r_q - i, c_q + i)
            if step in obs or i == r_q or (n - (c_q + i) < 0):
                diag_4 = False
            else:
                num += 1


        i+=1


    print(num)
    return num




# queensAttack(5,4, 4,3, [[5,5], [4,5], [3,4]])
# queensAttack(1, 0, 1,1, [])
queensAttack(100, 100, 54, 30, tu)


