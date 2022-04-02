import React, { useMemo } from "react";
import { useDropzone } from "react-dropzone";
import { FiInbox, FiAlertOctagon, FiArrowDown } from "react-icons/fi";

export interface IMoves {
  moves: ("RIGHT" | "UP" | "LEFT" | "DOWN")[];
  moveTables: number[];
}

export interface IResponse {
  status: "success";
  input: number[];
  node: number;
  time: number;
  result: IMoves[];
}

export default function Uploader({
  onUploadComplete,
}: {
  onUploadComplete: (data: IResponse) => void;
}) {
  function onDropAccepted() {
    // ...
  }

  const { getRootProps, getInputProps, isDragActive, isDragReject } =
    useDropzone({
      onDropAccepted,
      accept: "text/plain",
      maxFiles: 1,
    });

  const elements = useMemo(() => {
    if (isDragReject) {
      return (
        <div className="text-red-500 flex justify-center items-center flex-col">
          <FiAlertOctagon className="text-3xl mb-2" />
          <p className="text-xl">Format file tidak diizinkan</p>
          <p>
            Format yang diizinkan hanyalah file <code>text/plain</code>
          </p>
        </div>
      );
    } else if (isDragActive) {
      return (
        <div className="text-green-200 flex justify-center items-center flex-col">
          <FiArrowDown className="text-3xl mb-2" />
          <p className="text-xl">Lepas file disini</p>
        </div>
      );
    } else {
      return (
        <div className="text-slate-400 flex justify-center items-center flex-col">
          <FiInbox className="text-3xl mb-2" />
          <p className="text-xl font-bold">Letakan file disini...</p>
          <p>atau boleh juga klik untuk memilih file</p>
        </div>
      );
    }
  }, [isDragActive, isDragReject]);

  const className =
    "flex items-center justify-center border-4 border-slate-300 p-5 rounded-3xl border-dashed";
  return (
    <div {...getRootProps({ className })}>
      <input {...getInputProps()} />
      {elements}
    </div>
  );
}
