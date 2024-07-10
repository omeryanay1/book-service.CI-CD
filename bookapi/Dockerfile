FROM python:3.12.2-slim as base
WORKDIR ./app
COPY ../requirements.txt .
COPY main.py .
COPY BooksCollection.py .
COPY RatingsCollection.py .
RUN --mount=type=cache,target=/root/.cache/pip \
    python -m pip install -r requirements.txt
EXPOSE 5001 
CMD ["python3", "main.py"]
