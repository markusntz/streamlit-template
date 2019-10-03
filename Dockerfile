FROM python:3.7.4-stretch

RUN mkdir -p /root/.streamlit
RUN bash -c 'echo -e "\
[general]\n\
email = \"your-email@domain.com\"\n\
" > /root/.streamlit/credentials.toml'

WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501
CMD ["streamlit", "run", "src/app.py"]