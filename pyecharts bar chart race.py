#jupyter notebook

from pyecharts import options as opts
from pyecharts.charts import Bar, Timeline




continent=dict(zip(world['country'],world['continent']))
colors = dict(zip(world['continent'].unique(),
                  ['#adb0ff','#e48381','#90d595','#f7bb5f','#eafb50','#aafbff','#ffb3ff']))
tl = Timeline()
for i in range(len(world['date'].unique())):
    date=world['date'].unique()[i]
    data=world[world['date']==date].sort_values(by='confirm').tail(15).sort_values(by='confirm',ascending=False)
    bar = (
        Bar()
        .add_xaxis(data['country'].tolist())
        .add_yaxis('confirm',data['confirm'].tolist())
        .reversal_axis()
        .set_global_opts(xaxis_opts=opts.AxisOpts(position='top'),
                         yaxis_opts=opts.AxisOpts(is_inverse=True),
                         title_opts=(opts.TitleOpts(title='{}全球累计确诊人数前15的国家'.format(date),pos_left='center')),
                         legend_opts=(opts.LegendOpts(pos_left='right',pos_top='2%')))
        .set_series_opts(label_opts=(opts.LabelOpts(position='right',color='black')))
    )
    tl.add(bar, "{}日".format(i))
tl.add_schema(play_interval=500,is_auto_play=True,is_loop_play=False).render_notebook()
