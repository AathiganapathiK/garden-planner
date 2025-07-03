from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client['garden_planner_project']

# Optional: clear existing data (comment this if you want to keep them)
db['plants'].delete_many({})

plants = list([
    # Alliums
    {"name": "Garlic", "type": "Alliums", "light": "Full Sun", "image_url": "/static/images/garlic.jpg"},
    {"name": "Onions", "type": "Alliums", "light": "Full Sun", "image_url": "/static/images/onions.jpg"},

    # Cole Crops
    {"name": "Broccoli", "type": "Cole Crops", "light": "Full Sun"},
    {"name": "Cabbage", "type": "Cole Crops", "light": "Full Sun"},
    {"name": "Cauliflower", "type": "Cole Crops", "light": "Full Sun"},

    # Flowers
    {"name": "Cosmos", "type": "Flowers", "light": "Full Sun"},
    {"name": "Daffodils", "type": "Flowers", "light": "Full Sun"},
    {"name": "Lavender", "type": "Flowers", "light": "Full Sun"},
    {"name": "Lilies", "type": "Flowers", "light": "Partial Shade"},
    {"name": "Marigold", "type": "Flowers", "light": "Full Sun"},
    {"name": "Rose", "type": "Flowers", "light": "Full Sun"},
    {"name": "Sunflower", "type": "Flowers", "light": "Full Sun"},
    {"name": "Tulip", "type": "Flowers", "light": "Partial Shade"},

    # Fruits
    {"name": "Apple", "type": "Fruits", "light": "Full Sun"},
    {"name": "Blueberries", "type": "Fruits", "light": "Partial Shade"},
    {"name": "Grapes", "type": "Fruits", "light": "Full Sun"},
    {"name": "Orange", "type": "Fruits", "light": "Full Sun"},
    {"name": "Strawberries", "type": "Fruits", "light": "Full Sun"},

    # Greens
    {"name": "Lettuce", "type": "Greens", "light": "Partial Shade"},
    {"name": "Spinach", "type": "Greens", "light": "Partial Shade"},

    # Herbs
    {"name": "Basil", "type": "Herbs", "light": "Full Sun"},
    {"name": "Ginger", "type": "Herbs", "light": "Partial Shade"},
    {"name": "Mint", "type": "Herbs", "light": "Partial Shade"},
    {"name": "Mustard", "type": "Herbs", "light": "Full Sun"},
    {"name": "Parsley", "type": "Herbs", "light": "Partial Shade"},
    {"name": "Rosemary", "type": "Herbs", "light": "Full Sun"},

    # Legumes
    {"name": "Beans", "type": "Legumes", "light": "Full Sun"},
    {"name": "Peanut", "type": "Legumes", "light": "Full Sun"},
    {"name": "Peas", "type": "Legumes", "light": "Partial Shade"},

    # Melons/Squashes
    {"name": "Cucumber", "type": "Melons/Squashes", "light": "Full Sun"},
    {"name": "Pumpkin", "type": "Melons/Squashes", "light": "Full Sun"},
    {"name": "Watermelon", "type": "Melons/Squashes", "light": "Full Sun"},

    # Nightshades
    {"name": "Bellpepper", "type": "Nightshades", "light": "Full Sun"},
    {"name": "Tomatoes", "type": "Nightshades", "light": "Full Sun"},

    # Other Vegetables
    {"name": "Asparagus", "type": "Other Vegetables", "light": "Full Sun"},
    {"name": "Corn", "type": "Other Vegetables", "light": "Full Sun"},

    # Roots
    {"name": "Beetroot", "type": "Roots", "light": "Full Sun"},
    {"name": "Carrots", "type": "Roots", "light": "Full Sun"},
    {"name": "Potatoes", "type": "Roots", "light": "Full Sun"},
    {"name": "Radish", "type": "Roots", "light": "Full Sun"}
])

# Insert into MongoDB
db['plants'].insert_many(plants)

print("🌱 All plant data inserted successfully!")
