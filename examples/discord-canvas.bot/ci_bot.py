import discord
import csv
import requests

# Discord bot token and channel ID
DISCORD_TOKEN = 'your_discord_bot_token'
CHANNEL_ID = 123456789012345678  # Replace with your channel ID

# GitHub API token
GITHUB_TOKEN = 'your_github_token'

# CSV file path
CSV_FILE_PATH = 'path/to/your/local.csv'

# Initialize Discord client
client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.channel.id == CHANNEL_ID and 'pull request' in message.content.lower():
        # Extract pull request URL from the message
        pr_url = extract_pr_url(message.content)
        if pr_url:
            # Fetch pull request details
            pr_details = fetch_pr_details(pr_url)
            if pr_details:
                # Check against CSV
                is_valid = check_against_csv(pr_details)
                # Respond on Discord
                response = 'Submission is valid.' if is_valid else 'Submission is invalid.'
                await message.channel.send(response)

def extract_pr_url(content):
    # Logic to extract pull request URL from the message content
    return 'extracted_pr_url'

def fetch_pr_details(pr_url):
    headers = {'Authorization': f'token {GITHUB_TOKEN}'}
    response = requests.get(pr_url, headers=headers)
    if response.status_code == 200:
        return response.json()
    return None

def check_against_csv(pr_details):
    with open(CSV_FILE_PATH, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            # Logic to check if the pull request details match any CSV entry
            if row['student_id'] == pr_details['user']['id']:
                return True
    return False

# Run the Discord client
client.run(DISCORD_TOKEN)
import discord
import csv
import requests

# Discord bot token and channel ID
DISCORD_TOKEN = 'your_discord_bot_token'
CHANNEL_ID = 123456789012345678  # Replace with your channel ID

# GitHub API token
GITHUB_TOKEN = 'your_github_token'

# CSV file path
CSV_FILE_PATH = 'path/to/your/local.csv'

# Initialize Discord client
client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.channel.id == CHANNEL_ID and 'pull request' in message.content.lower():
        # Extract pull request URL from the message
        pr_url = extract_pr_url(message.content)
        if pr_url:
            # Fetch pull request details
            pr_details = fetch_pr_details(pr_url)
            if pr_details:
                # Check against CSV
                is_valid = check_against_csv(pr_details)
                # Respond on Discord
                response = 'Submission is valid.' if is_valid else 'Submission is invalid.'
                await message.channel.send(response)

def extract_pr_url(content):
    # Logic to extract pull request URL from the message content
    return 'extracted_pr_url'

def fetch_pr_details(pr_url):
    headers = {'Authorization': f'token {GITHUB_TOKEN}'}
    response = requests.get(pr_url, headers=headers)
    if response.status_code == 200:
        return response.json()
    return None

def check_against_csv(pr_details):
    with open(CSV_FILE_PATH, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            # Logic to check if the pull request details match any CSV entry
            if row['student_id'] == pr_details['user']['id']:
                return True
    return False

# Run the Discord client
client.run(DISCORD_TOKEN)
import discord
import csv
import requests

# Discord bot token and channel ID
DISCORD_TOKEN = 'your_discord_bot_token'
CHANNEL_ID = 123456789012345678  # Replace with your channel ID

# GitHub API token
GITHUB_TOKEN = 'your_github_token'

# CSV file path
CSV_FILE_PATH = 'path/to/your/local.csv'

# Initialize Discord client
client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.channel.id == CHANNEL_ID and 'pull request' in message.content.lower():
        # Extract pull request URL from the message
        pr_url = extract_pr_url(message.content)
        if pr_url:
            # Fetch pull request details
            pr_details = fetch_pr_details(pr_url)
            if pr_details:
                # Check against CSV
                is_valid = check_against_csv(pr_details)
                # Respond on Discord
                response = 'Submission is valid.' if is_valid else 'Submission is invalid.'
                await message.channel.send(response)

def extract_pr_url(content):
    # Logic to extract pull request URL from the message content
    return 'extracted_pr_url'

def fetch_pr_details(pr_url):
    headers = {'Authorization': f'token {GITHUB_TOKEN}'}
    response = requests.get(pr_url, headers=headers)
    if response.status_code == 200:
        return response.json()
    return None

def check_against_csv(pr_details):
    with open(CSV_FILE_PATH, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            # Logic to check if the pull request details match any CSV entry
            if row['student_id'] == pr_details['user']['id']:
                return True
    return False

# Run the Discord client
client.run(DISCORD_TOKEN)
