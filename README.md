## Overview
![alt text](/Misc_imaging/logo-no-background.svg "Goodmorning!")

**This is a personal project to provide myself with a good morning text that gives me a nice good morning message.**
- Collects data from my various servers and containers to make sure there are not any errors or downtime
- Collects relevant data from my google calendar for the day.
- Pulls the weather forecast
- Combines all of this data and then is compiled and written via ChatGPT to then send via sms to my device. This is based on either time of day or first event in the calendar.

## Features

- **Host Monitoring:** Collects and reports on network metrics, such as device status and bandwidth usage.
- **Google Calendar Integration:** Fetches upcoming events from my Google Calendar.
- **Weather Information:** Retrieves the current weather and forecasts using a free weather API.
- **ChatGPT Integration:** Processes the collected data and generates a summary using the ChatGPT API.
- **SMS Notifications:** Sends a daily "Good Morning" message with the summary via SMS.

## Technologies Used

- **Python:** Core programming language.
- **Docker:** Containerizes the application for consistent deployment.
- **Google APIs:** Accesses Google Calendar data.
- **OpenWeatherMap API (or similar):** Fetches weather data.
- **OpenAI API (ChatGPT):** Generates natural language summaries.
- **Twilio (or similar):** Sends SMS notifications.


## Future Improvements

- Expand network monitoring capabilities.
- Add support for additional calendar and weather services.
- Enhance natural language processing with more contextual data.
