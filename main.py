from file_reader import read_matrix
from johnson import Job, johnson_algorithm, max_downtime, time, johnson_condition
from brute_force import lexigraphic_permutations
from painter import paint

def main():
    filename = input('filename> ')
    matrix = read_matrix(filename=filename)

    # структурирование полученных из файла данных
    jobs = []
    original_jobs = []
    if len(matrix[0]) == 2:
        for i, elem in enumerate(matrix):
            jobs.append(Job(a=elem[0], b=elem[1], c=0.0, index=i))
            original_jobs.append(Job(a=elem[0], b=elem[1], c=0.0, index=i))
    elif len(matrix[0]) == 3:
        for i, elem in enumerate(matrix):
            jobs.append(Job(a=(elem[0] + elem[1]), b=(elem[1] + elem[2]),
                            c=elem[2], index=i))
            original_jobs.append(Job(a=elem[0], b=elem[1], c=elem[2], index=i))

    # Выбор метода по условию Джонсона
    if johnson_condition(original_jobs):
        print('Johnson')
        optimal_schedule = johnson_algorithm(jobs=jobs)
    else:
        print('Lexigraphic')
        optimal_schedule = lexigraphic_permutations(jobs=original_jobs)

    # просто вывод для отладки
    print(optimal_schedule)
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

    paint(jobs=optimal_schedule)

if __name__ == '__main__':
    main()
