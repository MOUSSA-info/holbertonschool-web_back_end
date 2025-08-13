#!/usr/bin/env python3
"""
12-log_stats.py
Script that provides some stats about Nginx logs stored in MongoDB
"""

from pymongo import MongoClient

if __name__ == "__main__":
    # Connexion au serveur MongoDB local
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    # Nombre total de logs
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # Affichage des comptes par méthode HTTP
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Compter les requêtes GET sur /status
    status_check_count = collection.count_documents({
        "method": "GET",
        "path": "/status"
    })
    print(f"{status_check_count} status check")
