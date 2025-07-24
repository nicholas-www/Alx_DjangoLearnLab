# Permissions & Groups Setup

This app uses Django's built-in permissions and group system.

## Custom Permissions

The `Article` model has custom permissions:
- `can_view`
- `can_create`
- `can_edit`
- `can_delete`

## Groups and Permissions

- **Viewers**: `can_view`
- **Editors**: `can_view`, `can_create`, `can_edit`
- **Admins**: All permissions

## Usage

- Permissions are enforced in views using `@permission_required`.
- Assign users to groups via the Django Admin.
- Users without proper permissions will receive a 403 Forbidden response.


# 🔐 HTTPS & Web Security Configuration

## Django Security Settings (`settings.py`)
- `SECURE_SSL_REDIRECT = True`: Forces all HTTP requests to HTTPS.
- `SECURE_HSTS_SECONDS = 31536000`: Applies HSTS policy for 1 year.
- `SECURE_HSTS_INCLUDE_SUBDOMAINS = True`: Includes subdomains in HSTS.
- `SECURE_HSTS_PRELOAD = True`: Requests preload listing in browser HSTS preload list.
- `SESSION_COOKIE_SECURE = True`: Session cookie only sent via HTTPS.
- `CSRF_COOKIE_SECURE = True`: CSRF cookie only sent via HTTPS.
- `X_FRAME_OPTIONS = 'DENY'`: Prevents clickjacking.
- `SECURE_CONTENT_TYPE_NOSNIFF = True`: Prevents MIME-type sniffing.
- `SECURE_BROWSER_XSS_FILTER = True`: Enables browser's XSS filter.

## Web Server HTTPS Setup (Nginx)
- HTTPS configured using Let’s Encrypt SSL certificates.
- Redirects all HTTP traffic to HTTPS.
- Enforces HSTS headers for strict HTTPS compliance.

## Recommendations
- Ensure `DEBUG = False` in production.
- Set `ALLOWED_HOSTS` to your actual domains.
- Regularly renew SSL certificates (or use auto-renew with Certbot).