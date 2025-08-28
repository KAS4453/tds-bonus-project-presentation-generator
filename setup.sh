# This is a bash script. Save it as `setup.sh` and run `bash setup.sh` in your terminal,
# or copy and paste these commands into your terminal one by one.

# --- 1. Create Project Directory Structure ---
# This creates the main folder for our project and subfolders for backend and frontend.
echo "Step 1: Creating project directories..."
mkdir decksmith-ai
cd decksmith-ai
mkdir backend
mkdir frontend
echo "Done."

# --- 2. Set up Python Virtual Environment in Backend ---
# We'll work inside the backend folder now.
echo "Step 2: Setting up Python backend..."
cd backend

# Create a virtual environment named 'venv'. This keeps our project's Python packages separate.
python3 -m venv venv

# Activate the virtual environment. You must do this every time you open a new terminal for this project.
# On Windows, the command is: venv\Scripts\activate
source venv/bin/activate
echo "Virtual environment activated."

# --- 3. Install Required Python Packages ---
# This installs the libraries we need for our server, PowerPoint handling, and Google's AI.
echo "Step 3: Installing Python packages..."
pip install Flask python-pptx google-generativeai python-dotenv Flask-Cors
echo "Packages installed."

# --- 4. Create Initial Backend Files ---
echo "Step 4: Creating initial backend files..."
# Create the main application file.
touch app.py

# Create a file to list our Python packages for deployment.
pip freeze > requirements.txt

# Create a file to ignore files we don't want to save to Git (like our virtual environment).
touch .gitignore

# Create a file to store our secret API key.
touch .env
echo "Backend setup complete. Your directory 'decksmith-ai/backend' is ready."