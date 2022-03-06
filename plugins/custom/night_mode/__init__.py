""" Night Mode for groups """
import os
from userge import config

from pymongo import MongoClient

from apscheduler.jobstores.mongodb import MongoDBJobStore
from apscheduler.schedulers.asyncio import AsyncIOScheduler 

TZ = os.environ.get("TIME_ZONE", "Asia/Kolkata")

monclient = MongoClient(config.DB_URI)

jobstores = {
    'default': MongoDBJobStore(client=monclient, database="Userge", collection='APSCHEDULER')
    }

scheduler = AsyncIOScheduler(jobstores=jobstores, timezone=TZ)
