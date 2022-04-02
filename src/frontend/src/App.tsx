import LeftMenu from "./components/LeftMenu";
import Uploader from "./components/Uploader";

function App() {
  return (
    <div className="w-100 h-[100vh] flex items-center justify-center bg-background">
      <div className="bg-white p-5 rounded-xl gap-3 flex">
        <LeftMenu />
        <Uploader onUploadComplete={() => {}} />
      </div>
    </div>
  );
}

export default App;
