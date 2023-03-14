#!/usr/bin/env python3
'''script that provides some stats about Nginx logs stored in MongoDB'''

from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    col = db.ngnix
    doc_num = col.count_documents({})
    print(f"{doc_num} logs")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        num1 = col.count_documents({"method": method})
        print(f"\tmethod {method}: {num1}")
    num2 = col.count_documents({"method": "GET", "path": "/status"})
    print(f"{num2} status check")
