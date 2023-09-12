#!/usr/bin/env python3

import cgi

def recommend_dish(cuisine, spicy_level):
    # Replace this with your recommendation logic
    recommendations = {
        "italian": {
            "mild": "Margherita Pizza",
            "medium": "Pasta Alfredo",
            "hot": "Arrabbiata Pasta"
        },
        "indian": {
            "mild": "Paneer Tikka",
            "medium": "Chicken Curry",
            "hot": "Vindaloo"
        },
        "chinese": {
            "mild": "Spring Rolls",
            "medium": "Kung Pao Chicken",
            "hot": "Mapo Tofu"
        }
    }

    return recommendations.get(cuisine, {}).get(spicy_level, "No recommendation available")
# Read user input
form = cgi.FieldStorage()
selected_cuisine = form.getvalue("cuisine", "")
selected_spicy = form.getvalue("spicy", "")

# Generate recommendation
recommendation = recommend_dish(selected_cuisine, selected_spicy)

# Print recommendation as a response
print("Content-Type: text/html\n")
print(f"<p>Recommended Dish: {recommendation}</p>")