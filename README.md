# Delivery Prediction Application

A Flask-based web application that provides delivery predictions through both static and dynamic approaches. The application consists of two assignments: one displaying static prediction results and another integrating with the Gemini API for dynamic predictions.

## Features

- **Assignment 1**: Static prediction display
  - Shows predefined delay status
  - Displays delivery difference
  - Simple and clean web interface

- **Assignment 2**: Dynamic predictions via Gemini API
  - Real-time prediction generation
  - API integration with Google's Gemini
  - Error handling and fallback mechanisms

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)
- Git
- Gemini API key (for Assignment 2)

## Installation

1. Clone the repository
```bash
git clone <repository_url>
cd <repository_directory>
```

2. Create and activate a virtual environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

3. Install required packages
```bash
pip install -r requirements.txt
```

4. Environment Setup
- For Assignment 1: No additional setup required
- For Assignment 2: Create a `.env` file in the project root:
```
GEMINI_API_KEY=your_gemini_api_key_here
```

## Project Structure

```
project/
│
├── app.py              # Main Flask application
├── requirements.txt    # Project dependencies
├── .env               # Environment variables (for Assignment 2)
├── README.md          # Project documentation
│
└── templates/         # HTML templates
    └── index.html     # Main prediction display page
```

## Running the Application

1. Ensure your virtual environment is activated
2. Run the Flask application:
```bash
python app.py
```
3. Access the application at `http://127.0.0.1:5000`

## API Endpoints

- `/` (GET): Displays static prediction results (Assignment 1)
- `/predict` (GET): Returns dynamic predictions using Gemini API (Assignment 2)

## Development

To modify the application:

1. Static predictions can be adjusted in the `MOCK_PREDICTION` dictionary in `app.py`
2. Gemini API integration can be customized in the `GeminiPredictor` class
3. Frontend appearance can be modified in `templates/index.html`

## Troubleshooting

Common issues and solutions:

1. **Missing Dependencies**
   - Error: `ModuleNotFoundError`
   - Solution: Run `pip install -r requirements.txt`

2. **Environment Variables**
   - Error: "Gemini API key not configured"
   - Solution: Ensure `.env` file exists with valid API key

3. **API Errors**
   - Error: Failed to get prediction
   - Solution: Verify API key validity and network connection

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support and questions:
- Open an issue in the repository
- Contact the development team

## Acknowledgments

- Flask framework
- Google Gemini API
- Contributors and maintainers
