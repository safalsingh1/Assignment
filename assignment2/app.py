from flask import Flask, render_template, request, jsonify
import os
import google.generativeai as genai

# Initialize Flask app
app = Flask(__name__)

# Set up upload folder
UPLOAD_FOLDER = 'static/uploads/'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Authenticate with Google Generative AI (Replace with your API key)
genai.configure(api_key="GEMINI_API")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if file:
        # Save the uploaded image
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        try:
            # Upload the image to Google Generative AI
            uploaded_file = genai.upload_file(filepath)

            # Generate content using Gemini
            model = genai.GenerativeModel("gemini-1.5-flash")
            result = model.generate_content(
                [
                    uploaded_file, "\n\n", "Can you tell me about this photo?"
                ]
            )

            # Return the result as a response
            return jsonify({"description": result.text})

        except Exception as e:
            return jsonify({"error": str(e)}), 500

    return jsonify({"error": "Something went wrong"}), 500

if __name__ == '__main__':
    app.run(debug=True)
