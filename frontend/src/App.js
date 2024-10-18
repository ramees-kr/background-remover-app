import React, { useState } from "react";
import axios from "axios";

function App() {
  const [originalImage, setOriginalImage] = useState(null);
  const [processedImage, setProcessedImage] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleImageChange = (event) => {
    setOriginalImage(URL.createObjectURL(event.target.files[0]));
  };

  const removeBackground = async () => {
    setLoading(true);
    const formData = new FormData();
    formData.append("image", document.querySelector("#imageInput").files[0]);

    try {
      const response = await axios.post("/remove_background", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });
      setProcessedImage(response.data.processed_image_url);
    } catch (error) {
      console.error("Error removing background:", error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <input type="file" id="imageInput" onChange={handleImageChange} />
      {originalImage && <img src={originalImage} alt="Original" />}
      <button onClick={removeBackground} disabled={loading}>
        {loading ? "Removing..." : "Remove Background"}
      </button>
      {processedImage && <img src={processedImage} alt="Processed" />}
    </div>
  );
}

export default App;
