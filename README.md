# InboxGenius

For Ignition Hackathon

**InboxGenius** is an AI-powered mail client designed to revolutionize how you manage your email. By integrating advanced AI capabilities with the power of the Gemini API, Flask, and MongoDB, InboxGenius offers smart, efficient, and personalized email management solutions.

## Features

- **AI-Powered Email Management**: Leverages AI to categorize, prioritize, and summarize emails, helping you stay organized and focused.
- **Smart Search**: Uses a MongoDB vector database to enhance search capabilities, allowing for context-aware searches that deliver more accurate results.
- **Personalized Inbox**: Adapts to your email habits, providing personalized suggestions and automations to streamline your inbox management.
- **Seamless Integration**: Built on Flask, making it lightweight, scalable, and easy to integrate with other web services.

## Technology Stack

- **Gemini API**: Utilized for AI capabilities, including email classification, sentiment analysis, and natural language processing.
- **Flask**: Serves as the web framework for the application, enabling a simple yet powerful backend.
- **MongoDB**: A NoSQL database that stores and manages email data, enhanced with vector embeddings to power advanced search features.

## Requirements
Python 3.11 or higher is required to run the application. 
https://www.python.org/

Gemini API Key (Sign up at https://ai.google.dev/gemini-api)

### Or you can use the following API, which is used for demonstration purposes for ignition hackathon: (Please do not use this API key for production purposes, this may be revoked at any time) This API key may expire since many people are using it.

`Genimi API Key: AIzaSyCrhFUQc9gf_QottXG9A_goXzV07HRZWT8`


## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/JunzhL/InboxGenius.git
    ```

2. **Navigate to the project directory**:

    ```bash
    cd InboxGenius
    ```

3. **Create and activate a virtual environment**:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

4. **Install the required dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

## Configuration (Must do before running the application)

1. **Set up MongoDB**: Ensure that you have a running instance of MongoDB. You can either set it up locally or use a cloud-based solution like MongoDB Atlas.

2. **Configure Environment Variables**: Create config `.env` file in the root directory and add the following variables:

    ```bash
    MONGO_URI = "mongodb+srv://Admin:rmkZXtzCUtJdHg2V@cluster0.xt7zv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    DATABASE = "Ignitionhackathon"
    TABLE = "emails"
    GOOGLE_API_KEY=YOUR_GEMINI_API_KEY # or use the provided API key
    FLASK_RUN_PORT=PORT_NUMBER
    FLASK_RUN_HOST="127.0.0.1"
    ```
    (You can use the following configuration for ignition hackathon demonstration purposes)
    ```bash
    # Example .env file
    MONGO_URI = "mongodb+srv://Admin:rmkZXtzCUtJdHg2V@cluster0.xt7zv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    DATABASE = "Ignitionhackathon"
    TABLE = "emails"
    GOOGLE_API_KEY= "AIzaSyCrhFUQc9gf_QottXG9A_goXzV07HRZWT8"
    FLASK_RUN_PORT= 8000
    FLASK_RUN_HOST="127.0.0.1"
    ```

## Running the Application

1. **Run the Flask development server**:

    ```bash
    flask run
    ```

2. **Access InboxGenius**: Open your browser and navigate to `http://127.0.0.1:8000/`. (Or the port number you specified in the `.env` file)

3. **Login**: Use the following credentials to log in:

    - **Email**: `demo@hack.com`
    - **Password**: `ignition`

## Usage

- **Inbox Management**: View and manage your emails through the web interface. Use the smart search feature to find emails based on context, not just keywords. More precise input leads to better results.
- **AI Suggestions**: Enable or customize AI suggestions for better email prioritization and automation.
- **AI Classification**: Use the AI-powered email classification feature to categorize emails based on content and context.
- **Custom Automation**: Set up rules and automation to further streamline your inbox based on your workflow.

## Contributing

We welcome contributions! Please feel free to submit a pull request or open an issue to discuss potential improvements or features.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or support, please open an issue.
