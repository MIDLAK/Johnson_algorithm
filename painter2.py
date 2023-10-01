import plotly.express as px
import pandas as pd
from johnson import Job

def paint(jobs: list[Job]) -> None:
    df = pd.DataFrame([
        dict(Task="Job A", Start='2009-01-01', Finish='2009-02-28', Resource="Alex"),
        dict(Task="Job B", Start='2009-03-05', Finish='2009-04-15', Resource="Alex"),
        dict(Task="Job C", Start='2009-02-20', Finish='2009-05-30', Resource="Max")
    ])

    fig = px.timeline(df, x_start="Start", x_end="Finish", y="Resource", color="Resource")
    fig.show()




def transform_data(jobs: list[Job]) -> list[dict]:
    lst = []
    for job in jobs:
        lst.append(dict(Task="Job A", Start='2009-01-01', Finish='2009-02-28'))
    return lst

paint([])
