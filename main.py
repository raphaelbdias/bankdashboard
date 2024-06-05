from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)


# Analysis (for example purposes, you can add more analyses as needed)
def get_summary_statistics():
    return df.describe()

def get_exit_analysis():
    return df.groupby('Exited').size()

@app.route('/')
def index():
    # summary_statistics = get_summary_statistics().to_html()
    # exit_analysis = get_exit_analysis().to_frame().to_html()
    return render_template('index.html', active_tab='dashboard')

@app.route('/statistics')
def statistics():
    # Replace with your statistics logic
    return render_template('statistics.html', active_tab='statistics')

@app.route('/analysis')
def analysis():
    # Replace with your analysis logic
    return render_template('analysis.html', active_tab='analysis')

if __name__ == '__main__':
    app.run(debug=True)
