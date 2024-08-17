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

## Configuration

1. **Set up MongoDB**: Ensure that you have a running instance of MongoDB. You can either set it up locally or use a cloud-based solution like MongoDB Atlas.

2. **Configure Environment Variables**: Create config `.env` file in the root directory and add the following variables:

    ```bash
    MONGO_URI=Set_Later
    GOOGLE_API_KEY=your_gemini_api_key
    FLASK_APP=inboxgenius
    FLASK_ENV=development
    ```

## Running the Application

1. **Run the Flask development server**:

    ```bash
    flask run
    ```

2. **Access InboxGenius**: Open your browser and navigate to `http://127.0.0.1:5000/`.

## Usage

- **Inbox Management**: View and manage your emails through the web interface. Use the smart search feature to find emails based on context, not just keywords.
- **AI Suggestions**: Enable or customize AI suggestions for better email prioritization and automation.
- **Custom Automation**: Set up rules and automation to further streamline your inbox based on your workflow.

## Contributing

We welcome contributions! Please feel free to submit a pull request or open an issue to discuss potential improvements or features.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or support, please open an issue.
