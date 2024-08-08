## Overview
![alt text](Robo_Coffee/Misc_imaging/logo-no-background.svg "Goodmorning!")

This project is a Python-based personal assistant that runs indefinitely in a Docker container. It gathers data from various sources, including your home network, Google Calendar, and a weather API. Using the ChatGPT API, the assistant processes and summarizes the collected information and sends a "Good Morning" message via SMS.

## Features

- **Home Network Monitoring:** Collects and reports on network metrics, such as device status and bandwidth usage.
- **Google Calendar Integration:** Fetches upcoming events from your Google Calendar.
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

## Getting Started

### Prerequisites

- **Docker:** Ensure Docker is installed on your system.
- **API Keys and Credentials:** You'll need API keys for Google, OpenWeatherMap, OpenAI, and Twilio (or an equivalent SMS service).
- **Python Libraries:** Required libraries are listed in `requirements.txt`.

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/my_personal_assistant.git
   cd my_personal_assistant
   ```

2. Set up environment variables for API keys and other sensitive data.

3. Build and run the Docker container:
   ```bash
   docker build -t my_personal_assistant .
   docker run -d --env-file .env my_personal_assistant
   ```

## Future Improvements

- Expand network monitoring capabilities.
- Add support for additional calendar and weather services.
- Enhance natural language processing with more contextual data.
