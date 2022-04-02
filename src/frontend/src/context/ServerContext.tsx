import React from "react";
import { createContext, useContext, useState } from "react";

interface IServerMetadata {
  server: string;
  setServer: (params: string) => void;
}

const ServerContext = createContext<null | IServerMetadata>(null);

export function ServerProvider({ children }: { children: React.ReactNode }) {
  const [server, setServer] = useState<string>("");

  return (
    <ServerContext.Provider value={{ server, setServer }}>
      {children}
    </ServerContext.Provider>
  );
}

export default ServerContext;
