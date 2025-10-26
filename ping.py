from fastapi import FastAPI
import uvicorn

app = FastAPI(title='Ping')

@app.get('/ping')
def ping():
    return 'PONG'

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=9696)

# use curl http://127.0.0.1:9696/ping
# or curl http://localhost:9696/ping
# 0.0.0.0 does not resolve on my PC correctly for some reason...

