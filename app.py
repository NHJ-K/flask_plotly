from flask import Flask, render_template
import pandas as pd
import json
import plotly
import plotly.express as px

app = Flask(__name__)

@app.route('/')

def notdash():
    df1 = pd.read_json('test.json')
    #print(df1)
    fig = px.bar(df1, x='time', y='forecast',  
      barmode='group')
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('notdash.html', graphJSON=graphJSON)

