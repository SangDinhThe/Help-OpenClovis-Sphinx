#build docs

FROM python:3.11-slim AS builder

WORKDIR /docs

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN apt update && apt install -y make

COPY . .
RUN make html

#Install nginx server

FROM nginx:alpine

COPY --from=builder /docs/_build/html /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
