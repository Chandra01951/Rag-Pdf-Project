import { useState } from "react";
import PdfUploader from "../components/PdfUploader";
import ChatWindow from "../components/ChatWindow";

export default function Home() {
  const [uploadedFile, setUploadedFile] = useState(null);

  return (
    <div className="home">
      <h2 className="title">Upload a PDF and ask questions about it</h2>

      <PdfUploader
        uploadedFile={uploadedFile}
        setUploadedFile={setUploadedFile}
      />

      <ChatWindow uploadedFile={uploadedFile} />
    </div>
  );
}
