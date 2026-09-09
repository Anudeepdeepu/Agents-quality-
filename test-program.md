1. IMPORT FUNCTION
────────────────────

from dotenv import load_dotenv

"Give me load_dotenv()"


              ↓


2. IMPORT OS MODULE
────────────────────

import os

"Give me environment-variable functionality"


              ↓


3. LOAD .ENV
────────────────────

load_dotenv()

.env
 ↓
GOOGLE_CLOUD_PROJECT=gen-lang-client-0992796703


              ↓


4. GET PROJECT ID
────────────────────

project = os.getenv("GOOGLE_CLOUD_PROJECT")

              ↓

project = "gen-lang-client-0992796703"


              ↓


5. CREATE GEMINI OBJECT
────────────────────────

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    vertexai=True,
    project=project
)


              ↓


6. RESULT
────────────────────

llm
 ↓
Gemini LLM object configured to use
Vertex AI + your Google Cloud project