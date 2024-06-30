# Mental Health Companion Chatbot: Diagnose, Support, Guide
This is an interface for web based chatbot that used Microsoft Azure Health Bot service and Streamlit web interface.
## Requirements
1. Webchat secret from your Azure Health Bot service (free tier available)
2. Python language
## Steps
1. Install `streamlit`
   ```
   pip install streamlit
   ```
2. In `chatbot.py`, replace `YOUR_WEBCHAT_SECRET` variable to yoour own webchat secret.
   ```
   headers: {
            'Authorization': `YOUR_WEBCHAT_SECRET`
          }
   ```
3. Run the app.
   ```
   streamlit chatbot.py
   ```
### Localtunnel Option
If you are not able to run it directly from step #3, you can you npm and localtunnel.
1. Install the localtunnel
   ```
   npm install localtunnel
   ```
2. Run the app using localtunnel and curl.
   ```
   streamlit run chatbot.py --server.address=localhost &>/content/logs.txt &
   npx localtunnel --port 8501 & curl ipv4.icanhazip.com
   ```
## Demonstration
The interface will look similar to this.


https://github.com/khalishaputri18/azure-mental-health-chatbot/assets/66949610/7ab8e08c-ccd6-4876-a091-bff76ad964e6

