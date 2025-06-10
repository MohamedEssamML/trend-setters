# Trend Setters: AI-Powered Video Ideation System

![Dashboard Preview](/output/screenshots/dashboard.png)

## Overview
Automated workflow that:
1. Scrapes viral TikTok content in specified niches
2. Analyzes engagement metrics
3. Generates fresh content ideas using AI
4. Organizes into Google Sheets/Notion
5. Optionally assigns to team members

## Features
- Multi-niche content scraping
- AI-powered idea generation
- Engagement metrics analysis
- Google Sheets/Notion integration
- Team assignment system

## Setup
1. Install requirements: `pip install -r requirements.txt`
2. Configure `config.json` with your API keys
3. Run main script: `python main.py`

## Usage
```python
from backend.scraper import TikTokScraper
from backend.ai_processor import ContentGenerator

scraper = TikTokScraper(["skincare", "tech"])
trends = scraper.scrape_viral_content()

generator = ContentGenerator()
ideas = generator.generate_video_ideas(trends)