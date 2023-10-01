import pandas as pd
import plotly.express as px
import datetime
from johnson import Job, downtime, downtime3

def paint(jobs: list[Job]) -> None:
    schedule = transform_data(jobs)

    df = pd.DataFrame(schedule)

    fig = px.timeline(df, x_start='Start', x_end='Finish', y='Resource', color='Task')
    fig.show()

def transform_data(jobs: list[Job]) -> list[dict]:
    schedule = []
    a_timeline = 0
    b_timeline = 0
    c_timeline = 0
    downtimes = downtime(jobs)
    downtimes_3 = downtime3(jobs)
    print(downtimes_3)
    for i in range(len(jobs)):
        schedule.append(dict(Task='Операция ' + str(jobs[i].index), 
                     Start = datetime.datetime.fromtimestamp(a_timeline).strftime('%Y-%m-%d %H:%M:%S'),
                     Finish = datetime.datetime.fromtimestamp(a_timeline 
                                                           + jobs[i].a).strftime('%Y-%m-%d %H:%M:%S'),
                     Resource='A'))
        a_timeline += jobs[i].a

        b_timeline += downtimes[i] # ожидание окончания операции A_i
        schedule.append(dict(Task='Операция ' + str(jobs[i].index),
                             Start= datetime.datetime.fromtimestamp(b_timeline).strftime('%Y-%m-%d %H:%M:%S'),
                             Finish = datetime.datetime.fromtimestamp(b_timeline + jobs[i].b).strftime('%Y-%m-%d %H:%M:%S'),
                             Resource='B'))
        b_timeline += jobs[i].b


        c_timeline += downtimes_3[i] # ожидание окончания операции B_i
        schedule.append(dict(Task='Операция ' + str(jobs[i].index),
                             Start= datetime.datetime.fromtimestamp(c_timeline).strftime('%Y-%m-%d %H:%M:%S'),
                             Finish = datetime.datetime.fromtimestamp(c_timeline + jobs[i].c).strftime('%Y-%m-%d %H:%M:%S'),
                             Resource='C'))
        c_timeline += jobs[i].c
    return schedule

