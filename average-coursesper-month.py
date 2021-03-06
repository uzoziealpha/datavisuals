#PLOT GRAPH 

import justpy as jp
import pandas
from datetime import datetime
from pytz import utc 

#to do plotting we need to add the library
import matplotlib.pyplot as plt

data = pandas.read_csv("reviews.csv", parse_dates=['Timestamp'])

data['Month'] = data['Timestamp'].dt.strftime('%Y-%m')
month_average_crs = data.groupby(['Month', 'Course Name']).count().unstack()
#print(month_average_crs)




#we want to use .read from pandas libr to show the data in a great format
data = pandas.read_csv("reviews.csv", parse_dates=['Timestamp'])



chart_def= """
{
    chart: {
        type: 'areaspline'
    },
    title: {
        text: 'Average course per month'
    },
    legend: {
        layout: 'vertical',
        align: 'left',
        verticalAlign: 'top',
        x: 150,
        y: 100,
        floating: false,
        borderWidth: 1,
        backgroundColor:
        '#FFFFFF'
    },
    xAxis: {
        categories: [
            'Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday',
            'Saturday',
            'Sunday'
        ],
        plotBands: [{ // visualize the weekend
            from: 4.5,
            to: 6.5,
            color: 'rgba(68, 170, 213, .2)'
        }]
    },
    yAxis: {
        title: {
            text: 'Fruit units'
        }
    },
    tooltip: {
        shared: true,
        valueSuffix: ' units'
    },
    credits: {
        enabled: false
    },
    plotOptions: {
        areaspline: {
            fillOpacity: 0.5
        }
    },
    series: [{
        name: 'John',
        data: [3, 4, 3, 5, 4, 10, 12]
    }, {
        name: 'Jane',
        data: [1, 3, 4, 3, 3, 5, 4]
    }]
}
"""

def app():
    wp = jp.QuasarPage()
    #creating object for each components 
    h1 = jp.QDiv(a=wp, text="Analysis of Course Reviews", classes="text-h3 text-center q-pa-md")
    p1 = jp.QDiv(a=wp, text="These graphs course review analysis")
    
    
    
    hc = jp.HighCharts(a=wp, options=chart_def)
   #categories here will be a new list
    hc.options.xAxis.categories = list(month_average_crs.index)
    
    #we need to create a list thats made of dictionaries {}
    #high order data variable 
    hc_data = [{"name":v1, "data":[v2 for v2 in month_average_crs[v1]]} for v1 in month_average_crs.columns]
    
    #assign it to series to take over the chart list to csv output 
    hc.options.series = hc_data
    return wp

jp.justpy(app)