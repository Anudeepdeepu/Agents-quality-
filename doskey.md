renaming the corrupt file 


Then recreate the configuration:

gcloud init

And verify:

gcloud config list

Expected structure:

[core]
account = your-email@gmail.com
project = your-project-id

Your active configuration is: [default]

ren C:\Users\Admin\AppData\Roaming\gcloud\configurations\config_default config_default_backup


(anu-agents) f:\agents\anu-agents>doskey/history
cd ..\..\
f:
cd f:\..\agents\
pwd
.venv\scripts\activate
code .
cd .\anu-agents
.venv\scripts\activate
uv add langchain-core langchain langchain-google-genai
uv add python-dotenv
gcloud auth application-default set-quota-project gen-lang-client-0992796703
ren C:\Users\Admin\AppData\Roaming\gcloud\configurations\config_default config_default_backup
gcloud init
gcloud config list
uv run test.py
gcloud auth application-default set-quota-project gen-lang-client-0992796703
uv run test.py
git init
echo .env>>.gitignore
echo .venv/>>.gitignore
doskey/history