import os
import os
import base64
import pandas as pd
import seaborn as sns
import requests 
import pickle
import matplotlib
matplotlib.use('Agg')  # Use the 'Agg' backend for non-GUI (file-based) plotting
import matplotlib.pyplot as plt
from flask import Flask, render_template, request, jsonify, send_from_directory, url_for
app = Flask(__name__)
# Load the DataFrame
df = pd.read_csv("df_new.csv")
@app.route('/')
def home():
    columns = df.columns.tolist()
    return render_template('index.html', fields=columns)

@app.route('/index.html')
def homepage():
    return render_template('index.html')

@app.route('/overview.html', methods=['GET', 'POST'])
def overview():
    # Ensure correct data types
    df['power_kW'] = pd.to_numeric(df['power_kW'], errors='coerce')
    df['mileage'] = pd.to_numeric(df['mileage'], errors='coerce')
    df['age'] = pd.to_numeric(df['age'], errors='coerce')

    # Default filter values
    selected_make_model = 'All'
    selected_type = 'All'
    power_kw_min = 0
    power_kw_max = float('inf')
    mileage_min = 0
    mileage_max = float('inf')
    age_min = 0
    age_max = float('inf')

    if request.method == 'POST':
        selected_make_model = request.form.get('make_model', 'All')
        selected_type = request.form.get('type', 'All')

        # Helper function to parse form input
        def parse_float(input_str, default):
            try:
                return float(input_str.strip()) if input_str else default
            except ValueError:
                return default

        # Retrieve form data and convert to float
        power_kw_min = parse_float(request.form.get('power_kw_min'), 0)
        power_kw_max = parse_float(request.form.get('power_kw_max'), float('inf'))
        mileage_min = parse_float(request.form.get('mileage_min'), 0)
        mileage_max = parse_float(request.form.get('mileage_max'), float('inf'))
        age_min = parse_float(request.form.get('age_min'), 0)
        age_max = parse_float(request.form.get('age_max'), float('inf'))

    # Filter the DataFrame based on the selected features
    filtered_df = df
    if selected_make_model != 'All':
        filtered_df = filtered_df[filtered_df['make_model'] == selected_make_model]
    if selected_type != 'All':
        filtered_df = filtered_df[filtered_df['type'] == selected_type]

    # Apply power kW filter
    filtered_df = filtered_df[(filtered_df['power_kW'] >= power_kw_min) & (filtered_df['power_kW'] <= power_kw_max)]
    # Apply mileage filter
    filtered_df = filtered_df[(filtered_df['mileage'] >= mileage_min) & (filtered_df['mileage'] <= mileage_max)]
    # Apply age filter
    filtered_df = filtered_df[(filtered_df['age'] >= age_min) & (filtered_df['age'] <= age_max)]

    # Calculate statistics
    stats = filtered_df.groupby('make_model').agg(
        count=('price', 'size'),
        min_price=('price', 'min'),
        max_price=('price', 'max'),
        avg_price=('price', 'mean')
    ).reset_index()

    stats.columns = ['Make/Model', 'Value Count', 'Minimum Price', 'Maximum Price', 'Average Price']

    # Convert to HTML table
    stats_table = stats.to_html(classes='table table-striped', index=False)

    return render_template('overview.html', 
                           make_models=df['make_model'].unique(),
                           car_types=df['type'].unique(),
                           df_head=filtered_df.head().to_html(classes='table table-striped'),
                           df_describe=filtered_df.describe().to_html(classes='table table-striped'),
                           stats_table=stats_table,
                           selected_make_model=selected_make_model,
                           selected_type=selected_type,
                           power_kw_min=power_kw_min,
                           power_kw_max=power_kw_max,
                           mileage_min=mileage_min,
                           mileage_max=mileage_max,
                           age_min=age_min,
                           age_max=age_max
                          )

