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

## Development Tracks

Hastory is currently split into two parallel tracks:

- **Short-term showcase track:** create polished, static card images for team presentations. These card images may include the Hastory logo, identity title, short copy, and front/back card layouts directly inside the image. This track prioritizes storytelling, visual quality, and quick presentation readiness.
- **Long-term product track:** keep the live app logic dynamic. Identity titles, mission text, buttons, review states, and future content should remain editable in code/data and rendered through reusable templates. Visual assets can support the template, but should not permanently lock core product text into images.

Do not mix these tracks by assuming showcase cards are the final product architecture. The short-term cards are presentation assets; the long-term app should continue toward reusable, responsive, data-driven card components.

Showcase assets live in `assets/showcase/`. The current company logo is saved as `assets/showcase/hastory_logo.png`. For short-term card backs, use the real logo file during composition instead of asking an image model to redraw the logo, so the wordmark and illustration stay accurate.

Current showcase card asset naming:

- `shared_kitchen_host_front.png`
- `shared_kitchen_host_back.png`
- `bike_messenger_front.png`
- `bike_messenger_back.png`
- `canal_letter_writer_front.png`
- `canal_letter_writer_back.png`
- `city_signal_collector_front.png`
- `city_signal_collector_back.png`
- `museum_apprentice_front.png`
- `museum_apprentice_back.png`
- `second_hand_explorer_front.png`
- `second_hand_explorer_back.png`

Received showcase cards:

- Shared Kitchen Host: front and back saved.
- Bike Messenger: front and back saved.
- Canal Letter Writer: front and back saved.

Still needed for the full showcase set:

- City Signal Collector: front and back.
- Museum Apprentice: front and back.
- Second-hand Explorer: front and back.

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
hastory
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
