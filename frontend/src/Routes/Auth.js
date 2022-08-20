import React from 'react'
import { Routes, Route, Navigate } from 'react-router-dom'
import Login from '../Auth/Screens/Login/Login'
import ForgotPasswaord from '../Auth/Screens/Password/Forgot_Password/ForgotPassword'
import ChangePassword from '../Auth/Screens/Password/Change_Password/ChangePassword'

const Auth = () => {
    return (
        <>
            <Routes>
                <Route index path="/" element={<Login />} />
                <Route path="/forgot_password" element={<ForgotPasswaord />} />
                <Route path="/change_password" element={<ChangePassword />} />
                <Route path="*" element={<Navigate to='/' />} />
            </Routes>
        </>
    )
}

export default Auth