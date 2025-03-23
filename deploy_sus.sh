#!/bin/bash

echo "🔧 Setting up SUS System Deployment..."
cd ~/Documents/sus-wei || exit

# Install requirements if present
if [ -f "requirements.txt" ]; then
  echo "📦 Installing Python dependencies..."
  pip3 install -r requirements.txt
fi

# Set permissions for all scripts
chmod +x *.py
chmod +x refine_loop.py
chmod +x auto_sync.py

# Run validator
echo "✅ Validating System..."
python3 validate.py

echo "🧠 Deployment Complete."
echo "📂 SUS is ready at ~/Documents/sus-wei"
