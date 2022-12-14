FROM public.ecr.aws/lambda/python:3.9
COPY ./backend/requirements.txt ./
COPY ./backend/app.py ./
RUN pip install --no-cache-dir -r requirements.txt
ENV STAGE=
ENTRYPOINT ["/bin/bash", "-l", "-c"]
CMD ["uvicorn app:app --reload --host 0.0.0.0 --port 8001"]
