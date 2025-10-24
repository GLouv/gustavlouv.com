#!/bin/bash
# Restart script - kills existing server and starts fresh

echo "🔄 Restarting development server..."

# Kill any existing uvicorn processes on port 8002
lsof -ti:8002 | xargs kill -9 2>/dev/null || true

# Start the server
./scripts/development/start.sh

