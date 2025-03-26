import pandas as pd
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gift_recommend.settings")
django.setup()  # This initializes Django settings

from recommendation.models import Recipient


# from recommendation.models import Recipient


def import_file():
    # Path to the CSV file (you can adjust this based on where your file is)
    print(1)
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DATASET_PATH = os.path.join(BASE_DIR, "personalized_gift_recommendation.csv")

    # Read the CSV file using pandas
    df = pd.read_csv(DATASET_PATH)

    # Loop through each row in the dataframe and save it to the database
    for _, row in df.iterrows():
        # Create and save a new Student instance for each row
        student = Recipient(
            user_location=row['user_location'],
            user_age=row['user_age'],
            user_gender=row['user_gender'],
            recipient_relationship=row['recipient_relationship'],
            recipient_age=row['recipient_age'],
            recipient_gender=row['recipient_gender'],
            recipient_interests=row['recipient_interests'],
            special_occasion=row['special_occasion'],
            budget_preference=row['budget_preference'],
            gift_name=row['gift_name'],
            category=row['category'],
            brand=row['brand'],
            price=row['price'],
            description=row['description'],
            gift_rating=row['gift_rating']


        )
        print(student)

        student.save()


import_file()