const dropArea = document.getElementById("drop-area");
const inputFile = document.getElementById("input-file");
const imageView = document.getElementById("img-view");
const imageViewOutput = document.getElementById("img-view-output");

inputFile.addEventListener("change", uploadImage);

function uploadImage() {
  const formData = new FormData();
  formData.append("file", inputFile.files[0]);

  // Display the uploaded image in the img-view area
  let imgLink = URL.createObjectURL(inputFile.files[0]);
  imageView.style.backgroundImage = `url(${imgLink})`;
  imageView.textContent = "";
  imageView.style.border = "0";

  // Send the image to Flask for background processing
  fetch("/process-image", {
    method: "POST",
    body: formData,
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.processed_image_url) {
        imageView.style.backgroundImage = `url(${data.processed_image_url})`;
        console.log(
          "Inside JS => data.processed_image_url: " +
            `url(${data.processed_image_url})`
        );
      }
    })
    .catch((error) => console.error("Error:", error));
}

dropArea.addEventListener("dragover", (event) => {
  event.preventDefault();
});

dropArea.addEventListener("drop", function (event) {
  event.preventDefault();
  inputFile.files = event.dataTransfer.files;
  uploadImage();
});
