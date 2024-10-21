# Background Remover App

This is a simple web application that allows you to remove the background from images using the `rembg` library in Python. It's built with Flask and deployed using Docker and GitHub Actions for continuous integration and deployment (CI/CD).

## Features

- **Background removal:** Removes the background from uploaded images.
- **Drag and drop:** Supports drag-and-drop file uploads for a convenient user experience.
- **Image preview:** Displays the original and processed images side-by-side.
- **Download:** Allows users to download the processed image.
- **Responsive design:** Adapts to different screen sizes for optimal viewing on various devices.

## Technologies Used

- **Flask:** Python web framework for building the application.
- **`rembg`:** Python library for removing image backgrounds.
- **Pillow:** Python Imaging Library for image processing.
- **Docker:** Containerization technology for packaging the application and its dependencies.
- **GitHub Actions:** CI/CD platform for automating the build and deployment process.
- **Cloudflare Pages:** Serverless platform for deploying the application.

## How to Run Locally

1.  **Clone the repository:**

    ```bash
    git clone [invalid URL removed]
    cd background-remover-app
    ```

2.  **Create and activate a virtual environment:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Flask app:**

    ```bash
    flask run
    ```

    The application will be accessible at `http://127.0.0.1:5000/`.

## GitHub Actions Workflow

This project uses GitHub Actions to automate the build and deployment process. The workflow file `.github/workflows/main.yml` defines the following steps:

1.  **Checkout code:** Checks out the code from the repository.
2.  **Build Docker image:** Builds the Docker image using the `Dockerfile`.
3.  **Deploy to Cloudflare Pages:** Deploys the image to Cloudflare Pages using the `cloudflare/pages-action@1` action.

The workflow is triggered on every push to the `main` branch.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [rembg library](https://github.com/danielgatis/rembg)
- [Flask](https://flask.palletsprojects.com/en/2.2.x/)
- [Pillow](https://python-pillow.org/)
- [Docker](https://www.docker.com/)
- [GitHub Actions](https://github.com/features/actions)
- [Cloudflare Pages](https://pages.cloudflare.com/)
