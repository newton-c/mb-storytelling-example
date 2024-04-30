import pandas as pd
from plotnine import *

theme_ic = theme(text=element_text(family='Roboto'),
                 plot_title=element_text(color='#3B3B3B', ha='left',
                                         weight='black', size=24, margin={"t": 25, "b": 25}),
                 plot_subtitle=element_text(color='#3B3B3B', ha='left', size=19, margin={"b": 30}),
                 axis_text_y=element_text(size=15, color='#B3B3B3'),
                 axis_text_x=element_text(size=15, color='#3B3B3B'),
                 axis_ticks_y=element_line(size=0, color='white'),
                 panel_background=element_rect(fill='white'), panel_grid_major_x=None,
                 panel_grid_minor=None, axis_line_x=element_line(size=2, color='#3B3B3B'))

datos = pd.read_csv('datos/aerocertalsa.csv')

p = (ggplot(datos)
 + aes(x='fecha_publicacion', y='monto_estimado')
 + geom_line(group=1)
 + xlab('')
 + ylab('')
 + theme_ic
)

p.show()