@app.route('/visualization.html', methods=['GET', 'POST'])
def visualization():
    make_models = df['make_model'].unique()
    selected_make_model = request.args.get('make_model', default=make_models[0], type=str)
    field = request.args.get('field', default='power_kW', type=str)

    # Ensure the field is valid
    if field not in df.columns:
        field = 'type'  # Fallback to a default field if invalid

    # Initialize plot URLs
    plot_box_url = url_for('static', filename='images/placeholder.png')
    plot_url = url_for('static', filename='images/placeholder.png')

    fig, ax = plt.subplots()
    # Create the boxplot with blue color
    sns.boxplot(y=df['price'], ax=ax, color='blue')
    # Overlay the data points
    #sns.stripplot(y=df['price'], ax=ax, color='black', jitter=True, alpha=0.6)
    # Set plot titles and labels
    ax.set_title('Price Distribution')
    ax.set_xlabel('')  # No x-label needed for single column boxplot
    ax.set_ylabel('Price')
    # Save the plot to the 'static' directory
    box_plot_path = 'static/plot1.png'
    plt.savefig(box_plot_path)
    plt.close()

    # Generate plot for the selected make/model
    print("secilen modelllll",selected_make_model)
    if selected_make_model != 'All':
        filtered_df = df[df['make_model'] == selected_make_model]
        if not filtered_df.empty:
            fig, ax = plt.subplots()
             # Create the boxplot
            sns.boxplot(x='make_model', y='price', data=filtered_df, ax=ax, color='blue')

            # Overlay the data points
            sns.stripplot(x='make_model', y='price', data=filtered_df, ax=ax, color='black', jitter=True, alpha=0.6)

            # Set plot titles and labels
            ax.set_title(" ")
            ax.set_xlabel('Make/Model')
            ax.set_ylabel('Price')

            plot_filename = f'{selected_make_model}_boxplot.png'
            plot_path = os.path.join('static', 'images', plot_filename)
            plt.savefig(plot_path)
            plt.close()
            plot_box_url = url_for('static', filename=f'images/{plot_filename}')
            print("plot_box urllll",plot_box_url)

    # Generate plot for the selected field
    if field in df.columns:
        fig, ax = plt.subplots()

        if df[field].dtype == 'object' or df[field].dtype.name == 'category':
            df[field].value_counts().plot(kind='bar', ax=ax)
            ax.set_title(f'Count Plot for {field}')
            ax.set_xlabel(field)
            ax.set_ylabel('Count')
            ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
        else:
            df.plot.scatter(x=field, y='price', ax=ax)
            ax.set_title(f'Price Distribution for {field}')
            ax.set_xlabel(field)
            ax.set_ylabel('Price')

        plot_filename = f'{field}_plot.png'
        plot_path = os.path.join('static', 'images', plot_filename)
        plt.savefig(plot_path)
        plt.close()
        plot_url = url_for('static', filename=f'images/{plot_filename}')
        print("plot urllll",plot_url)
    # Get the list of make/model for dropdown
    make_models = df['make_model'].unique()
 

    return render_template('visualization.html', box_plot_path = 'static/plot1.png', selected_make_model= selected_make_model, plot=plot_url, plot_box=plot_box_url, selected_field=field, fields=df.columns, make_models=make_models)
