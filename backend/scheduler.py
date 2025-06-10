from apscheduler.schedulers.background import BackgroundScheduler
from scraper import scrape_tiktok_trends
from ai_processor import generate_content
from database import save_trend

def scheduled_task():
    trends = scrape_tiktok_trends()
    contents = generate_content(trends)
    for trend, content in zip(trends, contents):
        save_trend(trend['hashtag'], trend['views'], content)
    print("Scheduled task completed: Trends saved.")

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(scheduled_task, 'interval', minutes=60)  # Runs every hour
    scheduler.start()