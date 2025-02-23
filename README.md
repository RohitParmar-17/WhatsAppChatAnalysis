# WhatsApp Chat Analyzer

## Overview
The WhatsApp Chat Analyzer is a tool that allows users to analyze chat data exported from WhatsApp to identify various underlying relationships and generate insightful visualizations. It supports chat logs in a 24-hour format (AM-PM) and provides detailed analytics.

## Screenshots
Here are some screenshots of the WhatsApp Chat Analyzer in action:

<img src="https://github.com/RohitParmar-17/WhatsAppChatAnalysis/blob/main/screenshots/wp1.png" alt="Chat Statistics" width="100%">

<img src="https://github.com/RohitParmar-17/WhatsAppChatAnalysis/blob/main/screenshots/wp2.png" alt="Chat Statistics" width="100%">

<img src="https://github.com/RohitParmar-17/WhatsAppChatAnalysis/blob/main/screenshots/wp3.png" alt="Chat Statistics" width="100%">

## Features
- **Message Statistics**: Get an overview of total messages, word count, and media files.
- **Most Active Users**: Identify the most active participants in a group chat.
- **Word Cloud**: Visual representation of the most frequently used words.
- **Emoji Analysis**: Breakdown of emoji usage across the conversation.
- **Time-Based Analysis**: Insights into chat activity by hour, day, and month.
- **Weekly & Monthly Trends**: Identify trends and peak activity periods.

## Tech Stack
- **Python Libraries**: Streamlit, Matplotlib, Seaborn, URLExtract, WordCloud, Pandas, Emoji

## Installation
### Prerequisites
Ensure you have Python installed on your system.

### Steps to Run Locally
1. **Clone the Repository**
   ```sh
   git clone https://github.com/RohitParmar-17/WhatsAppChatAnalysis.git
   cd WhatsAppChatAnalysis
   ```

2. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
   ```

3. **Run the Application**
   ```sh
   streamlit run app.py
   ```
   The app will be accessible at the provided local URL.

## Usage
1. Export a WhatsApp chat and save it as a `.txt` file.
2. Upload the chat file in the application.
3. Explore various analytics, including message frequency, word clouds, and emoji trends.

## Deployment
To deploy the project using Streamlit Sharing or a cloud platform:
1. Create a Streamlit account and deploy via Streamlit Sharing.
2. Use `Heroku`, `AWS`, or `Google Cloud` for manual deployment.

## Contributing
If you’d like to contribute:
- Fork the repository
- Create a new branch (`git checkout -b feature-branch`)
- Make your changes and commit (`git commit -m "Added new feature"`)
- Push to the branch (`git push origin feature-branch`)
- Open a pull request


## Contact
For any issues or suggestions, feel free to reach out:
- **Email**: rohitghost5050@gmail.com

