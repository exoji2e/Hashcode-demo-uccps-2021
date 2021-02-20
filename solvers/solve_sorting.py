import argparse
import random
from collections import *
from dataparser import parse

# inp is an input file as a single string
# return your output as a string
def solve(inp, args):
    # TODO: Solve the problem
    random.seed(args['seed'])
    ns = parse(inp)
    
    left_pizzas = []
    for i in range(ns.M):
        left_pizzas.append(i)
    
    left_pizzas.sort(key=lambda p_id: len(ns.pizzas[p_id]['ingredients']))
    
    def pick(no):
        if len(left_pizzas) < no:
            return None
        L = []
        for _ in range(no):
            p_id = left_pizzas.pop()
            L.append(p_id)
        return L
    
    teams = []
    for _ in range(ns.T2):
        pizzas = pick(2)
        if pizzas != None:
            teams.append(pizzas)

    for _ in range(ns.T3):
        pizzas = pick(3)
        if pizzas != None:
            teams.append(pizzas)
    
    for _ in range(ns.T4):
        pizzas = pick(4)
        if pizzas != None:
            teams.append(pizzas)

    out = []
    out.append(str(len(teams)))
    for team in teams:
        L = [len(team)] + team
        s = ' '.join(map(str, L))
        out.append(s)

    return '\n'.join(out)
