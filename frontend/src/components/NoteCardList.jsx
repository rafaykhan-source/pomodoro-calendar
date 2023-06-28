import NoteCard from "./NoteCard";
  
function NoteCardList() {
return (
    <>
    <div className="flex h-80 max-w-[1380px] mx-auto px-4 text-white">
      <ul>
        <li><NoteCard /></li>
      </ul>
    </div>
    </>
);
}

export default NoteCardList