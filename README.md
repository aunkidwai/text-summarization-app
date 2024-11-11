# Text Summarization App

📝 **Text Summarization App** is a Streamlit application that allows users to summarize text from various sources, including direct text input, PDF files, and URLs. The app provides customizable options for word limits, temperature, summary style, and keyword focus, making it a versatile tool for anyone needing quick summaries.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Contributing](#contributing)
- [License](#license)

## Features
- **Multiple Input Types**: Accepts text input, PDF uploads, and URLs for summarization.
- **Customizable Options**: Users can set minimum and maximum word limits, temperature, summary style (extractive or abstractive), and focus on specific keywords.
- **Interactive Interface**: A user-friendly interface with a sidebar for settings, sample inputs for demonstration, and loading indicators.
- **Responsive Design**: The app is designed to be responsive and works well on various screen sizes.

## Technologies Used
- [Streamlit](https://streamlit.io/) - A framework for building web applications in Python.
- [Langchain](https://langchain.readthedocs.io/en/latest/) - A framework for developing applications powered by language models.
- [PyPDF2](https://pypdf2.readthedocs.io/en/latest/) - A library for reading PDF files.
- [Requests](https://docs.python-requests.org/en/latest/) - A library for making HTTP requests.
- [Ollama](https://ollama.com/) - A tool for running language models locally.

## Installation
To run the Text Summarization App locally, follow these steps:

1. **Install Ollama**:
   - Follow the installation instructions on the [Ollama website](https://ollama.com/docs/installation) to install Ollama on your system.

2. **Install the Llama model**:
   - After installing Ollama, run the following command to download the `llama3.1:8b` model:
     ```bash
     ollama pull llama3.1:8b
     ```

3. **Clone the repository**:
   ```bash
   git clone https://github.com/aunkidwai/text-summarization-app.git
   cd text-summarization-app
   ```

4. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

5. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

6. **Run the Streamlit app**:
   ```bash
   streamlit run main.py
   ```

## Usage
1. **Select Input Type**: Choose between Text, PDF, or URL.
2. **Enter Input**: Depending on the selected input type, provide the necessary input (text, upload a PDF, or enter a URL).
3. **Set Options**: Specify the minimum and maximum word limits, temperature, summary style, and any keywords to focus on.
4. **Generate Summary**: Click the "Generate Summary" button to receive the summarized text.

## How It Works
- The app uses the Langchain library to interact with a language model (OllamaLLM) for generating summaries.
- Users can input text directly, upload PDF files, or provide URLs. The app extracts text from PDFs and fetches content from URLs.
- The summarization process is customizable, allowing users to specify various parameters to tailor the output to their needs.

## Contributing
Contributions are welcome! If you have suggestions for improvements or new features, please fork the repository and submit a pull request.

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Made with ❤️ by [Your Name]
