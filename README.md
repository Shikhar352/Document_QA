
Document Question-Answering Application
This project is a Gradio-based web application that answers questions based on the content of a provided document. Using a fine-tuned Hugging Face roberta-base-squad2 model, the application extracts relevant answers from the uploaded document.

Features
Upload a .txt file containing text data.
Ask questions based on the content of the uploaded document.
Get precise answers using a pre-trained Question-Answering model.
Requirements
To run this application, you need to install the following dependencies:

torch
gradio
transformers
You can install them using the command:

bash
Copy code
pip install torch gradio transformers
How to Use
Clone this repository or copy the code file to your local machine.
Set up the model path: Ensure the model path points to a valid roberta-base-squad2 model checkpoint. Update the model_path variable in the script as needed.
Run the application: Execute the Python script:
bash
Copy code
python app.py
Open the Gradio Interface: The interface will launch in your default web browser or display a shareable link in the terminal.
Application Interface
The interface consists of:

File Upload: Upload a .txt file containing the context.
Question Input: Enter your question in the provided textbox.
Answer Display: The application will return the answer based on the file content.
Example Workflow
Upload a .txt file containing the following text:
kotlin
Copy code
Gradio is an open-source Python library that is used to create customizable UI components for machine learning models.
Enter the question:
csharp
Copy code
What is Gradio?
The output will be:
kotlin
Copy code
an open-source Python library that is used to create customizable UI components for machine learning models.
Troubleshooting
Ensure the uploaded file is in .txt format.
Check that the model path (model_path) points to the correct local checkpoint of the Hugging Face model.
License
This project is open-source and available under the MIT License.

Acknowledgments
Hugging Face for providing pre-trained models and the transformers library.
Gradio for the easy-to-use UI development tools.
