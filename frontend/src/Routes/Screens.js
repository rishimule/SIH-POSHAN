import React from 'react'
import School from '../School/School'
import District from '../District/District'
import Auth from './Auth'
import State from '../State/State'
import National from '../National/National'

const Screens = ({ userType }) => {

    const getScreen = () => {
        switch (userType) {
            case 'school':
                return <School />
            case 'district':
                return <District />
            case 'state':
                return <State />
            case 'national':
                return <National />
            default:
                return <Auth />
        }
    }

    return (
        <>
            {getScreen(userType)}
        </>
    )
}

export default Screens