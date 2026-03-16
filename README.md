# Interactive Periodic Table with AI Q&A

An interactive **Periodic Table desktop application** built with Python and PyQt6.
Users can click on any element and ask questions about it, which are answered using an AI model.

## Features

* Interactive **periodic table GUI**
* Color-coded element categories
* Click any element to ask questions
* AI-generated answers about chemical elements
* Clean and simple desktop interface

## Technologies Used

* Python
* PyQt6
* python-dotenv
* OpenAI API (or compatible API endpoint)
* AI model: `mistralai/Mistral-Small-3.2-24B-Instruct-2506`

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/periodic-table-ai.git
cd periodic-table-ai
```

### 2. Install dependencies

```bash
pip install PyQt6 python-dotenv openai
```

### 3. Create a `.env` file

Create a file called `.env` in the project folder and add:

```
API_KEY=your_api_key_here
BASE_URL=your_api_base_url_here
```

## Running the Application

Run the Python file:

```bash
python periodic_table_main.py
```

A window will open showing the periodic table.

## How to Use

1. Launch the application.
2. Click on any element in the periodic table.
3. A question box will appear.
4. Type a question about the element.
5. Click **Submit** to receive an AI-generated answer.

Example questions:

* "What is this element commonly used for?"
* "Where is this element found?"
* "Is this element toxic?"
* "What are the main properties of this element?"

## Interface Overview

* **Element Grid** – Displays the periodic table.
* **Question Box** – Enter a question about the selected element.
* **Submit Button** – Sends the question to the AI model.
* **Answer Box** – Displays the response.

## Project Structure

```
periodic-table-ai
│
├── main.py
├── .env
└── README.md
```

## Notes

* The application requires a valid API key.
* Responses are limited to **500 characters** to keep answers concise.

## Future Improvements

* Add element information panel
* Add search functionality
* Add element property database
* Improve UI styling
* Add offline chemistry dataset

## Author

Sepide Taleb
