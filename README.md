# Prediction Result App

## Overview

This project contains two assignments that run a simple web application using `app.py`. The first assignment displays prediction results, while the second assignment integrates with the Gemini API to get dynamic results. Both assignments require minimal setup—just run `app.py` to launch the app.

## Requirements

- Python 3.7+
- Flask (for the web application)
- Gemini API key (for the second assignment)
- Additional dependencies listed in `requirements.txt`

## Installation

### Step 1: Clone the repository

Clone this repository to your local machine:

```bash
git clone <repository_url>
cd <repository_directory>

### Step 2: Install dependencies
Create a virtual environment and install the required packages:

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install -r requirements.txt

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install -r requirements.txt
Step 3: Set up environment variables (for the second assignment)
For the first assignment: No additional setup is required.
For the second assignment: Set the Gemini API key as an environment variable. Create a .env file in the project root directory with the following content:
makefile
Copy code
GEMINI_API_KEY=your_gemini_api_key_here
Replace your_gemini_api_key_here with your actual Gemini API key.

Step 4: Run the application
Run the app.py file:

bash
Copy code
python app.py
The app will be available at http://127.0.0.1:5000/ in your web browser.

Usage
First Assignment: After running the app, visit the homepage to view the prediction results for the first assignment. The page will display the delay status and delivery difference.

Second Assignment: Once the Gemini API key is set up, the app will use the key to fetch dynamic prediction results from the Gemini API.

Folder Structure
bash
Copy code
project/
│
├── app.py              # Main application file
├── requirements.txt    # Required dependencies
├── .env                # Gemini API key (for the second assignment)
└── README.md           # Project documentation
Troubleshooting
If you encounter any issues running the app, ensure you have correctly set up the environment variables and installed all dependencies.
If the Gemini API is not working, verify that your API key is valid and correctly set in the .env file.
