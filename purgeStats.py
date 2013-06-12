from pymongo import Connection
from pymongo.database import Database
import redis
import datetime

connection = Connection()

db = Database(connection, 'zip')
r = redis.StrictRedis(host='localhost', port=6379, db=0)

dateTime = datetime.datetime.now()

hosts = r.hgetall('request.hosts')
hostsCount = r.hlen('request.hosts')
requests = r.get('request.count')
xhrRequests = r.get('request.xhr')
cacheHits = r.get('request.cacheHit')
cacheMiss = r.get('request.cacheMiss')
notFound = r.get('request.notFound')

db.stats.insert({'date': dateTime.strftime("%Y-%m-%d"),
                 'hour': dateTime.hour,
                 'time': dateTime.strftime("%H:%M"),
                 'requests': requests,
                 'hosts': hosts,
                 'countHosts': hostsCount,
                 'xhrRequests': xhrRequests,
                 'cacheHits': cacheHits,
                 'cacheMisses': cacheMiss,
                 'notFound': notFound})

if (dateTime.hour is 23):
    r.delete('request.hosts', 'request.count', 'request.xhr', 'request.cacheHit', 'request.cacheMiss', 'request.notFound')
