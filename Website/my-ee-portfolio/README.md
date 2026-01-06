# My Electrical Engineering Portfolio

This project is a personal portfolio website designed to showcase electrical engineering projects and host essays in both text and LaTeX formats. The application is built using Python and Flask, providing a simple and effective way to present your work.

## Project Structure

```
my-ee-portfolio
├── app
│   ├── __init__.py          # Initializes the Flask application
│   ├── routes.py            # Defines the routes for the web application
│   ├── models.py            # Contains data models for projects and essays
│   ├── static
│   │   └── style.css        # CSS styles for the web application
│   ├── templates
│   │   ├── base.html        # Base template for the application
│   │   ├── index.html       # Home page template
│   │   ├── projects.html     # Projects page template
│   │   └── essays.html      # Essays page template
│   └── utils.py             # Utility functions for file handling
├── essays
│   ├── example_essay.txt    # Example essay in plain text format
│   └── example_essay.tex    # Example essay in LaTeX format
├── projects
│   └── project1.md          # Example project details in Markdown format
├── requirements.txt          # Lists project dependencies
├── run.py                   # Entry point for running the application
└── README.md                # Documentation for the project
```

## Setup Instructions

1. **Clone the repository:**

   ```
   git clone https://github.com/leucaniline/my-ee-portfolio.git
   cd my-ee-portfolio
   ```

2. **Install the required dependencies:**

   ```
   pip install -r requirements.txt
   ```

3. **Run the application:**

   ```
   python run.py
   ```

4. **Access the application:**
   Open your web browser and go to `http://127.0.0.1:5000` to view your portfolio.

## Features

- Display a list of electrical engineering projects.
- Host essays in both plain text and LaTeX formats.
- Responsive design with a clean and modern interface.

## Contributing

Feel free to submit issues or pull requests if you have suggestions for improvements or new features.
