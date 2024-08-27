import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pickle

# Load the dataset
df = pd.read_csv('df_new.csv')

# Load the model pipeline
with open('model_pipeline.pkl', 'rb') as f:
    model_pipeline = pickle.load(f)

# Define the Streamlit app
st.title('Car Model Analysis')

# Define custom CSS and inject it into the Streamlit app
def set_custom_css():
    st.markdown("""
        <style>
        /* Global Styling */
        .stApp {
            background: url(../images/bg.jpg);
            background-size: cover;
        }

        /* Title Styling */
        .title {
            font-family: 'Arial', sans-serif;
            font-size: 36px;
            color: #333;
        }

        /* Header Styling */
        .header {
            font-family: 'Arial', sans-serif;
            font-size: 28px;
            color: #333;
        }

        /* Subheader Styling */
        .subheader {
            font-family: 'Arial', sans-serif;
            font-size: 24px;
            color: #555;
        }

        /* Button Styling */
        .stButton>button {
            font-family: 'Arial', sans-serif;
            font-size: 18px;
            color: #ffffff;
            background-color: #007bff;
        }

        /* Background color for pages */
        .statistics-page { 
            background-color: #e0f7fa; 
        }
        .plots-page { 
            background-color: #e8f5e9; 
        }
        .prediction-page { 
            background-color: #fff3e0; 
        }
        </style>
        """, unsafe_allow_html=True)

# Apply custom CSS
set_custom_css()

# Static navigation bar using radio buttons
st.sidebar.title('Navigation')
page = st.sidebar.radio('Select a Page', ['Statistics', 'Plots', 'Prediction'])

# Page 1: Display Statistics
if page == 'Statistics':
    st.markdown('<div class="statistics-page">', unsafe_allow_html=True)
    st.markdown('<h1 class="header">Data Statistics</h1>', unsafe_allow_html=True)
    
    st.markdown('<h2 class="subheader">Data Head</h2>', unsafe_allow_html=True)
    st.write(df.head())
    
    st.markdown('<h2 class="subheader">Data Description</h2>', unsafe_allow_html=True)
    st.write(df.describe())

        # New section: Value Counts of Categorical Features
    st.markdown('<h2 class="subheader">Value Counts of Categorical Features</h2>', unsafe_allow_html=True)
    categorical_columns = df.select_dtypes(include=['object']).columns  # Select categorical columns
    for col in categorical_columns:
        st.markdown(f'**{col}**')
        st.write(df[col].value_counts())
    
    
    st.markdown('</div>', unsafe_allow_html=True)

# Page 2: Show Plots
elif page == 'Plots':
    st.markdown('<div class="plots-page">', unsafe_allow_html=True)
    st.markdown('<h1 class="header">Data Visualization</h1>', unsafe_allow_html=True)

    # Scatter plot for selected feature vs. price
    numeric_columns = df.select_dtypes(include=['number']).columns
    feature_options = numeric_columns.difference(['price'])
    
    feature = st.selectbox('Select Numeric Feature to Plot Against Price', feature_options)
    st.markdown(f'<h2 class="subheader">Price vs {feature}</h2>', unsafe_allow_html=True)
    fig, ax = plt.subplots()
    sns.scatterplot(data=df, x=feature, y='price', ax=ax)
    st.pyplot(fig)

    # Histogram for selected feature
    histogram_feature = st.selectbox('Select Feature for Histogram', numeric_columns)
    st.markdown(f'<h2 class="subheader">Distribution of {histogram_feature}</h2>', unsafe_allow_html=True)
    fig, ax = plt.subplots()
    sns.histplot(df[histogram_feature], bins=10, kde=True, ax=ax)
    st.pyplot(fig)

    # Dropdown for selecting make/model to visualize
    make_model_options = df['make_model'].value_counts().nlargest(20).index.tolist()
    selected_make_model = st.selectbox('Select Make Model for Streamplot', make_model_options)

    # Filter data based on selected make/model
    filtered_df = df[df['make_model'] == selected_make_model]

    # Dropdown for selecting features to plot against each other
    x_feature = st.selectbox('Select Feature for X-axis', numeric_columns)
    y_feature = st.selectbox('Select Feature for Y-axis', numeric_columns)

    # Streamplot for selected features
    st.markdown(f'<h2 class="subheader">Streamplot of {x_feature} vs {y_feature} for {selected_make_model}</h2>', unsafe_allow_html=True)
    fig, ax = plt.subplots()
    sns.kdeplot(data=filtered_df, x=x_feature, y=y_feature, cmap='Blues', fill=True, ax=ax)
    st.pyplot(fig)

    # Box Plot and Strip Plot for selected make/model
    st.markdown('<h1 class="header">Box Plot and Strip Plot for Selected Make/Model</h1>', unsafe_allow_html=True)
    selected_make_model = st.selectbox('Select Make/Model', ['All'] + df['make_model'].unique().tolist())

    if selected_make_model != 'All':
        filtered_df = df[df['make_model'] == selected_make_model]
        if not filtered_df.empty:
            fig, ax = plt.subplots(figsize=(10, 6))
            sns.boxplot(x='make_model', y='price', data=filtered_df, ax=ax, color='blue')
            sns.stripplot(x='make_model', y='price', data=filtered_df, ax=ax, color='black', jitter=True, alpha=0.6)
            ax.set_title(f'Price Distribution for {selected_make_model}')
            ax.set_xlabel('Make/Model')
            ax.set_ylabel('Price')
            st.pyplot(fig)
        else:
            st.write("No data available for the selected make/model.")
    else:
        st.write("Select a specific make/model to see the plot.")

    st.markdown('</div>', unsafe_allow_html=True)

# Page 3: Make Predictions
elif page == 'Prediction':
    st.markdown('<div class="prediction-page">', unsafe_allow_html=True)
    st.markdown('<h1 class="header">Make a Prediction</h1>', unsafe_allow_html=True)

    make_model = st.selectbox('Make Model', df['make_model'].unique())
    type_ = st.selectbox('Type', df['type'].unique())
    power_kW = st.number_input('Power kW', min_value=0, max_value=1000, value=100)
    engine_size = st.number_input('Engine Size', min_value=0, max_value=10000, value=2000)
    age = st.number_input('Age', min_value=0, max_value=50, value=5)
    mileage = st.number_input('Mileage', min_value=0, max_value=200000, value=50000)

    if st.button('Predict'):
        input_data = {
            'make_model': make_model,
            'type': type_,
            'power_kW': power_kW,
            'engine_size': engine_size,
            'age': age,
            'mileage': mileage
        }
        input_df = pd.DataFrame([input_data])
        prediction = model_pipeline.predict(input_df)
        st.write(f'Prediction: {prediction[0]}')

    st.markdown('</div>', unsafe_allow_html=True)
