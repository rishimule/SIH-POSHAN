import React from 'react'
import NotificationsIcon from '@mui/icons-material/Notifications';
import Avatar from '@mui/material/Avatar';
import Badge from '@mui/material/Badge';
import MobileNav from '../MobileNav/MobileNav';

import './Navbar.css'

const Navbar = ({ user, NavRoutes }) => {
    return (
        <nav>
            <div className="d-flex align-items-center">
                <MobileNav user={user} NavRoutes={NavRoutes} />
                <Badge color="error" badgeContent={`${user.notifications}`} >
                    <NotificationsIcon sx={{ color: "#a9a9a9", cursor: "pointer" }} />
                </Badge>
                <div className="divider"></div>
                <div className="user-info d-flex align-items-center justify-content-between">
                    <p className='me-2'>{user.name}</p>
                    <Avatar alt="Remy Sharp" src="/static/images/avatar/1.jpg" style={{ width: "30px", height: "30px" }} />
                </div>
            </div>
        </nav>
    )
}

export default Navbar