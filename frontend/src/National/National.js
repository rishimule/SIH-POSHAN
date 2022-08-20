import React from 'react'
import { Routes, Route, Navigate } from 'react-router-dom'
import Dashboard from './Screens/Dashboard/Dashboard'
import Profile from './Screens/Profile/Profile'
import Attendance from './Screens/Attendance/Attendance'
import Details from './Screens/Details/Details'
import Meal from './Screens/Meal/Meal'
import StudentRegister from './Screens/StudentRegister/StudentRegister'
import Sidebar from '../Components/Sidebar/Sidebar'
import Navbar from '../Components/Navbar/Navbar'


const National = () => {
    const user = {
        type: "national",
        icon: "fa-brands fa-fort-awesome",
        name: "User Name",
        notifications: 10
    }

    const NavRoutes = [
        {
            title: "Dashboard",
            path: "/dashboard"
        },
        {
            title: "Profile",
            path: "/profile"
        },
        {
            title: "Today's Meal",
            path: "/meal"
        },
        {
            title: "Attendance",
            path: "/attendance"
        },
        {
            title: "Student Details",
            path: "/student_datails"
        },
        {
            title: "regiter students",
            path: "/regiter_students"
        },
    ]
    return (
        <div className=" District container-fluid p-0">
            <div className="row m-0 p-0">
                <div className="col-md-3 col-lg-2 p-0 d-none d-md-block">
                    <Sidebar NavRoutes={NavRoutes} user={user} />
                    <div className="psudo-block" style={{ height: "100vh" }}></div>
                </div>
                <div className="col-md-9 col-lg-10 py-2 px-4">
                    <Navbar user={user} NavRoutes={NavRoutes} />
                    <div>
                        <Routes>
                            <Route path='/' element={<Navigate to="/dashboard" />} />
                            <Route path='/dashboard' element={<Dashboard />} />
                            <Route path='/profile' element={<Profile />} />
                            <Route path='/meal' element={<Meal />} />
                            <Route path='/attendance' element={<Attendance />} />
                            <Route path='/student_datails' element={<Details />} />
                            <Route path='/regiter_students' element={<StudentRegister />} />
                            <Route path='*' element={<Navigate to="/dashboard" />} />
                        </Routes>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default National