import React from 'react'
import FileDownloadIcon from '@mui/icons-material/FileDownload';
import './Dashboard.css'
import Divider from '@mui/material/Divider';


const Dashboard = () => {

    const infoCard = [
        {
            title: 'Meals Served (Monthly)',
            value: '9,856',
        },
        {
            title: 'Meals Served (Weekly)',
            value: '2,150',
        },
        {
            title: 'Today\'s Attendance',
            value: '46%',
        },
        {
            title: 'Average Daily Meal\'s Served',
            value: '309',
        },
    ]

    return (
        <div className="dashboard">
            <div className="page-header d-flex justify-content-between my-5 align-items-center">
                <div className='d-none d-md-block'></div>
                <h3 className='text-center text-uppercase'>Dashboard</h3>
                <button className='report-btn'><FileDownloadIcon style={{ width: "18px" }} /> Generate Report</button>
            </div>
            <div className="info-cards my-4">
                <div className="row">
                    {infoCard.map((card, index) => {
                        return (
                            <div className="col-md-6 col-lg-3 my-3 my-lg-0 px-lg-4" key={index}>
                                <div className="info-card">
                                    <p className='card-title text-center'>{card.title}</p>
                                    <p className='fw-600 text-center mt-1 data'>{card.value}</p>
                                </div>
                            </div>
                        )
                    })}
                </div>
            </div>
            <div className="container-fluid my-5 mean-cal">
                <h4 className='px-3'>Mean Calories</h4>
                <Divider className='my-2' style={{ borderColor: "rgb(0 0 0 / 35%)", borderBottomWidth: "3px", borderRadius: "5px" }} />
            </div>
            <div className="container-fluid d-flex align-items-center justify-content-center pb-5">
                <div className="container-fluid bmi">
                    <h4 className='px-3'>BMI</h4>
                    <Divider className='my-2' style={{ borderColor: "rgb(0 0 0 / 35%)", borderBottomWidth: "3px", borderRadius: "5px" }} />
                </div>
            </div>
        </div>
    )
}

export default Dashboard