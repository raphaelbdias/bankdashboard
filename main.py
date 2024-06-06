from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

df = pd.read_csv('Churn_Modelling.csv')

# Function to format currency and round off to 1 decimal
def format_currency(amount):
    return "{:,.1f} €".format(round(amount, 1))

# Function to convert boolean to 'Yes' or 'No'
def to_yes_no(value):
    return 'Yes' if value else 'No'

# Apply data transformations
df['Balance'] = df['Balance'].apply(format_currency)
df['EstimatedSalary'] = df['EstimatedSalary'].apply(format_currency)
df['HasCrCard'] = df['HasCrCard'].apply(to_yes_no)
df['IsActiveMember'] = df['IsActiveMember'].apply(to_yes_no)
df['Exited'] = df['Exited'].apply(to_yes_no)

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

@app.route('/data')
def data():
    customers_data = df.to_dict(orient='records')
    return render_template('data.html', active_tab='data', customers=customers_data)

if __name__ == '__main__':
    app.run(debug=True)
