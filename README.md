# Authentication API (JWT + email verification)

Standalone Django REST auth service: register, email activation, JWT login, password reset.

## Layout

```
manage.py
config/              # project settings + urls
authentication/      # User model, serializers, views
requirements.txt
```

## Endpoints

| Method | Path | Description |
|--------|------|-------------|
| POST | `/api/auth/register/` | Create inactive user + send activation email |
| GET | `/api/auth/activate/<uid>/<token>/` | Activate account |
| POST | `/api/auth/login/` | Return access + refresh JWT |
| POST | `/api/auth/password-reset/` | Email password-reset link |

In development, emails are printed to the console (`EMAIL_BACKEND=console`).

## Run

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
