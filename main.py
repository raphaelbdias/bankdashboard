from flask import Flask, render_template
import pandas as pd
import folium

app = Flask(__name__)

df = pd.read_csv('Churn_Modelling.csv')

location_coords = {
    'France': [46.603354, 1.888334],
    'Spain': [40.463667, -3.74922],
    'Germany': [51.165691, 10.451526]
}

# Add coordinates to the dataframe
df['Coordinates'] = df['Geography'].map(location_coords)

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
    # Create a map centered in Europe
    map_center = [45.603354, 9.888334]
    folium_map = folium.Map(location=map_center, zoom_start=3, tiles="cartodb positron")

    # Add markers to the map
    # for idx, row in df.iterrows():
    #     if row['Coordinates']:
    #         folium.Marker(
    #             location=row['Coordinates'],
    #             popup=row['Geography'],
    #             icon=folium.Icon(color='blue', icon='info-sign')
    #         ).add_to(folium_map)

    # Save the map to an HTML file
    map_html = folium_map._repr_html_()
    return render_template('index.html', active_tab='dashboard', map_html=map_html)

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
