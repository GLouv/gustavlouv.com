#!/bin/bash
# Development startup script for Gustav Louv website

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${BLUE}🚀 Starting Gustav Louv Website (Development)${NC}"
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo -e "${RED}❌ Virtual environment not found${NC}"
    echo "Run: python3 -m venv venv"
    exit 1
fi

# Activate virtual environment
echo -e "${GREEN}✓ Activating virtual environment${NC}"
source venv/bin/activate

# Check if dependencies are installed
if ! python -c "import fastapi" 2>/dev/null; then
    echo -e "${RED}❌ Dependencies not installed${NC}"
    echo "Run: pip install -r requirements.txt"
    exit 1
fi

echo -e "${GREEN}✓ Dependencies OK${NC}"

# Check if .env file exists
if [ ! -f ".env" ]; then
    echo -e "${RED}⚠ .env file not found${NC}"
    echo "Creating from env.example..."
    cp env.example .env
    echo -e "${GREEN}✓ Created .env file - please configure it${NC}"
fi

# Start the development server
echo ""
echo -e "${BLUE}Starting FastAPI server on port 8002...${NC}"
echo -e "${BLUE}Visit: http://localhost:8002${NC}"
echo ""

uvicorn app.main:app --reload --port 8002 --host 0.0.0.0

