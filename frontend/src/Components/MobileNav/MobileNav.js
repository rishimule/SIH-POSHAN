import React, { useState } from 'react'
import Sidebar from '../Sidebar/Sidebar'
import './MobileNav.css'

const MobileNav = ({ user, NavRoutes }) => {
    const [open, setOpen] = useState(false)

    const toggleMenu = () => {
        setOpen(!open)
    }

    return (
        <div className='mob-nav d-block d-md-none'>
            <i className="fa-solid fa-bars" onClick={toggleMenu}></i>
            <div className={`menu ${open ? "active" : ""}`}>
                <div className="close-box" onClick={toggleMenu}>
                    <i className="fa-solid fa-xmark" id='menuClose-btn' ></i>
                </div>
                <Sidebar NavRoutes={NavRoutes} user={user} setOpen={setOpen} />
            </div>
        </div>
    )
}

export default MobileNav