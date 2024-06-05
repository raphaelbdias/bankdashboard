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
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
