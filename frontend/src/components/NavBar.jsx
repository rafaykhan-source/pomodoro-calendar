// import { useState } from 'react'
import { AiFillGithub } from "react-icons/ai"
import SettingsButton from "./SettingsButton"
import '../App.css'

function NavBar() {
  // const [count, setCount] = useState(0)

  return (
    <>
      <div className='flex justify-between items-center h-20 max-w-[1240px] mx-auto px-4 text-white'>
        <h1 className='w-full text-3xl font-semibold text-[#ee4e22]'><a href="http://localhost:5173/">PomoCal</a></h1>
        <ul className='flex'>
            <li className='p-4 text-4xl'><a href="https://github.com/rafaykhan-source/pomodoro-calendar"><AiFillGithub /></a></li>
            <li className='p-4'><SettingsButton /></li>
        </ul>
      </div>
    </>
  )
}

export default NavBar
