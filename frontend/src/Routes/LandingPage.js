import React from 'react'
import Auth from './Auth';
import Screens from './Screens';

const LandingPage = ({ userType, isLoggedIn }) => {
    return (
        <>
            {isLoggedIn === true ? <Screens userType={userType} /> : <Auth />}
        </>
    )
}

export default LandingPage