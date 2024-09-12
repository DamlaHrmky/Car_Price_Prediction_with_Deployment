# Car Price Prediction

This project aims to predict car prices based on various features using linear regression models. The model is trained on historical car price data and is deployed as a web application using Flask.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Model Details](#model-details)
- [Deployment](#deployment)
- [License](#license)

## Project Overview

The Car Price Prediction project is designed to estimate the price of a car based on its features such as make, model, year, mileage, and more. The project utilizes linear regression techniques to create a predictive model and provides a user-friendly web interface for making predictions.

## Features

- **Price Prediction**: Predict car prices based on input features.
- **User Interface**: Simple web application built with Flask for easy interaction.
- **Model Training**: Linear regression models to predict car prices.

## Installation

To set up and run the project locally, follow these steps:

1. **Clone the Repository**

    ```bash
    git clone https://github.com/yourusername/car-price-prediction.git
    cd car-price-prediction
    ```

2. **Create a Virtual Environment**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Application**

    ```bash
    python app.py
    ```

5. Open your browser and navigate to `http://127.0.0.1:5000/` to use the application.

## Usage

- **Input**: Enter the details of the car such as make, model, year, mileage, etc.
- **Prediction**: Submit the form to get the predicted price of the car.

## Screenshots

Here are some screenshots of the Flask application:
*Figure 1: Home page of the car price prediction application.*
![Hom![1](https://github.com/user-attachments/assets/98499c8e-f2d4-4e5f-be4a-77fc5f25fe13)


*Figure 2: Prediction result page showing data overview.*
![Predict![2](https://github.com/user-attachments/assets/b4f513ee-29cd-4640-a0a7-b4fc1309f42b)

*Figure 3: Prediction result page showing price distributions*
![3](https://github.com/user-attachments/assets/7ef55f27-e833-4c9c-97a8-78daedfcedd7)

*Figure 3: Prediction result page showing price prediction*
![4](https://github.com/user-attachments/assets/1d04654f-1853-4e43-9704-6219e610ad9b)
![5](https://github.com/user-attachments/assets/699ccac2-8fce-4365-b2f0-29b19686638c)



## Model Details

- **Model**: Linear Regression
- **Features**: Includes various car attributes such as make, model, year, mileage, and more.
- **Training**: The model is trained on historical car price data using linear regression techniques.

## Deployment

The project is deployed using Flask. The `app.py` file contains the Flask application that serves the web interface and handles user input.

### To Deploy on Your Own Server

1. **Ensure Flask is installed**:

    ```bash
    pip install Flask
    ```

2. **Run the Flask Application**

    ```bash
    python app.py
    ```

3. **Access the Application**: Open `http://127.0.0.1:5000/` in your web browser.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