@app.route('/prediction.html', methods=['GET', 'POST'])
def prediction():
    # Fetch make models and car types for the dropdowns
    make_models = df['make_model'].unique()
    car_types = df['type'].unique()

    # Initialize variables
    selected_make_model = None
    selected_type = None
    power_kw = 0
    mileage = 0
    age = 0
    engine_size = 0
    prediction = None

    if request.method == 'POST':
        # Retrieve form data
        selected_make_model = request.form.get('make_model')
        selected_type = request.form.get('type')
        power_kw = request.form.get('power_kw')
        mileage = request.form.get('mileage')
        age = request.form.get('age')
        engine_size = request.form.get('engine_size')

        # Convert form inputs to appropriate types
        try:
            power_kw = float(power_kw) if power_kw.strip() else 0.0
            mileage = float(mileage) if mileage.strip() else 0.0
            age = int(age) if age.strip() else 0
            engine_size = float(engine_size) if engine_size.strip() else 0.0
        except ValueError as e:
            return render_template('prediction.html',
                                   make_models=make_models,
                                   car_types=car_types,
                                   selected_make_model=selected_make_model,
                                   selected_type=selected_type,
                                   power_kw=power_kw,
                                   mileage=mileage,
                                   age=age,
                                   engine_size=engine_size,
                                   error=f'Error in processing input data: {e}'
                                  )

        # Prepare features for prediction with the correct column names
        features = pd.DataFrame([{
            'make_model': selected_make_model,
            'type': selected_type,
            'power_kW': power_kw,  # Updated column name
            'mileage': mileage,
            'age': age,
            'engine_size': engine_size
        }])

        # Make the prediction
        try:
            prediction = model.predict(features)[0]
            
        except Exception as e:
            return render_template('prediction.html',
                                   make_models=make_models,
                                   car_types=car_types,
                                   selected_make_model=selected_make_model,
                                   selected_type=selected_type,
                                   power_kw=power_kw,
                                   mileage=mileage,
                                   age=age,
                                   engine_size=engine_size,
                                   prediction=f'Prediction error: {e}'
                                  )

    return render_template('prediction.html',
                           make_models=make_models,
                           car_types=car_types,
                           selected_make_model=selected_make_model,
                           selected_type=selected_type,
                           power_kw=power_kw,
                           mileage=mileage,
                           age=age,
                           engine_size=engine_size,
                           prediction=prediction
                          )
with open('model_pipeline.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()  # Get data from the POST request
    input_features = data['features']

    # Make predictions
    predictions = model.predict([input_features])
    
    return jsonify(predictions.tolist())  # Return predictions as JSON

@app.route('/plot')
def plot():
    generate_plot()  # Function to generate the plot
    return send_from_directory('static', 'plot.png')
def generate_plot():
    # Count the occurrences of each model
     # Count the occurrences of each model
    model_counts = df['make_model'].value_counts()

    # Select the top 10 most frequent models
    top_10_models = model_counts.head(15)

    # Identify the most frequent model within the top 10
    most_frequent_model = top_10_models.idxmax()  # Most frequent model name
    most_frequent_count = top_10_models.max()     # Count of the most frequent model

    # Plotting
    #plt.figure(figsize=(7, 5))
    ax = sns.barplot(x=top_10_models.index, y=top_10_models.values, palette="viridis")

    # Highlight the most frequent model within the top 10
    plt.bar(most_frequent_model, most_frequent_count, color='red')

    plt.title('Top 15 Model Count Plot')
    
    # Add labels to the bars
    for i, value in enumerate(top_10_models.values):
        ax.text(i, value + 0.05, f'{value}', ha='center', va='bottom')
    # Add model names to the bars
    for i, (model_name, value) in enumerate(top_10_models.items()):
        ax.text(i, value / 2, f'{model_name}', ha='center', va='center', rotation=90,color='white')

    # Highlight the most frequent model within the top 10
    plt.bar(most_frequent_model, most_frequent_count, color='red')
    plt.ylabel('Count')
    plt.xlabel('')
    #plt.xticks(rotation=45)
     # Remove x-axis labels (tick labels under the bars)
    ax.set_xticks([])

    

    # Save the plot to the 'static' directory
    plot_path = 'static/plot.png'
    plt.savefig(plot_path)
    plt.close()



    

@app.route('/api/labels')
def labels():
    # Assuming 'type' is a column in your DataFrame
    df = pd.read_csv("df_new.csv")
    return jsonify(df['type'].unique().tolist())

@app.route('/api/data', methods=['GET'])
def data():
    df = pd.read_csv("df_new.csv")
    selector = request.args.getlist('selector')
    filtered_df = df[df['type'].isin(selector)]
    return jsonify(filtered_df.to_dict(orient='records'))

if __name__ == "__main__":
    app.run(host='0.0.0.0')  # Ensure it runs on port 5000
