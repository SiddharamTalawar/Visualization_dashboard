from django.shortcuts import render
import json
from .models import Content
from plotly.offline import plot
import plotly.express as px
import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go


def dataView(request):
    """This view helps us to store data in models from json file."""
    # creating a file object.
    json_data = open('jsondata (3).json', 'r', encoding='utf8')
    my_data = json_data
    # parsing/converting json data to python data.
    python_data = json.load(my_data)

    for data in python_data:
        dictonary = data
        # converting the dictonary instance to model instance, i.e saving the data to model.
        m = Content(**dictonary)
        m.save()
    pydata = {'python_data': 'python_data is added to database'}
    return render(request, 'index.html', pydata)


def barplotView(request):
    """By using data present in database this view helps us to plot various graphs."""
    qs = Content.objects.all()
    # orgnising data so it can converted into pandas dataframe using listcompressions.
    data = [
        {
            "title": item.title,
            "intensity": item.intensity,
            "sector": item.sector,
            "topic": item.topic,
            "end_year": item.end_year,
            "start_year": item.start_year,
            "country": item.country,
            "pestle": item.pestle,
            "likelihood": item.likelihood,
            "region": item.region,
            "relevance": item.relevance,
            "source": item.source,

        } for item in qs
    ]
    df = pd.DataFrame(data)
    # plots and graphs.
    fig = px.bar(df,  x="country", color="country",
                 title='Ammount of data we have on each country')
    bar_plot = plot(fig, output_type="div")

    fig = px.scatter(
        df, x='start_year', y='end_year',  color='intensity',
        hover_data=['title', 'sector', 'topic', 'region', 'country', 'pestle'],
        title='Data on topics with there different levels of impacts(intensity)'
    )
    scatter_plot = plot(fig, output_type="div")

  # creating bar charts  using year as constraints
    fig = px.bar(
        df, x="start_year", y="end_year", color='pestle', hover_data=["title", "sector", "topic"],
        barmode="group", title='Data on external factors that influence an organisation -- PESTLE  '

    )
    bar_plot2 = plot(fig, output_type="div")


# creating filters for navbar dropdown box.
    country_data_list = []
    for item in data:
        country_data = item.get('country')
        country_data_list.append(country_data)
# making sure that the lists have only unique values.
        country_data_set = set(country_data_list)
        unique_country_data_list = list(country_data_set)
# sorting the list alphbetically, for ease of access in navbar(A-Z).
    unique_country_data_list.sort()

    context = {'bar_plot': bar_plot, 'scatter_plot': scatter_plot,
               'bar_plot2': bar_plot2, 'unique_country_data_list': unique_country_data_list}
    return render(request, 'index.html', context)


def countryView(request, country):
    """By using data present in database this view helps us to plot various graphs."""
    # orgnising data so it can converted into pandas dataframe using listcompressions.
    qs = Content.objects.filter(country=country)
    data = [
        {
            "title": item.title,
            "intensity": item.intensity,
            "sector": item.sector,
            "topic": item.topic,
            "end_year": item.end_year,
            "start_year": item.start_year,
            "country": item.country,
            "pestle": item.pestle,
            "likelihood": item.likelihood,
            "region": item.region,
            "relevance": item.relevance,
            "source": item.source,

        } for item in qs
    ]
    df = pd.DataFrame(data)

    # creating sactter plot for given country
    fig = px.scatter(
        df, x='start_year', y='end_year', color='intensity',
        hover_data=['title', 'sector', 'topic', 'region', 'country', 'pestle'],
        title='Data on topics with there different levels of impacts(intensity) on ' +
        country+'.'


    )
    country_scatter_plot = plot(fig, output_type="div")

    # creating bar charts  using year as constraints
    fig = px.bar(
        df, x="start_year", y="end_year", color='pestle', hover_data=["title", "sector", "topic"],
        barmode="group", title='Data on external factors that influence an organisations of ' + country+' -- PESTLE  '

    )
    bar_plot2 = plot(fig, output_type="div")

    context = {'country_scatter_plot': country_scatter_plot,
               'bar_plot2': bar_plot2}
    return render(request, 'graph.html', context)



