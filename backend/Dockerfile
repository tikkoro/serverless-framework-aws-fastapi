FROM public.ecr.aws/lambda/python:3.9
COPY ./backend/requirements.txt ./
COPY ./backend/main.py ./
RUN pip install --no-cache-dir -r requirements.txt
ENV STAGE=
ENTRYPOINT ["/bin/bash", "-l", "-c"]
CMD ["uvicorn main:app --reload --host 0.0.0.0 --port 8001"]
