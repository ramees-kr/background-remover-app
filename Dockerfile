FROM python:3.9

COPY u2net.onnx /home/.u2net/u2net.onnx

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