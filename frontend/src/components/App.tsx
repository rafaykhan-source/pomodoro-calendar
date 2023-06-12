import React from 'react'
import Nav from './nav'
import NoteCardList from './NoteCardList'
import TaskCardList from './TaskCardList'

function App() {
  return (
    <div>
      <div className="justify flex">
        <Nav />
      </div>
      <div className="flex">
        <NoteCardList />
      </div>
      <div className="flex">
        <TaskCardList />
      </div>
    </div>
  )
}

export default App
