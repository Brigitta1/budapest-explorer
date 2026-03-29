#The main file of the project

import random

places = [
    {
        "name": "Gellért Hill",
        "fact": "Offers one of the best panoramic views of Budapest",
        "mission": "Take a photo that captures 'height' or 'perspective'"
    },
    {
        "name": "Fisherman’s Bastion",
        "fact": "Neo-Romanesque terrace with fairy-tale towers",
        "mission": "Photograph patterns or repetition"
    },
    {
        "name": "Margaret Island",
        "fact": "A peaceful green island in the middle of the Danube",
        "mission": "Capture something that feels calm and slow"
    }
]

today = random.choice(places)

print("📍 Today’s place:", today["name"])
print("📖 Fact:", today["fact"])
print("🎯 Mission:", today["mission"])
