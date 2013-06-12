from pymongo import Connection
from pymongo.database import Database
import redis
import json
import datetime

connection = Connection()

db = Database(connection, 'zip')
r = redis.StrictRedis(host='localhost', port=6379, db=0)

dateTime = datetime.datetime.now()

hosts = r.hgetall('request.hosts')
hostsCount = r.hlen('reqest.hosts')
requests = r.get('request.count')
xhrRequests = r.get('request.xhr')
cacheHits = r.get('request.cacheHit')
cacheMiss = r.get('request.cacheMiss')
notFound = r.get('request.notFound')

db.stats.insert({'date': datetime.strftime("%Y-%m-%d %H:%M"),
                 'requests': requests,
                 'hosts': hosts,
                 'countHosts': hostsCount,
                 'xhrRequests': xhrRequests,
                 'cacheHits': cacheHits,
                 'cacheMisses': cacheMiss,
                 'notFound': notFound})
