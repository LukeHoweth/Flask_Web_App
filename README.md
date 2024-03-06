# Flask Notes App

Welcome to the Flask Notes App! This simple web application allows users to sign up for an account, store their notes in a SQLAlchemy database, and manage their personal journal entries.

## Features

- **User Authentication**: Users can sign up for an account and securely log in.
- **Note Management**: Add and delete personal notes in your journal.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.x
- Flask
- SQLAlchemy

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/flask-notes-app.git
    cd flask-notes-app
    ```

2. Create a virtual environment (recommended):

    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

4. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Configuration

1. Open the `config.py` file and configure the `SECRET_KEY` for Flask.

## Usage

1. Run the Flask application:

    ```bash
    python app.py
    ```

2. Open your web browser and navigate to [http://localhost:5000](http://localhost:5000).

3. Sign up for a new account.

4. Log in with your credentials.

5. Start adding and deleting notes in your personal journal.

## Contributing

Feel free to contribute to this project! Submit issues for bugs or feature requests, and create pull requests to improve the functionality.
