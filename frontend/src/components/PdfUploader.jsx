import { uploadPDF } from "../services/api";

export default function PdfUploader({ uploadedFile, setUploadedFile }) {
  const handleUpload = async (e) => {
    const file = e.target.files[0];
    if (!file) return;

    try {
      const result = await uploadPDF(file);
      setUploadedFile(file);
      alert(result.message);
    } catch (error) {
      alert("Failed to upload PDF");
      console.error(error);
    }
  };

  const removeFile = () => {
    setUploadedFile(null);
  };

  return (
    <div className="uploader">
      {!uploadedFile ? (
        <>
          <label htmlFor="pdf-upload" className="upload-label">
            📄 Upload PDF
          </label>
          <input
            id="pdf-upload"
            type="file"
            accept=".pdf"
            onChange={handleUpload}
            className="upload-input"
          />
        </>
      ) : (
        <div className="uploaded-file">
          <span>📄 {uploadedFile.name}</span>
          <button onClick={removeFile}>❌</button>
        </div>
      )}
    </div>
  );
}
