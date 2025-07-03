from pymongo import MongoClient
import os

# MongoDB setup
client = MongoClient('mongodb://localhost:27017/')
db = client['garden_planner_project']
plants = db['plants']

# Path where images are stored (relative to static folder)
image_dir = 'static/images'

# Get all image filenames in static/images
image_files = {f.lower(): f for f in os.listdir(image_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp'))}

# Update each plant with matching image_url
for plant in plants.find():
    name = plant['name'].replace(" ", "").lower()
    matched_file = None

    # Match file based on cleaned plant name
    for ext in ['.jpg', '.jpeg', '.png', '.webp']:
        filename = name + ext
        if filename in image_files:
            matched_file = image_files[filename]
            break

    if matched_file:
        image_url = f"/static/images/{matched_file}"
        plants.update_one({'_id': plant['_id']}, {'$set': {'image_url': image_url}})
        print(f"✅ Updated {plant['name']} with {image_url}")
    else:
        print(f"⚠️ No image found for {plant['name']}")
