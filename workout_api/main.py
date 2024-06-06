from fastapi import FastAPI
app = FastAPI(title='WorkoutApi')

if __name__ =='main':
    import uvicorn
    
    uvicorn.run('main:app', host=