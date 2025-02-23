# NASA APOD Telex Integration

A **Telex Interval Integration** that fetches [NASA’s Astronomy Picture of the Day (APOD)](https://apod.nasa.gov/apod/) and posts it to a Telex channel every day at a scheduled time (e.g., 8 AM). Optionally, the integration can cross-post the same content to Slack and Twitter.

---

## Table of Contents
1. [Project Description](#project-description)  
2. [Features](#features)  
3. [Project Structure](#project-structure)  
4. [Technologies Used](#technologies-used)  
5. [Setup Instructions](#setup-instructions)  
6. [Configuration](#configuration)  
7. [Running the Application](#running-the-application)  
8. [Telex Integration Setup](#telex-integration-setup)  
9. [Usage & Endpoints](#usage--endpoints)  
12. [Contributing](#contributing)  
13. [License](#license)  
14. [Support](#support)  

---

## Project Description
This integration automatically retrieves NASA’s Astronomy Picture of the Day (APOD) and its description, then posts it to a **Telex channel** on a set schedule. By default, it fetches data every morning at 8 AM, but you can adjust this interval. Optionally, it can also post to Slack and Twitter if those integrations are configured.

**Key Objectives:**
- Deliver daily, educational, and visually appealing astronomy content.
- Increase user engagement in Telex channels (and optionally Slack/Twitter).
- Provide a straightforward example of a **Telex Interval Integration**.

---

## Features
- **Daily Scheduling**: Uses an interval scheduler (e.g., cron) to fetch the APOD data once a day.  
- **Rich Content Delivery**: Retrieves image URLs, titles, and descriptions from NASA’s API.  
- **Multi-Platform Support**: Optionally cross-post the same message to Slack channels and/or Twitter feeds.  
- **Configurable Settings**: Choose the exact time for daily posting, specify Slack/Twitter credentials, and set the Telex channel ID.  

---

## Project Structure

```plaintext
├── src/
│   ├── resources/
│   │   ├── __init__.py
│   │   └── ...
│   ├── routes/
│   │   ├── __init__.py
│   │   └── ...
│   ├── utilities/
│   │   ├── __init__.py
│   │   ├── apod_manager.py       # Core logic to fetch & format APOD data
│   │   ├── error_handlers.py     # Error handling logic
│   │   └── config.py             # Environment & scheduling config
│   ├── server.py                 # Main server setup (Flask or FastAPI)
├── .env                          # Environment variables (NASA_API_KEY, etc.)
├── integration_settings.json     # Telex integration JSON spec
├── README.md                     # This README
├── requirements.txt              # Python dependencies
├── sample.env                    # Example environment file
└── ...
```

**Notable Files:**
- `server.py`: Entry point that sets up the web server (Flask/FastAPI).
- `apod_manager.py`: Contains logic to fetch the APOD data from NASA and handle message formatting.
- `integration_settings.json`: Defines the Telex Interval Integration spec (e.g., `tick_url`, `settings`, etc.).

---

## Technologies Used
- **Python 3.XX**
- **Flask** 
- **Requests**
- **Deployment Platform**: [Render](https://napod.onrender.com)
- **Version Control**: GitHub


---

## Setup Instructions

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/telexintegrations/NASA-Astronomy-Picture-of-the-Day-Integration.git
   cd NASA-Astronomy-Picture-of-the-Day-Integration
   ```

2. **Create a Virtual Environment**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment**  
   - Copy `sample.env` to `.env`.
   - Set your environment variables (e.g., `NASA_API_KEY`, `TELEX_CHANNEL_ID`, etc.).

---

## Configuration

1. **Environment Variables** (in your `.env` file):
   - `NASA_API_KEY`: Your free NASA API key from [https://api.nasa.gov/](https://api.nasa.gov/).
   - `TELEX_CHANNEL_ID`: The Telex channel where the APOD content should be posted.
   - `POST_TO_SLACK` (optional): Boolean or string indicating if Slack posting is enabled.
   - `SLACK_WEBHOOK_URL` (optional): Slack webhook for cross-posting.
   - `POST_TO_TWITTER` (optional): Boolean or string indicating if Twitter posting is enabled.
   - `TWITTER_API_KEY` & `TWITTER_API_SECRET` (optional): Credentials for posting to Twitter.
   - `SCHEDULE_CRON`: Cron expression (e.g., `0 8 * * *`) specifying the daily fetch time.

2. **Telex Integration Settings** (`integration_settings.json`):
   - Make sure the `integration_type` is set to `"interval"`.
   - Define your `tick_url`, `settings`, and default values as per the [Telex Integration Settings Spec](https://docs.telex.im/docs/Integrations/creating_integration).

---

## Running the Application

1. **Local Development**  
   Run the Flask application:
   ```bash
   ./run.sh # for linux or macOS
   ```

   or 

   ```bash
    python3 -m src.server # for windows
   ```

2. **Scheduling the Integration**  
   - The application should run continuously to ensure it can receive the Telex `/api/napod-tick` calls at the defined interval.
   - Alternatively, if you use an internal scheduler (like `APScheduler`), it will trigger the APOD fetch at the specified time (e.g., 8 AM daily).

3. **Verifying the Endpoint**  
   - For an interval integration, Telex calls the `/api/napod-tick` endpoint at the scheduled interval.

---

## Telex Integration Setup

1. **Host Your Integration JSON**  
   - Ensure `integration_settings.json` is accessible via a public URL

2. **Add Integration to Telex**  
   - In your Telex organization, go to **Apps** → **Add Integration**.
   - Provide the URL of your hosted `integration_settings.json`.
   - Once Telex loads it, click **Install** or **Activate** for your chosen channel(s).

3. **Configure Settings**  
   - In the Telex dashboard, set any required settings (e.g., `nasa_api_key`, `schedule_time`, etc.) as defined in your `integration_settings.json`.

4. **Enable Cross-Posting**  
   - If you want Slack/Twitter cross-posting, ensure those integrations are also activated and that your `.env` or Telex settings reflect the correct credentials.

---

## Usage & Endpoints

- **`GET /api/integration.json`**
   - Fetches the Telex integration configuration

- **`POST | GET /api/napod-tick`**  
  - Called by Telex at the interval you set in the integration.  
  - Fetches APOD data from NASA’s API, formats the content, and posts it to the configured Telex channel.  
  - Optionally cross-posts to Slack/Twitter if enabled.

   - `return_url` for channel is expected when making a post request
   ```bash
      curl -XPOST  https://napod.onrender.com/api/tick -H "accept: application/json"   -H "Content-Type: application/json"   -d '{
         "return_url": "https://ping.telex.im/v1/webhooks/01952fb5-b579-7754-9218-6fafaa359a21",
         }'
  ```
  - `return_url` default to NAPOD telex channel for get requests.

   ![Telex integration](https://github.com/telexintegrations/NASA-Astronomy-Picture-of-the-Day-Integration/blob/main/images/NAPOD-telex.png)


- **Optional Health Check** (e.g., `GET /api/healthcheck`)  
  - Returns a simple JSON message indicating that the integration is running.

---

## Contributing

1. **Fork the Repository**  
2. **Create a Feature Branch** (`git checkout -b feature/amazingFeature`)  
3. **Commit Changes** (`git commit -m 'Add amazingFeature'`)  
4. **Push to Branch** (`git push origin feature/amazingFeature`)  
5. **Open a Pull Request**  

We welcome improvements, bug fixes, and feature additions!

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## Support

- **Issues**: If you encounter any problems or have questions, please open an issue on the GitHub repository.  
- **Telex Docs**: For more details on building integrations, refer to the [Telex Documentation](https://docs.telex.im/).  
- **NASA APOD**: Learn more about NASA’s APOD at [https://api.nasa.gov/](https://api.nasa.gov/).

---

