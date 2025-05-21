import React, { useState } from 'react';
import axios from 'axios';

function FileUpload() {
  const [file, setFile] = useState(null);

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleUpload = async () => {
    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await axios.post('http://backend:8000/api/upload', formData, {
      headers: { 'Content-Type': 'multipart/form-data' },
    });
    alert('File uploaded successfully!');
    console.log(response.data);
  } catch (error) {
    alert('Error uploading file.');
    console.error(error);
  }
};

  return (
    <div>
      <input type="file" onChange={handleFileChange} />
      <button onClick={handleUpload}>Upload</button>
    </div>
  );
}

export default FileUpload;
