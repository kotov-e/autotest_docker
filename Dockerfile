FROM python
COPY requirements.txt .
COPY main.py .
RUN pip install --no-cache -r requirements.txt
RUN playwright install --with-deps chromium
RUN mkdir allure-results
CMD ["pytest", "main.py", "--alluredir=allure-results"]