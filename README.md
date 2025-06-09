## Django Template

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template/GB6Eki?referralCode=U5zXSw)

## Environment Variables

This application uses environment variables for configuration. Copy the `.env.example` file to `.env` to get started:

```
cp .env.example .env
```

Then edit the `.env` file with your specific configuration values:

- `SECRET_KEY`: Django secret key (keep this private and secure)
- `DEBUG`: Set to True for development, False for production
- `ALLOWED_HOSTS`: Comma-separated list of allowed hosts
- Database configuration (`PGDATABASE`, `PGUSER`, etc.)

**Important**: Never commit your `.env` file to version control.
