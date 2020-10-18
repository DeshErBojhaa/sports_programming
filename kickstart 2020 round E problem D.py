from heapq import heappush, heappop
from collections import defaultdict
from math import inf, isfinite, isinf

adj = defaultdict(list)

def dijkstra():
    # heap contains tuples of (cost, city, stone). Ans is the minimum cost to make a golden stone.
    heap = []
    cost = [[inf]*STONES for _ in range(CITYS)]

    for ct, row in enumerate(av_stones):
        for stone in row:
            cost[ct][stone] = 0
            heappush(heap, (0, ct, stone))
    
    while heap:
        cur_cost, cur_ct, cur_stone = heappop(heap)
        if cur_cost >= 10**12:
            return -1
        
        if cur_stone == 0:
            return cur_cost

        # Check if moving this stone to nxt city is optimal.
        for nxt in adj[cur_ct]:
            # Moving this stone to the next city is not optimal.
            if cost[nxt][cur_stone] <= cur_cost + 1:
                continue
            cost[nxt][cur_stone] = cur_cost + 1
            heappush(heap, (cur_cost+1, nxt, cur_stone))
        
        # Try execute all recipes that includes cur_stone.
        for recipe_idx in stone_recipe[cur_stone]:
            recipe_cost, recipe_result = 0, recipes[recipe_idx][-1]
            for st in recipes[recipe_idx][:-1]:
                # Current city does not have the necessary stones. 
                if isinf(cost[cur_ct][st]):
                    break
                recipe_cost += cost[cur_ct][st]
            else:  # All the required sotnes for this recipe was available in current city.

                # It is possible that we make the golden stone here, but there can be another way
                # of making the stone which costs less.
                if cost[cur_ct][recipe_result] > recipe_cost:
                    cost[cur_ct][recipe_result] = recipe_cost
                    heappush(heap, (recipe_cost, cur_ct, recipe_result))

    return -1


def do(case):
    global CITYS, EDGES, STONES, RECIPES, av_stones, recipes, stone_recipe, adj
    CITYS, EDGES, STONES, RECIPES = map(int, input().split())
    adj = defaultdict(list)
    # Build the graph. Make junctions 0 indexed
    for _ in range(EDGES):
        u, v = map(lambda x: int(x) -1, input().split())
        adj[u].append(v)
        adj[v].append(u)

    # Take available stones present at each city
    av_stones = [list(map(lambda x: int(x) -1, input().split()))[1:] for _ in range(CITYS)]

    # Take recipes
    recipes = [list(map(lambda x: int(x)-1, input().split()))[1:] for _ in range(RECIPES)]
    
    stone_recipe = defaultdict(set)
    for i, row in enumerate(recipes):
        for st in row[:-1]:
            stone_recipe[st].add(i)
    
    print('Case #{}: {}'.format(case, dijkstra()))

T = int(input())
for i in range(1, T+1):
    do(i)
    
