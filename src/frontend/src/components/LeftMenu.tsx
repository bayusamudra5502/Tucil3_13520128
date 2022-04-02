import { FormEvent, useContext, useState } from "react";
import ServerContext from "../context/ServerContext";
import logo from "../img/logo.png";
import { AiOutlineClose } from "react-icons/ai";

export default function LeftMenu() {
  const { server, setServer } = useContext(ServerContext)!;
  const [serverValue, setServerValue] = useState("");

  function changeServer(e: FormEvent) {
    e.preventDefault();
    setServer(serverValue);
  }

  function resetServer() {
    setServer("");
  }

  return (
    <div className="max-w-xs p-2 flex flex-col justify-center items-center">
      <img src={logo} alt="Logo 15-Puzzle Solver" className="w-[50%] mb-9" />
      <h1 className="text-4xl mb-2">15-Puzzle Solver</h1>
      <p className="text-lg mb-4">Sang penakluk 15-puzzle</p>
      <div className="w-[100%]">
        <h2 className="font-bold mb-2">Server</h2>
        {!server ? (
          <form className="flex flex-col" onSubmit={changeServer}>
            <input
              type="url"
              className="mb-3 py-2 px-2.5 border-2 rounded-lg border-slate-300"
              placeholder="http://localhost"
              value={serverValue}
              onChange={(e) => setServerValue(e.target.value)}
            ></input>
            <button className="bg-blue-theme text-white rounded-lg py-2 px-3">
              Submit
            </button>
          </form>
        ) : (
          <div className="flex items-center">
            <p>{server}</p>
            <AiOutlineClose
              className="font-bold ml-1 cursor-pointer"
              onClick={resetServer}
            />
          </div>
        )}
      </div>
    </div>
  );
}
