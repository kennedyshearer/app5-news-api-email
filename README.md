# News Email Digest

A Python application that fetches the latest news articles about a specific topic and delivers them via email as a daily digest.

## Features

- 📰 Fetches latest news articles using the News API
- 📧 Sends formatted email digest with article titles, descriptions, and links
- 🔄 Configurable topic selection (currently set to "Tesla")
- 📅 Daily news updates based on current date
- 🌐 English language news filtering
- 📊 Limits to top 20 most recent articles

## Prerequisites

Before running this application, make sure you have:

- Python 3.6 or higher
- A News API key (free at [newsapi.org](https://newsapi.org/))
- Gmail account with app password enabled
- Required Python packages (see Installation)

## Installation

1. Clone the repository:
```bash
git clone <your-repository-url>
cd <repository-name>
```
2. Install required packages:
```bash
pip install requests
```
