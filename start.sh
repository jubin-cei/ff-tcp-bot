#!/bin/bash

# God Blaze Bot Startup Script
# This script handles graceful startup and shutdown

set -e

echo "🚀 Starting God Blaze Free Fire Bot..."
echo "📅 Date: $(date)"
echo "🌍 Timezone: ${TZ:-UTC}"

# Check if credentials file exists
if [ ! -f "God_Blaze.txt" ]; then
    echo "❌ ERROR: God_Blaze.txt not found!"
    echo "💡 Please create credentials file with:"
    echo "   uid=YOUR_UID"
    echo "   password=YOUR_ENCRYPTED_PASSWORD"
    exit 1
fi

# Check if token file exists (create if doesn't exist)
if [ ! -f "token.json" ]; then
    echo "⚠️  token.json not found, will be created on first run"
    echo "{}" > token.json
fi

# Create cache directory if it doesn't exist
mkdir -p /app/cache

echo "✅ Pre-flight checks passed"
echo "🎮 Launching bot..."
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Trap SIGTERM and SIGINT for graceful shutdown
trap 'echo "🛑 Received shutdown signal, stopping bot..."; exit 0' SIGTERM SIGINT

# Run the bot with unbuffered output
exec python -u main.py
