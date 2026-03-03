#!/bin/bash
# ================================================================
# Environment Setup — German Weather ML Pipeline
# ================================================================

echo "Setting up Python environment..."

# Check Python version
python3 --version || { echo "Python 3 is required"; exit 1; }

# Check if conda is available
if command -v conda &> /dev/null; then
    echo "Conda detected. Creating environment from environment.yml..."
    conda env create -f ../environment.yml
    echo ""
    echo "Activate with: conda activate german-weather-ml"
else
    echo "Conda not found. Using pip..."
    pip install --upgrade pip
    pip install \
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
fi

# Verify PySpark installation
echo ""
echo "Verifying installation..."
python3 -c "import pyspark; print(f'PySpark {pyspark.__version__} - OK')"
python3 -c "import sklearn; print(f'scikit-learn {sklearn.__version__} - OK')"
python3 -c "import pandas; print(f'pandas {pandas.__version__} - OK')"
python3 -c "import pyarrow; print(f'pyarrow {pyarrow.__version__} - OK')"

echo ""
echo "Setup complete!"
echo ""
