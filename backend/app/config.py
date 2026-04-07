import os
from dotenv import load_dotenv

load_dotenv()

class Settings:

    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

    POSTGRES_HOST = os.getenv("POSTGRES_HOST")
    POSTGRES_PORT = os.getenv("POSTGRES_PORT")
    POSTGRES_DB = os.getenv("POSTGRES_DB")
    POSTGRES_USER = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")

    NEO4J_URI = os.getenv("NEO4J_URI")
    NEO4J_USER = os.getenv("NEO4J_USER")
    NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")

settings = Settings()



# " cohere "



# import os
# from dotenv import load_dotenv

# load_dotenv()


# class Settings:

#     COHERE_API_KEY = os.getenv("COHERE_API_KEY")

#     POSTGRES_HOST = os.getenv("POSTGRES_HOST")
#     POSTGRES_PORT = os.getenv("POSTGRES_PORT")
#     POSTGRES_DB = os.getenv("POSTGRES_DB")
#     POSTGRES_USER = os.getenv("POSTGRES_USER")
#     POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")

#     NEO4J_URI = os.getenv("NEO4J_URI")
#     NEO4J_USER = os.getenv("NEO4J_USER")
#     NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")


# settings = Settings()