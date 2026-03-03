FROM python:3.9-slim

# Install Java for Spark
RUN apt-get update && \
    apt-get install -y --no-install-recommends openjdk-11-jre-headless curl wget && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
ENV PYSPARK_PYTHON=python3
ENV PYSPARK_DRIVER_PYTHON=python3

WORKDIR /app

# Install Python dependencies
RUN pip install --no-cache-dir \
    pyspark>=3.4 \
    numpy>=1.21 \
    pandas>=1.4 \
    matplotlib>=3.5 \
    seaborn>=0.12 \
    scikit-learn>=1.1 \
    scipy>=1.9 \
    pyarrow>=10.0 \
    findspark \
    jupyter \
    requests \
    beautifulsoup4 \
    tqdm \
    psutil \
    pyyaml \
    pytest \
    joblib

COPY . /app

EXPOSE 8888

CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--allow-root", "--no-browser"]
