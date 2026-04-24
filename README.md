# God Blaze - Free Fire TCP Bot

A Free Fire TCP bot for automated gameplay interactions.

## Features

- 60+ in-game commands
- Automated friend/squad interactions
- Chat automation
- Auto-reconnect on disconnect
- Docker support with auto-updates

## Quick Start

### Local Development

```bash
pip install -r requirements.txt
python main.py
```

### Docker

```bash
# Build and run locally
docker-compose up -d

# Use pre-built image from GitHub Container Registry
# 1. Edit docker-compose.auto-update.yml and replace YOUR_GITHUB_USERNAME
# 2. Run:
docker-compose -f docker-compose.auto-update.yml up -d
```

## Configuration

Edit `God_Blaze.txt` with your credentials:

```
uid=YOUR_UID_HERE
password=YOUR_ENCRYPTED_PASSWORD_HERE
```

## GitHub Actions Setup

1. Push code to GitHub
2. Workflow builds Docker image automatically
3. Image pushed to GitHub Container Registry (ghcr.io)
4. Watchtower auto-updates your deployment

**Make package public:**

- Go to GitHub profile → Packages → god-blaze-bot
- Package settings → Change visibility → Public

## Deploy to Claw Cloud

```yaml
services:
  god-blaze-bot:
    image: ghcr.io/YOUR_USERNAME/god-blaze-bot:latest
    restart: unless-stopped
    volumes:
      - ./God_Blaze.txt:/app/God_Blaze.txt:ro
      - ./token.json:/app/token.json
```

## Troubleshooting

- **Import Errors:** `pip install -r requirements.txt`
- **Connection Issues:** Check credentials in God_Blaze.txt
- **Module Not Found:** Reinstall dependencies
