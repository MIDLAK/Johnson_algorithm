from typing import NamedTuple

class Job(NamedTuple):
    index: int
    a: float
    b: float
    c: float

def min_a(jobs: list[Job]) -> tuple[float, int]:
    '''Возвращает минимальную продолжительность работы на первой машине в 
    паре с её индексом'''
    mina = jobs[0].a
    mina_index = jobs[0].index
    for job in jobs:
        if job.a < mina:
            mina = job.a
            mina_index = job.index
    return (mina, mina_index)

def min_b(jobs: list[Job]) -> tuple[float, int]:
    '''Возвращает минимальную продолжительность работы на второй машине в 
    паре с её индексом'''
    minb = jobs[0].b
    minb_index = jobs[0].index
    for job in jobs:
        if job.b < minb:
            minb = job.b
            minb_index = job.index
    return (minb, minb_index)

def johnson_algorithm(jobs: list[Job]) -> list[Job]:
    '''Возвращает расписание (порядок работ относительно первончально 
    переданных данных) по переданным массивам длительностей операций на 
    первой (a) и второй (b) машинах'''
    a_schedule = []
    b_schedule = []
    while(len(jobs) != 0):
        mina, a_index = min_a(jobs=jobs)
        minb, b_index = min_b(jobs=jobs)
        if mina < minb:
            for job in jobs:
                if job.index == a_index:
                    a_schedule.append(job)
                    jobs.remove(job)
        else:
            for job in jobs:
                if job.index == b_index:
                    b_schedule.insert(0, job)
                    jobs.remove(job)
    schedule = a_schedule + b_schedule # конечное новое расписание
    return schedule

def max_downtime(jobs: list[Job]) -> float:
    '''K-функция, вычисляющая максимальный простой
    K(i) = K(i-1) + a_i - b_i'''
    max_downtime = 0
    downtime = 0
    for i in range(len(jobs)):
        if i > 0:
            downtime += jobs[i].a - jobs[i-1].b
        else:
            downtime += jobs[i].a

        if downtime > max_downtime:
            max_downtime = downtime
    return max_downtime

def downtime(jobs: list[Job]) -> list[float]:
    '''Возвращает список простоев для второй машины'''
    downtimes = [0.0] * len(jobs)
    for i in range(len(jobs)):
        a_sum = 0
        b_sum = 0
        x_sum = 0
        for j in range(i+1):
            a_sum += jobs[j].a
            if j > 0:
                b_sum += jobs[j-1].b
                x_sum += downtimes[j-1]

        downtimes[i] = max(a_sum - b_sum - x_sum, 0)
    return downtimes

def downtime3(jobs: list[Job]) -> list[float]:
    '''Возвращает список простоев для третьей машины'''
    downtime_2 = downtime(jobs) # простои второго станка по отношению к первому
    # подставляем в качестве a-задач b-задачи, увеличенные на соответствующие им
    # длительности простоя. b-задачи же заменяем на c-задачи
    jobs_offset = []
    for i in range(len(jobs)):
        jobs_offset.append(Job(a=jobs[i].b + downtime_2[i], b=jobs[i].c, c=0, 
                         index=jobs[i].index))
    downtime_3 = downtime(jobs=jobs_offset)
    return downtime_3

def time(jobs: list[Job]) -> float:
    '''Возвращает время окончания производственного процесса для двух машин'''
    time = 0
    for job in jobs:
        time += job.b
    time += max_downtime(jobs)
    return time

def time3x(jobs: list[Job]) -> float:
    '''Возвращает время окончания производственного процесса для трёх машин'''
    time = 0
    k = jobs[0].a
    h = jobs[0].b
    y_max = k + h
    for i in range(len(jobs)):
        time += jobs[i].c
        # вычисление максимального простоя K + H
        if i > 0:
            k += jobs[i].a - jobs[i-1].b
            h += jobs[i].b - jobs[i-1].c 
            if y_max < k + h:
                y_max = k + h
    return time + y_max

def johnson_condition(jobs: list[Job]) -> bool:
    '''Проверка условия Джонсона для трёх машин, т.е. все операции на второй машине 
    по длительности меньше любой операции на первой или третьей'''

    # поиск минимумов среди операций a и c и максимума среди операций b
    a_min = jobs[0].a
    b_max = jobs[0].b
    c_min = jobs[0].c
    for job in jobs:
        if job.a < a_min:
            a_min = job.a
        if job.b > b_max:
            b_max = job.b
        if job.c < c_min:
            c_min = job.c
    
    # проверка условия Джонсона
    if a_min >= b_max or c_min >= b_max:
        return True
    else:
        return False
