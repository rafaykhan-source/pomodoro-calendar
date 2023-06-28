// import { useState } from 'react'
import '../App.css'
import { Button } from '@material-tailwind/react';

function SettingsButton() {
  // const [count, setCount] = useState(0)

  return (
    <>
      <Button className="bg-[#ee4e22] hover:bg-[#8f2d12] font-semibold py-2 px-4 rounded">Settings</Button>
    </>
  )
}

export default SettingsButton
