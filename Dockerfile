FROM python:3.9

# Install wget for downloading files
RUN apt-get update && apt-get install -y wget

# Set up the necessary directories
RUN mkdir -p /root/.u2net

# Download the u2net.onnx and u2netp.onnx model files
RUN wget -O /root/.u2net/u2net.onnx 'https://github.com/danielgatis/rembg/releases/download/v0.0.0/u2net.onnx'

#COPY u2net.onnx /home/.u2net/u2net.onnx 
#COPY u2netp.onnx /root/.u2net/u2net.onnx

WORKDIR /app

# Copy the requirements file
COPY backend/requirements.txt .

# Create and activate the virtual environment
RUN python3 -m venv venv
ENV PATH="/app/venv/bin:$PATH"

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the backend code
COPY backend/ .

# Expose the backend port
EXPOSE 5000

# Start the Flask app
CMD ["flask", "run", "--host=0.0.0.0"] 