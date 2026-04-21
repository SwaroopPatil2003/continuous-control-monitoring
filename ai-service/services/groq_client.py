import os
import time
import logging
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class GroqClient:
    def __init__(self):
        api_key = os.getenv("GROQ_API_KEY")

        if not api_key:
            raise ValueError("GROQ_API_KEY not found in .env")

        self.client = Groq(api_key=api_key)
        self.model = "llama-3.3-70b-versatile"

    def generate_text(self, prompt):
        retries = 3
        delay = 2

        for attempt in range(1, retries + 1):
            try:
                logging.info(f"Attempt {attempt}: Sending request to Groq")

                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=[
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.5,
                    max_tokens=300
                )

                result = response.choices[0].message.content.strip()

                logging.info("Response received successfully")
                return result

            except Exception as error:
                logging.error(f"Attempt {attempt} failed: {error}")

                if attempt < retries:
                    logging.info(f"Retrying in {delay} seconds...")
                    time.sleep(delay)
                    delay *= 2
                else:
                    return "Error: Unable to get response from Groq after 3 attempts"