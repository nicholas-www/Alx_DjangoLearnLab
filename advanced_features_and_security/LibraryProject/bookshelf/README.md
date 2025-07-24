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
