# Weather App

## Description

This Django Weather App provides weather information for a given city and a 5-day weather forecast. It fetches data from the OpenWeatherMap API and displays it to the user. The app also includes a search feature for city names, using the API-Ninjas API.

## Requirements

- Python 3.7 or higher
- Django 4.2 or higher
- Requests library
- API keys for OpenWeatherMap and API-Ninjas

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/Weather-App.git
cd Weather-App
```

### 2. Create a Virtual Environment

```bash
python -m venv djangoenv
```

### 3. Activate the Virtual Environment

- **On Windows:**

  ```bash
  djangoenv\Scripts\activate
  ```

- **On macOS/Linux:**

  ```bash
  source djangoenv/bin/activate
  ```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Set Up Environment Variables

Create a `.env` file in the root directory and add your API keys:

```
OPENWEATHERMAP_API_KEY=your_openweathermap_api_key
API_NINJAS_API_KEY=your_api_ninjas_api_key
```

Alternatively, you can directly insert these API keys into your `views.py` file, but using environment variables is recommended for security.

### 6. Run Migrations

```bash
python manage.py migrate
```

### 7. Start the Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your web browser to view the app.

## Project Structure

- **`weather_app/`**: Contains Django app files.
  - **`templates/weather_app/index.html`**: HTML template for the weather app.
  - **`views.py`**: Contains view functions to handle requests and interact with APIs.
- **`static/`**: Contains static files such as CSS and images.
- **`manage.py`**: Django’s command-line utility for administrative tasks.
- **`requirements.txt`**: List of Python packages required to run the project.

## API Details

### OpenWeatherMap API

- **Current Weather**: `https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}`
- **5-Day Forecast**: `https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}`

### API-Ninjas

- **City Search**: `https://api.api-ninjas.com/v1/city?name={query}`

## Features

- Search for cities and view current weather information.
- View a 5-day weather forecast.
- Modal with additional information about the Product Manager Accelerator Program.

## Troubleshooting

- Ensure all environment variables are correctly set.
- Check API keys and ensure they are valid and have not expired.
- Verify that all dependencies are installed properly.
  
