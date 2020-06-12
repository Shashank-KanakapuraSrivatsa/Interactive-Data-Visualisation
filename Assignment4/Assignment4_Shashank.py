import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

##----------------------------------------------------------------------------##
#Read CSV file
df = pd.read_csv('DataWeierstrass.csv',sep=';')
##----------------------------------------------------------------------------##

##----------------------------------------------------------------------------##
#Restructure the string values so that it can be used meaningfully in the plot
#Reference: https://stackoverflow.com/questions/33413249/how-to-remove-string-value-from-column-in-pandas-dataframe
df['professor'] = df.professor.str.replace('prof?','')
df['lecture'] = df.lecture.str.replace('lecture?','')
##----------------------------------------------------------------------------##

##----------------------------------------------------------------------------##
#Values of lecture should be converted to integers in order to plot it on the graph
#Reference: https://stackoverflow.com/questions/57131454/how-to-convert-a-field-of-dataframe-into-int-in-python
df['lecture'] = pd.to_numeric(df['lecture'])
##----------------------------------------------------------------------------##

##----------------------------------------------------------------------------##
##Visualizing the Parallel Co-Ordinates for Weierstrass-Prize(Best Teacher)
#Reference : https://plotly.com/python/splom/
fig = px.scatter_matrix(df,dimensions=['lecture','participants','professional expertise','motivation',
'clear presentation',"overall impression"],color='professor',symbol='professor',
color_discrete_sequence = px.colors.colorbrewer.Paired, 
title='Scatter Plot Matrix for Weierstrass-Prize(Best Teacher)')
fig.update_traces(diagonal_visible=False)
fig.write_html("ScatterPlot.html")
fig.show()
##----------------------------------------------------------------------------##

##----------------------------------------------------------------------------##
#Visualizing the Parallel Co-Ordinates for Weierstrass-Prize(Best Teacher)
#Reference : https://plotly.com/python/parallel-coordinates-plot/
professorMin = df['professor'].min()
professorMax = df['professor'].max()
lectureMin = df['lecture'].min()
lectureMax = df['lecture'].max()
participantsMin = df['participants'].min()
participantsMax = df['participants'].max()
professionalExpertiseMin = df['professional expertise'].min()
professionalExpertiseMax = df['professional expertise'].max()
motivationMin = df['motivation'].min()
motivationMax = df['motivation'].max()
clearPresentationMin = df['clear presentation'].min()
clearPresentationMax = df['clear presentation'].max()
overallImpressionMin = df['overall impression'].min()
overallImpressionMax = df['overall impression'].max()
df['professor'] = pd.to_numeric(df['professor'])

fig = go.Figure(data=
        go.Parcoords(
            line = dict(color = df['professor'],
                   colorsrc = "professor",
                   colorscale = 'Rainbow',
                   showscale = True),
                   dimensions = list([
                dict(label = "Professor", values = df['professor']),
                dict(range = [0, lectureMax],
                    label = "Lecture Number", values = df['lecture']),
                dict(range = [0,participantsMax],
                    label = "Participants", values = df['participants']),
                dict(range = [0,professionalExpertiseMax],
                    label = 'Professional Expertise', values = df['professional expertise']),
                dict(range = [0,motivationMax],
                    label = 'Motivation', values = df['motivation']),
                dict(range = [0,clearPresentationMax],
                    label = 'Clean Presentation', values = df['clear presentation']),
                dict(range = [0,overallImpressionMax],
                    label = 'Overall impression', values = df['overall impression'])])
            )
)
fig.update_layout(
        title="Parallel Co-ordinates of Weierstrass-Prize(Best Teacher)"
    )
fig.write_html("Parallel_Co-Ordinates.html")
fig.show()
