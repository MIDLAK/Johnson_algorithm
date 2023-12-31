from file_reader import read_matrix
from johnson import Job, johnson_algorithm, max_downtime, time, johnson_condition, time3x
from brute_force import lexigraphic_permutations
from painter import paint

def main():
    filename = input('filename> ')
    matrix = read_matrix(filename=filename)

    # структурирование полученных из файла данных
    jobs = []
    original_jobs = []
    jobs_copy = []
    if len(matrix[0]) == 2:
        for i, elem in enumerate(matrix):
            jobs.append(Job(a=elem[0], b=elem[1], c=0.0, index=i))
            original_jobs.append(Job(a=elem[0], b=elem[1], c=0.0, index=i))
            jobs_copy.append(Job(a=elem[0], b=elem[1], c=0.0, index=i))
    elif len(matrix[0]) == 3:
        for i, elem in enumerate(matrix):
            jobs.append(Job(a=(elem[0] + elem[1]), b=(elem[1] + elem[2]),
                            c=elem[2], index=i))
            original_jobs.append(Job(a=elem[0], b=elem[1], c=elem[2], index=i))
            jobs_copy.append(Job(a=elem[0], b=elem[1], c=elem[2], index=i))

    # Выбор метода по условию Джонсона
    if johnson_condition(original_jobs) or len(matrix[0]) == 2:
        print('Method: Johnson')
        johnson_schedule = johnson_algorithm(jobs=jobs)
        optimal_schedule = []
        for i in range(len(johnson_schedule)):
            for j in range(len(jobs_copy)):
                if johnson_schedule[i].index == jobs_copy[j].index:
                    optimal_schedule.append(jobs_copy[j])
    else:
        print('Method: Lexigraphic')
        optimal_schedule = lexigraphic_permutations(jobs=original_jobs)

    if len(matrix[0]) == 2:
        t = time(original_jobs)
        opt_time = time(optimal_schedule)
        print(f'T(s_orig) = {t}')
        print(f'T(s_opt) = {opt_time}')
    elif len(matrix[0]) == 3:
        t = time3x(original_jobs)
        opt_time = time3x(optimal_schedule)
        print(f'T(s_orig) = {t}')
        print(f'T(s_opt) = {opt_time}')


    # просто вывод для отладки
    #print(optimal_schedule)
    #print(original_jobs)
    #max_start_downtime = max_downtime(jobs=jobs)
    #start_time = time(jobs=jobs)
    #optimal_schedule = johnson_algorithm(jobs=jobs)
    #optimal_time = time(jobs=optimal_schedule)
    #max_optimal_downtime = max_downtime(jobs=optimal_schedule) 
    #print(f'start_downtime={max_start_downtime}, opt_downtime={max_optimal_downtime}')
    #print(f'start_time={start_time}, optimal_time={optimal_time}')
    #print(original_jobs)
    #print(optimal_schedule)
    # конец просто вывода для отладки

    paint(jobs=optimal_schedule, original_jobs=original_jobs)

if __name__ == '__main__':
    main()
