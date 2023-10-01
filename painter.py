import pandas as pd
import plotly.express as px
import datetime

from plotly.tools import make_subplots
from johnson import Job, downtime, downtime3

def paint(jobs: list[Job], original_jobs: list[Job]) -> None:
    schedule = transform_data(jobs, suf=' opt')
    schedule_original = transform_data(original_jobs, suf=' orig')

    df = pd.DataFrame(schedule)
    df_original = pd.DataFrame(schedule_original)

    df_concat = pd.concat([df, df_original])

    fig = px.timeline(df_concat, x_start='Start', x_end='Finish', y='Operation', color='Task')
    fig.show()

def transform_data(jobs: list[Job], suf: str) -> list[dict]:
    schedule = []
    a_timeline = 0
    b_timeline = 0
    c_timeline = 0
    downtimes = downtime(jobs)
    downtimes_3 = downtime3(jobs)
    print(downtimes_3)
    for i in range(len(jobs)):
        c_timeline += downtimes_3[i] # ожидание окончания операции B_i
        schedule.append(dict(Task='Операция ' + str(jobs[i].index),
                             Start= datetime.datetime.fromtimestamp(c_timeline).strftime('%Y-%m-%d %H:%M:%S'),
                             Finish = datetime.datetime.fromtimestamp(c_timeline + jobs[i].c).strftime('%Y-%m-%d %H:%M:%S'),
                             Operation='C'+suf))
        c_timeline += jobs[i].c

        b_timeline += downtimes[i] # ожидание окончания операции A_i
        schedule.append(dict(Task='Операция ' + str(jobs[i].index),
                             Start= datetime.datetime.fromtimestamp(b_timeline).strftime('%Y-%m-%d %H:%M:%S'),
                             Finish = datetime.datetime.fromtimestamp(b_timeline + jobs[i].b).strftime('%Y-%m-%d %H:%M:%S'),
                             Operation='B'+suf))
        b_timeline += jobs[i].b

        schedule.append(dict(Task='Операция ' + str(jobs[i].index), 
                     Start = datetime.datetime.fromtimestamp(a_timeline).strftime('%Y-%m-%d %H:%M:%S'),
                     Finish = datetime.datetime.fromtimestamp(a_timeline 
                                                           + jobs[i].a).strftime('%Y-%m-%d %H:%M:%S'),
                     Operation='A'+suf))
        a_timeline += jobs[i].a



    return schedule

