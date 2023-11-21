steps to run: 
1. (optional) create python venv: mkdir env-yi python -m venv env-yi source ./env-yi/bin/activate

2. install required packages:
`pip install -r requirements.txt`

3. set flask envs and run:
`export FLASK_APP=app.py` &
`flask run`


to query it, for example with curl:
`curl -X POST http://127.0.0.1:5000/generate-text -H "Content-Type: application/json" -d '{"text":"Your input text here"}'`
