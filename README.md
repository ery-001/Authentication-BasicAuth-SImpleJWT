# Authentication (Basic Auth + SimpleJWT)

Django REST Framework authentication app with email registration, account activation, JWT login, and password reset.

## Features

- User registration (inactive until email activation)
- Email activation links (`/api/auth/activate/<uid>/<token>/`)
- Login that returns SimpleJWT `access` and `refresh` tokens
- Password reset flow
- Custom user model support via Django `get_user_model()`

## Stack

- Django + Django REST Framework
- `djangorestframework-simplejwt`
- Django email (`send_mail`) for activation

## API endpoints

| Method | Path | Description |
|--------|------|-------------|
| POST | `register/` | Create account and send activation email |
| GET | `activate/<uidb64>/<token>/` | Activate account |
| POST | `login/` | Authenticate; returns JWT pair |
| POST | `password-reset/` | Request password reset |

## Setup

1. Place this `authentication` app inside a Django project (or add a project package that includes it in `INSTALLED_APPS`).
2. Install dependencies (example):

```bash
pip install django djangorestframework djangorestframework-simplejwt
```

3. Configure email settings and include the app URLs, for example:

```python
path("api/auth/", include("authentication.urls")),
```

4. Run migrations and start the server:

```bash
python manage.py migrate
python manage.py runserver
```

## Notes

- Registered users are created with `is_active=False` until they verify email.
- Activation links in development point at `http://localhost:8000`.
