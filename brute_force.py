from johnson import Job, time3x
from itertools import permutations

# TODO: Написать алгоритм самому
def lexigraphic_permutations(jobs: list[Job]) -> list[Job]:
    perms = list(permutations(jobs))
    min_time = time3x(list(perms[0]))
    optimal_schedule = []
    for p in perms:
        t = time3x(list(p))
        if t < min_time:
            optimal_schedule.insert(0, list(p))
            min_time = t
    return optimal_schedule[0]

    
    
