from google import genai
from google.genai.errors import ClientError
from app.config import settings
import time

client = genai.Client(api_key=settings.GEMINI_API_KEY)


def ask_gemini(prompt: str):

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )

        return response.text

    except ClientError as e:

        error_code = getattr(e, "code", None)

        # Quota exceeded
        if error_code == 429:
            print("⚠️ Gemini quota exceeded:", e)
            time.sleep(5)
            return "⚠️ Gemini API quota exceeded. Please try again after a few seconds."

        # Invalid API key
        elif error_code == 401:
            print("❌ Invalid API key:", e)
            return "Invalid Gemini API key. Check your .env file."

        # Model not found
        elif error_code == 404:
            print("❌ Model not found:", e)
            return "Gemini model not available."

        else:
            print("Gemini client error:", e)
            return "Gemini API error occurred."

    except Exception as e:
        print("Unexpected Gemini error:", e)
        return "Unexpected error while calling Gemini."



# "  cohere "


# import cohere
# import time
# from app.config import settings

# co = cohere.Client(settings.COHERE_API_KEY)


# def ask_llm(prompt: str):

#     try:

#         response = co.chat(
#             model="command-a",
#             message=prompt,
#             temperature=0
#         )

#         return response.text.strip()

#     except cohere.errors.TooManyRequestsError:
#         print("⚠️ Cohere rate limit exceeded")
#         return "⚠️ Cohere API rate limit exceeded"

#     except cohere.errors.UnauthorizedError:
#         print("⚠️ Invalid Cohere API key")
#         return "⚠️ Cohere API key invalid"

#     except Exception as e:
#         print("⚠️ LLM error:", e)
#         time.sleep(2)
#         return "⚠️ LLM request failed"