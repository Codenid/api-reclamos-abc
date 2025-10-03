FROM python:3.11-alpine

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir --no-deps -r requirements.txt

COPY ./src ./src

EXPOSE 8001

CMD ["uvicorn", "src.api_reclamos.main:app", "--host", "0.0.0.0", "--port", "8001"]