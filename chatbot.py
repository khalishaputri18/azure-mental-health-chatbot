import streamlit as st

st.title('Health Bot - Diagnose :stethoscope:')
st.write('Assist you in diagnosing your mental health issues and giving first aid solution.')

html_code = """
<!DOCTYPE html>
<html>
  <head>
    <title>Azure Health Bot</title>
    <style>
      html, body {
        height: 100%;
        margin: 0;
        display: flex;
        justify-content: center;
        align-items: center;
        background-color: #0E1117;
      }
      #webchat-container {
        height: 80vh;
        width: 80vh;
        max-width: 1200px;
        border: 2px solid #3498db;
        border-radius: 20px;
        overflow: hidden;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
      }
      #webchat {
        height: 100%;
        width: 100%;
      }
    </style>
    <script src="https://cdn.botframework.com/botframework-webchat/latest/webchat.js"></script>
  </head>
  <body>
    <div id="webchat-container">
      <div id="webchat" role="main"></div>
    </div>
    <script>
      (async function() {
        const res = await fetch('https://directline.botframework.com/v3/directline/tokens/generate', {
          method: 'POST',
          headers: {
            'Authorization': `YOUR_WEBCHAT_SECRET`
          }
        });
        const { token } = await res.json();

        window.WebChat.renderWebChat(
          {
            directLine: window.WebChat.createDirectLine({ token }),
            userID: 'user1',
            username: 'User'
          },
          document.getElementById('webchat')
        );
      })();
    </script>
  </body>
</html>
"""

st.components.v1.html(html_code, height=800)