import React from 'react'
import './ForgotPassword.css'
import { useState } from 'react'
import ForgotPassEmail from '../../../Components/Password/Forgot_Password/ForgotPassEmail'
import EnterForgotPass from '../../../Components/Password/Forgot_Password/EnterForgotPass'

const ForgotPassword = () => {
    const [currPage, setCurrPage] = useState(1)
    return (
        <>
            {currPage === 2 ? <EnterForgotPass /> : <ForgotPassEmail setCurrPage={setCurrPage} />}
        </>
    )
}

export default ForgotPassword