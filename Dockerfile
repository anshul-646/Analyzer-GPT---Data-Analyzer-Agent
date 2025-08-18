# Use lightweight Python base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install required Python packages
RUN pip install --no-cache-dir pandas matplotlib streamlit seaborn scikit-learn

# Default command
CMD ["bash"]
