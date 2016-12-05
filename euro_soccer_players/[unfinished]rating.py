from sqlalchemy import create_engine
import pandas as pd
from bokeh.io import show, curdoc
from bokeh.plotting import figure, output_server, output_file
from bokeh.models import HoverTool, ColumnDataSource, DatetimeTickFormatter
from bokeh.layouts import widgetbox, row
from bokeh.models.widgets import Select

engine = create_engine('sqlite:///database.sqlite')

df = pd.read_sql_query("SELECT * FROM Player_Attributes as a \
INNER JOIN (SELECT player_name, player_api_id FROM Player) \
as b ON a.player_api_id = b.player_api_id", engine)
df = df.set_index(['player_name'])
#print(df.head())
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values('date', ascending=False)
#print(df)

source = ColumnDataSource(data={
    'x'       : df.loc['Lionel Messi'].date,
    'y'       : df.loc['Lionel Messi'].overall_rating,
    'potential' : df.loc['Lionel Messi'].potential,
})

p = figure(title='Lionel Messi', x_axis_label='date', y_axis_label='overall_rating',
           plot_height=400, plot_width=700,
           tools=[HoverTool(tooltips=[('Potential', '@potential')])])

p.circle(x='x', y='y', source=source)

p.xaxis.formatter=DatetimeTickFormatter(formats=dict(
        days=["%d %B %Y"],
        months=["%d %B %Y"],
        years=["%d %B %Y"],
    ))

def update_plot(attr, old, new):
    name = name_select.value
    new_data = {
        'x': df.loc[name].date,
        'y': df.loc[name].overall_rating,
        'potential': df.loc[name].potential
    }
    p.title.text = '%d'%name
    source.data = new_data

name_select = Select(
    options=['Lionel Messi', 'Cristiano Ronaldo', 'Franck Ribery', 'Andres Iniesta', 'Zlatan Ibrahimovic'],
    value='Lionel Messi',
    title='choose the player'
)

name_select.on_change('value',update_plot)

layout = row(widgetbox(name_select), p)
curdoc().add_root(layout)
#output_file("hover.html")
show(p)
