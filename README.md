# Isro-Missions
ISRO Mission Chatbot
A simple chatbot that allows users to inquire about ISRO missions based on mission name, launch vehicle, or application.

Features
Loads ISRO mission data from CSV
Searches missions by name, vehicle, or application
Interactive chatbot with user-friendly responses
Simple text-based interface
Installation
Ensure you have Python installed (version 3.6+ recommended).

Install required dependencies using:

pip install pandas
Usage
Place the ISRO mission dataset (ISRO mission launches.csv) in the correct path.
Update the dataset_path variable with the correct file location.
Run the script using:
python chatbot.py
Example Commands
"Chandrayaan" → Returns details about Chandrayaan missions.
"PSLV" → Lists all missions launched using the PSLV vehicle.
"Communication" → Displays missions with communication applications.
"exit" → Ends the chatbot session.
Limitations
Data accuracy depends on the CSV file provided.
User queries must closely match dataset entries for accurate results.
The chatbot currently runs in a terminal; no GUI or voice interaction yet.
Future Enhancements
Improve natural language processing for better query handling.
Add voice-based interaction using speech recognition.
Implement data visualization for mission trends and insights.
License
This project is open-source and free to use.
