# GovSoft

Hukumat tashkilotlari va tizimlarni boshqarish API.

## Quick Start

### Clone & Setup
```bash
git clone git@github.com:mastersherkulov/govsoft.git
cd govsoft
cp .env.example .env
```

### Docker (Tavsiya etiladi)
```bash
docker-compose up -d
```

API: `http://localhost:8080`

## Stack
- Django 5.0, DRF, PostgreSQL 15
- JWT Auth, Docker

## API Docs
- Swagger: `http://localhost:8080/swagger/`
- Redoc: `http://localhost:8080/redoc/`
- Admin: `http://localhost:8080/admin/`
