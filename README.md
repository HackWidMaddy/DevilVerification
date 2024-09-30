# DevilVerification

## Overview

**DevilVerification** is a project that demonstrates clipboard injection techniques for executing dynamic payloads based on user input. Inspired by John Hammond's recent video, this tool showcases the risks of social engineering and the ease with which malicious payloads can be executed through deceptive practices.

## Demo Video

Check out the demo video [here](https://github.com/HackWidMaddy/DevilVerification/blob/main/view.mp4).

## Features

- **Admin Portal**: A user-friendly interface built with Streamlit for entering website details, redirect URLs, and payloads.
- **Dynamic Payload Execution**: Generates a spoofed verification page that mimics Cloudflare's security checks.
- **Clipboard Injection**: Automatically copies the specified payload to the user's clipboard.
- **User Instructions**: Provides misleading instructions to trick users into executing the payload.

## Technologies Used

- **Streamlit**: For the frontend user interface.
- **Flask**: For handling API requests and generating dynamic HTML content.
- **HTML/CSS**: For creating the spoofed verification page.

## Installation

### Prerequisites

Ensure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/devilverification.git
cd devilverification
```

Install Dependencies
You can install the required packages using pip:

```bash
pip install streamlit flask
```

Usage
1. Run the Flask API: Navigate to the directory containing the flask.py file and run the following command:
```bash
python flaske.py
```

2.Run the Streamlit Application: In a new terminal window, navigate to the directory containing main.py and run:
```bash
streamlit run main.py
```

3.Access the Admin Portal: Open your web browser and go to http://localhost:8501 to access the admin portal.

4.Create a Slog:
-Enter the Website Name.
-Specify the Redirect To URL.
-Input the Payload you wish to execute.
-Click on Create Slog.

5.Execution: After creating the slog, the application will generate a link to the spoofed verification page. When the user visits this link, the payload will be copied to their clipboard automatically.

## Important Note
This project is intended for educational purposes only. It serves as a demonstration of social engineering techniques and should not be used for malicious activities. Always ensure you have proper authorization before testing any security vulnerabilities.

## Contributing
Contributions are welcome! If you have suggestions for improvements or want to report issues, please create an issue or submit a pull request.

## Acknowledgments
Special thanks to John Hammond for the inspiration and valuable insights into cybersecurity practices.
