run:
    @uvicorn workout_api.main:app --reload
creat-migration:
   @PYTHONPATH=$PYTHONPATH:$(pwd) alembic revision -- autogenerate -m $(d)

run-migration:
   @PYTHONPATH=$PYTHONPATH:$(pwd) alembic upgrade head