# TaskFlow

TaskFlow is a lightweight task manager built with Python, PyQt, and SQLite. It helps you create, organize, and track your daily tasks with a minimal and intuitive interface.

## Instalation

## Features

- Create and manage tasks – Easily add, edit, and delete tasks.

- Track progress – Mark tasks as completed and monitor their status.

- Simple and intuitive interface – Minimalist design for easy task management.

- Local storage with SQLite – Keep your tasks saved without needing an internet connection.

## Setting Up for Development

1. Clone the repository:

    ```bash
    git clone https://github.com/limadaniel70/TaskFlow
    ```

2. Navigate to the project directory:

    ```bash
    cd TaskFlow
    ```

3. Create and activatea virtual environment:

    ```bash
    python -m venv .venv
    # or virtualenv .venv
    source venv/bin/activate
    ```

    On windows:

    ```powershell
    py -m venv .venv
    # or virtualenv .venv
    .\venv\Scripts\activate.ps1
    ```

4. Install dependencies:

    ```bash
    # main deps
    pip install -r ./requirements/requirements.txt
    # dev deps
    pip install -r ./requirements/requirements-dev.txt
    ```

## Usage

Activate the virtual environment:

```bash
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate      # Windows
```

Run the app:

```
python app/main.py
```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch:

    ```bash
    git checkout -b feature-name
    ```

3. Commit your changes:

    ```bash
    git commit -m "Add feature-name"
    ```

4. Push to your branch:

    ```bash
    git push origin feature-name
    ```

5. Open a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
