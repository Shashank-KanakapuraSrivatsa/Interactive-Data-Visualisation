import sys
import pandas as pd
import numpy as np

import plotly.express as px
import plotly.graph_objects as go
from matplotlib import pyplot as plt
from pandas.plotting._matplotlib import parallel_coordinates

inputfilename = "DataWeierstrass.csv"

def read_input_data(filename):

    inputdata = pd.read_csv(filename,sep=";")
    return (inputdata)

def encode_categorical_variables(dataDF):

    # Encode the professor categorical 
    dataDF['professor'] = dataDF['professor'].str.replace('prof', '')

    # Encode the lecture categorical variable into a int list
    dataDF['lecture'] = pd.to_numeric(dataDF['lecture'].str.replace('lecture', ''))

    return (dataDF)

def draw_plotly_scatter_plot_matrix(dataDF):

    # Reference : https://plotly.com/python/splom/ 
    # Using : Styled Scatter Matrix with Plotly Express

    figure  = px.scatter_matrix(dataDF,
                                dimensions=["lecture", "participants", "professional expertise", "motivation", "clear presentation", "overall impression" ],
                                color="professor",
                                symbol="professor",
                                title="Scatter matrix of Weierstrass-Prize") 
    figure.update_traces(diagonal_visible=False)
    figure.show()

def draw_plotly_go_parallel_coordinates_matrix(dataDF):

    # Converting the professor attribute into int datatype
    dataDF['professor'] = pd.to_numeric(dataDF['professor'])

    # Calculate the min, max and range to be used while defining the range
    dimensions=["lecture", "participants", "professional expertise", "motivation", "clear presentation", "overall impression" ]

    min_max_range = {}
    for col in dimensions:
        min_max_range[col] = [dataDF[col].min(), dataDF[col].max(), np.ptp(dataDF[col])]
 
    # Reference : https://plotly.com/python/parallel-coordinates-plot/
    # Usage : Advanced Parallel Coordinates Plot
    
    figure = go.Figure(data=
        go.Parcoords(
            line = dict(color = dataDF['professor'],
                   colorsrc = "professor",
                   colorscale = 'Rainbow',
                   showscale = False),
            dimensions = list([
                dict(range = [(dataDF['professor'].min() - 1 ), (dataDF['professor'].max() + 1)],
                    label = "Professor Number", values = dataDF['professor']),
                dict(range = [(dataDF['lecture'].min() - 1 ), (dataDF['lecture'].max() + 1)],
                    label = "Lecture Number", values = dataDF['lecture']),
                dict(range = [(dataDF['participants'].min() - 1 ), (dataDF['participants'].max() + 1)],
                    label = "Participants", values = dataDF['participants']),
                dict(range = [6,0],
                    tickvals = [ 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6 ],
                    label = 'Professional Expertise', values = dataDF['professional expertise']),
                dict(range = [6,0],
                    tickvals = [ 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6 ],
                    label = 'Motivation', values = dataDF['motivation']),
                dict(range = [6,0],
                    tickvals = [ 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6 ],
                    label = 'Clean Presentation', values = dataDF['clear presentation']),
                dict(range = [6,0],
                    tickvals = [ 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6 ],
                    label = 'Overall impression', values = dataDF['overall impression'])])
            )
        )
    
    figure.update_layout(
        title="Parallel Co-ordinates of Weierstrass-Prize"
    )
    figure.show()

def draw_parallel_coordinates(dataDF):

    # Reference : https://benalexkeen.com/parallel-coordinates-in-matplotlib/

    unique_count = dataDF['professor'].nunique()

    print(unique_count)

    colors = dict(**mcolors.CSS4_COLORS)
    colors_list = list(colors.values())

    reduced_colors_list = colors_list[0:unique_count]

    print(len(reduced_colors_list))

    columns = ['participants','professional_expertise', 'motivation','clear_presentation', 'overall_impression']

    column_index = []
    for index, value in enumerate(columns):
        column_index.append(index)

    print(column_index)

    # Get min, max and range
    min_max_range = {}
    for col in columns:
        min_max_range[col] = [dataDF[col].min(), dataDF[col].max(), np.ptp(dataDF[col])]

    
    print("min_max_range", min_max_range)
    # Normalize the data for each of the individual columns

    normalized_dataDF = dataDF
    for column in columns :
        normalized_dataDF[column] = np.true_divide(dataDF[column] - dataDF[column].min(), np.ptp(dataDF[column]))

    print(normalized_dataDF)

    parallel_coordinates(dataDF, "professor" ,cols=[ 'participants','professional_expertise', 'motivation','clear_presentation', 'overall_impression'])
    plt.show()

    # Create (column_index-1) sublots along x axis
    fig, axes = plt.subplots(1, len(column_index)-1, sharey=False, figsize=(15,5))


def main():
    print("Hello")

    inputDF = read_input_data(inputfilename)

    encodedDF = encode_categorical_variables(inputDF)
    
    ## Task 1: Visualizegiven data with ascatterplotmatrix
    draw_plotly_scatter_plot_matrix(encodedDF)

    ## Task 2 : Visualizegiven data with parallel coordinates.
    draw_plotly_go_parallel_coordinates_matrix(encodedDF)


if __name__ == "__main__":
    main()