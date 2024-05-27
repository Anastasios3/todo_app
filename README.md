![image](https://github.com/Anastasios3/todo_app/assets/117446378/da269659-f25b-4709-8a44-cea6e5060bc6)


To-Do List Application

This is a minimal To-Do List application built with Flask. The application allows users to add, complete, and delete tasks. The application data is stored in a SQLite database, and the interface is designed to be simple and user-friendly.

## Features

- Add new tasks to the to-do list.
- Mark tasks as completed.
- Delete tasks from the list.
- Data persistence using SQLite.
- Minimal and clean user interface.

## Requirements

- Python 3.6+
- Flask
- Flask-SQLAlchemy
- PyInstaller (for creating executable)

## Installation

1. **Clone the Repository**

```sh
git clone https://github.com/Anastasios3/todo_app.git
cd todo_app
```

2. **Create a Virtual Environment**

```sh
python -m venv todo_env
```

3. **Activate the Virtual Environment**

For Windows:
```sh
todo_env\Scripts\activate
```

For macOS/Linux:
```sh
source todo_env/bin/activate
```

4. **Install the Required Packages**

```sh
pip install -r requirements.txt
```

## Configuration

Make sure you have a `config.py` file in the root directory of the project with the following content:

```python
import os

class Config:
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../instance/todo_app.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
```

## Running the Application

1. **Initialize the Database**

```sh
flask shell
```

In the Flask shell, run the following commands:

```python
from app import db
db.create_all()
exit()
```

2. **Run the Application**

```sh
python run.py
```

3. **Open the Application in Your Browser**

Navigate to `http://127.0.0.1:5000` in your browser to use the application.

## Creating an Executable

1. **Install PyInstaller**

```sh
pip install pyinstaller
```

2. **Create the Executable**

```sh
pyinstaller --onefile --windowed todo_app.spec
```

3. **Locate the Executable**

The executable will be located in the `dist` directory.

## Directory Structure

```
todo_app/
│
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   └── templates/
│       └── index.html
│
├── instance/
│   └── todo_app.sqlite
│
├── static/
│   └── style.css
│
├── config.py
├── run.py
├── requirements.txt
├── todo_app.spec
└── README.md
```

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

If you have any questions or suggestions, feel free to reach out.

- **Email**: tatarakis.a@gmail.com
- **GitHub**: Anastasios3 - https://github.com/Anastasios3
