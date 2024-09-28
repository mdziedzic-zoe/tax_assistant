import os
from openai import OpenAI
from dotenv import load_dotenv
import logging
import time

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Assistant ID
ASSISTANT_ID = "asst_otiQS4sGkxLPSHIYkhEmCnwC"

def analyze_document_with_gpt4(file_path, prompt):
    try:
        # Upload the file
        with open(file_path, "rb") as file:
            file_response = client.files.create(file=file, purpose="assistants")
        file_id = file_response.id
        logger.info(f"File uploaded successfully. File ID: {file_id}")

        # Create a thread
        thread = client.beta.threads.create()
        logger.info(f"Thread created. Thread ID: {thread.id}")

        # Add a message to the thread with attachments
        client.beta.threads.messages.create(
            thread_id=thread.id,
            role="user",
            content=prompt,
            attachments=[
                { "file_id": file_id, "tools": [{"type": "file_search"}] }
            ]
        )
        
        # Run the assistant
        run = client.beta.threads.runs.create(
            thread_id=thread.id,
            assistant_id=ASSISTANT_ID,
            instructions=f"Analyze the uploaded file (File ID: {file_id}) and respond to: {prompt}"
        )
        logger.info(f"Run created. Run ID: {run.id}")

        # Wait for the run to complete
        while True:
            run_status = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
            logger.info(f"Run status: {run_status.status}")
            if run_status.status == 'completed':
                break
            elif run_status.status == 'failed':
                logger.error(f"Run failed: {run_status.last_error}")
                return None
            time.sleep(5)  # Wait for 5 seconds before checking again

        # Retrieve the messages
        messages = client.beta.threads.messages.list(thread_id=thread.id)
        logger.info(f"Retrieved {len(messages.data)} messages from the thread")

        # Get the latest assistant message
        for message in reversed(messages.data):
            if message.role == "assistant":
                response = message.content[0].text.value
                logger.info("Assistant response received")
                return response

        logger.warning("No assistant response found in the messages")
        return None

    except Exception as e:
        logger.error(f"Error analyzing document with GPT-4: {e}", exc_info=True)
        return None

def process_document(document_path, prompt):
    try:
        response = analyze_document_with_gpt4(document_path, prompt)
        
        if response:
            logger.info("GPT-4 Analysis:")
            logger.info(response)
        else:
            logger.error("Failed to get analysis from GPT-4")
        
        return response
    except FileNotFoundError:
        logger.error(f"Error: File not found at {document_path}")
    except Exception as e:
        logger.error(f"Error processing document: {e}")

if __name__ == "__main__":
    # Example usage for testing
    document_path = "umowa.pdf"
    prompt = "Analyze this document and provide a summary of its key points."
    process_document(document_path, prompt)
