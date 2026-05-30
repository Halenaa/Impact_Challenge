# Hastory Streamlit MVP

A small Streamlit demo for Hastory's role-based belonging experience for international students in Amsterdam.

## Flow

1. Home / Introduction
2. Belonging Profile Questionnaire
3. Result + Identity Match
4. Task Page
5. Task Submission Form
6. Anonymous Resonance Wall
7. Admin Dashboard

## Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

The app stores pilot data in `submissions.db`.
Delete that local file when you want to reset demo data before a new pilot run.

## Admin

The default admin password is:

```text
borrowed-admin
```

For deployment, set `ADMIN_PASSWORD` in Streamlit secrets or as an environment variable.

## MVP Scope

Included:

- Rule-based profile matching
- Six borrowed identities
- Six offline tasks
- SQLite storage
- Anonymous resonance wall with admin approval
- Basic dashboard metrics and CSV export

Not included in v1:

- Login
- AI generation
- Map API
- Photo upload
- Real-time comments
- Payments
- Multi-school permissions
- Native app
