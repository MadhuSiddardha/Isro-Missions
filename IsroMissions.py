# import pandas as pd

# data=pd.read_csv(r"C:\Users\kalam\Downloads\ISRO mission launches.csv")
# print("data")

import pandas as pd

# Load the ISRO dataset
dataset_path = r"C:\Users\kalam\Downloads\ISRO mission launches.csv"
isro_data = pd.read_csv(dataset_path, encoding="ISO-8859-1")

# Rename columns for easier access
isro_data.columns = ["serial", "mission_name", "launch_date", "vehicle", "orbit", "application", "remarks"]

# Display the dataset to confirm successful loading and renaming
print("Dataset Loaded Successfully.")

# Chatbot Functionality
def chatbot():
    print("Welcome to the ISRO Mission Chatbot!")
    print("You can ask about specific missions, vehicles, or applications.")

    while True:
        user_input = input("\nAsk me about an ISRO mission or type 'exit' to quit: ").strip().lower()

        if user_input == 'exit':
            print("Thank you for using the ISRO Mission Chatbot. Goodbye!")
            break

        # Search by mission name
        mission = isro_data[isro_data["mission_name"].str.contains(user_input, case=False, na=False)]
        if not mission.empty:
            print("\nMission Details:")
            print(mission)
            continue

        # Search by vehicle
        vehicle = isro_data[isro_data["vehicle"].str.contains(user_input, case=False, na=False)]
        if not vehicle.empty:   
            print("\nMissions by Vehicle:")
            print(vehicle)
            continue

        # Search by application
        application = isro_data[isro_data["application"].str.contains(user_input, case=False, na=False)]
        if not application.empty:
            print("\nMissions by Application:")
            print(application)
            continue

        # If no matches found
        print("\nSorry, I couldn't find any information related to your query. Please try again.")

# Run the chatbot
if __name__ == "__main__":
    chatbot()