from dataparser import *
from collections import *

# inp: the input file as a single string
# out: the answer file produced by your solver, as a single string
# return the score of the output as an integer
def score(inp, out):
    ns = parse(inp)
    itr = (line for line in out.split('\n'))
    # TODO: implement
    D = ni(itr)
    assert 1 <= D <= ns.T2 + ns.T3 + ns.T4
    used = set()
    c2, c3, c4 = 0, 0, 0
    tot_score = 0
    for i in range(D):
        L = nl(itr)
        no = L[0]
        assert 2 <= no <= 4
        if no == 2: c2 += 1
        if no == 3: c3 += 1
        if no == 4: c4 += 1
        pizzas = L[1:]
        assert no == len(pizzas)
        all_ingerd = []
        for p_id in pizzas:
            assert 0 <= p_id < ns.M
            assert p_id not in used
            used.add(p_id)
            p = ns.pizzas[p_id]
            all_ingerd.extend(p['ingredients'])
        no_ingred = len(set(all_ingerd))
        tot_score += no_ingred**2

    assert c2 <= ns.T2
    assert c3 <= ns.T3
    assert c4 <= ns.T4

    return tot_score


