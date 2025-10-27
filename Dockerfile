# Created new dockerfile for homework week 5 specifically
# Question 6 - it should start like that:

FROM agrigorev/zoomcamp-model:2025

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /code

ENV PATH="/code/.venv/bin:$PATH"

# Install all the dependencies from pyproject.toml
COPY "pyproject.toml" "uv.lock" ".python-version" ./

# Actually install dependencies 
RUN uv sync 

# Copy your FastAPI script
# Run it with uvicorn
# After that, you can build your docker image.

# Copy application code and model data into the container
COPY "predict_hw5.py" "pipeline_v1.bin" ./

# Expose TCP port 9696 so it can be accessed from outside the container
EXPOSE 9696
# Run the application using uvicorn (ASGI server)
# predict_hw5:app → refers to 'app' object inside predict_hw5.py
# --host 0.0.0.0 → listen on all interfaces
# --port 9696    → listen on port 9696
ENTRYPOINT ["uvicorn", "predict_hw5:app", "--host", "0.0.0.0", "--port", "9696"]

# Build it:

# docker build -t predict-convert .

# And run it:

# docker run -it --rm -p 9696:9696 predict-convert

