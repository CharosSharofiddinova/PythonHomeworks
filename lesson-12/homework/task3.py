import requests
from bs4 import BeautifulSoup
import json
import time

BASE_URL = "https://www.demoblaze.com/"
API_URL = "https://api.demoblaze.com/bycat"
NEXT_BUTTON_ID = "next2"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Content-Type": "application/json"
}

def get_laptops():
    payload = {"cat": "laptops"}
    response = requests.post(API_URL, json=payload, headers=HEADERS)
    
    if response.status_code != 200:
        print("Failed to fetch laptop data")
        return []
    
    laptops_data = response.json().get("Items", [])
    laptops = []
    
    for item in laptops_data:
        laptops.append({
            "name": item.get("title", "Unknown"),
            "price": f"${item.get('price', 'N/A')}",
            "description": item.get("desc", "No description available")
        })
    
    return laptops

def save_to_json(data, filename="laptops.json"):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    print(f"Data saved to {filename}")

if __name__ == "__main__":
    laptops = get_laptops()
    if laptops:
        save_to_json(laptops)
    else:
        print("No laptops found.")
