# Miguel's Portfolio Site

A personal portfolio built with Flask that automatically pulls project data from the GitHub API, showcasing real repositories with descriptions, creation dates, and links back to each repo.

## Features

- **Dynamic project listing** — pulls repos directly from the GitHub API (name, description, creation date, URL), with forked repos filtered out
- **Caching layer** — GitHub data is cached for 1 hour to avoid hitting API rate limits on every page load
- **Pagination** — projects list is paginated (5 per page) using list slicing
- **Project detail pages** — each project has its own page with a Bootstrap image carousel and a direct link to its GitHub repo
- **Random post route** — jumps to a random project
- **Contact form** — sends emails via Gmail SMTP with `Reply-To` set to the visitor's email, so replies go directly to them
- **About page** — personal introduction

## Tech Stack

- **Backend:** Flask (Python)
- **Frontend:** Bootstrap 5, Jinja2 templates
- **Data:** GitHub REST API
- **Email:** smtplib + Gmail SMTP

## Project Structure

```
my_website/
├── main.py              # Flask routes
├── github_fetcher.py     # GitHub API integration + caching
├── email_sender.py       # Contact form email logic
├── .env                  # Environment variables (not committed)
├── .gitignore
├── static/
│   ├── css/
│   ├── js/
│   └── assets/
└── templates/
    ├── header.html
    ├── footer.html
    ├── index.html         # Home / project listing
    ├── post.html          # Project detail page
    ├── about.html
    └── contact.html
```

## Setup

1. Clone the repo:
```bash
git clone https://github.com/mikeyggg/my_website.git
cd my_website
```

2. Create a virtual environment and install dependencies:
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install flask requests python-dotenv
```

3. Create a `.env` file in the project root with:
```
SITE_PASSWORD=your_gmail_app_password
```

4. Update `GITHUB_USERNAME` in `github_fetcher.py` if forking this project.

5. Run the app:
```bash
python main.py
```

The site will be available at `http://127.0.0.1:5000`.

## Notes

- This project is currently running locally. Deployment (Gunicorn + Nginx) is planned but not yet configured.
- Project images are currently placeholders — real screenshots per project are a planned improvement.

## Author

Miguel Valadez — [GitHub](https://github.com/mikeyggg)
