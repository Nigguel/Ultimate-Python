"""     Variables de entorno     """

import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.getenv("SENDGRID_API_KEY")
print(apikey)
