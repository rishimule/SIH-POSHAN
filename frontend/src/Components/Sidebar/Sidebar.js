import React, { useEffect, useState } from 'react'
import './Sidebar.css'
import { NavLink } from 'react-router-dom'

const Sidebar = ({ NavRoutes, user, setOpen }) => {
    const closeMob = () => {
        if (window.innerWidth < 768) {
            setOpen(false)
        } else {
            return
        }
    }

    return (
        <div className='sidebar container-fluid col-md-3 col-lg-2 m-0 p-0 overflow-auto'>
            <div className='sidebar-header d-flex align-items-center p-4'>
                <i className={user.icon}></i>
                <h3 className='ms-3' style={{ textTransform: "uppercase" }}>{user.type}</h3>
            </div>
            <div className='sidebar-body'>
                <ul>
                    {NavRoutes.map((e, index) => {
                        return (
                            <NavLink activeClassName="active" to={e.path} key={index} onClick={closeMob}>
                                <li>{e.title}</li>
                            </NavLink>
                        )
                    })}
                </ul>
            </div>
        </div>
    )
}

export default Sidebar