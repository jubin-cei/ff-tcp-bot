# God Blaze - Free Fire TCP Bot

A Free Fire TCP bot for automated gameplay interactions.

## Requirements

- Python 3.8 or higher
- Windows/Linux/MacOS

## Installation

### 1. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure Credentials

Edit `God_Blaze.txt` with your Free Fire account details:

```
uid=YOUR_UID_HERE
password=YOUR_ENCRYPTED_PASSWORD_HERE
```

**Note:** The password should be AES-encrypted. Use the existing format as reference.

## Running the Bot

### Option 1: Direct Run

```bash
python main.py
```

### Option 2: Using Virtual Environment (Recommended)

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

**Linux/MacOS:**

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
```

## Features

The bot supports various commands for Free Fire interactions:

- Message automation
- Squad chat features
- Room management
- Badge customization
- Title management
- Guild information retrieval
- Player statistics
- And more...

## Commands

Once the bot is running and connected, you can use various commands in the Free Fire chat. Admin commands are restricted to whitelisted UIDs.

## Important Notes

- Keep your credentials secure (God_Blaze.txt is excluded from git)
- Token refresh happens automatically every 5 hours
- The bot connects to Free Fire servers based on your region
- Ensure stable internet connection for best performance

## Troubleshooting

**Import Errors:**

- Make sure all dependencies are installed: `pip install -r requirements.txt`

**Connection Issues:**

- Check your internet connection
- Verify credentials in God_Blaze.txt
- Ensure Free Fire servers are accessible

**Module Not Found:**

- Activate virtual environment if using one
- Reinstall dependencies: `pip install -r requirements.txt --force-reinstall`
