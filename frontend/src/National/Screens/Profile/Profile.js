import React from 'react'
import './Profile.css'
import AccountCircleOutlinedIcon from '@mui/icons-material/AccountCircleOutlined';
import Divider from '@mui/material/Divider';
import LinearProgress from '@mui/material/LinearProgress';
import TextField from '@mui/material/TextField';

const Profile = () => {
    const summary = {
        Schools_Reported: 80,
        Meals_Taken: 60,
        Schools_NotReported: 40
    }

    const [values, setValues] = React.useState({
        student_name: "",
        user_name: "",
        email: "",
        address1: "",
        address2: "",
        district: "",
        state: "",
        pin: "",
        country: "India",

    });

    const handleChange = (prop) => (event) => {
        setValues({ ...values, [prop]: event.target.value });
    };

    const handleClick = () => {
        console.log(values);
        setValues({ ...values, meal_name: "", image: "", calories: "", protiens: "" })
    };


    return (
        <div className='profile container-fluid p-3'>
            <div className="row">
                <div className="col-md-5 col-lg-3 d-flex flex-column align-items-center ">
                    <div className="container p-4 my-3">
                        <AccountCircleOutlinedIcon sx={{ width: "100%", height: "auto" }} />
                        <button className="green-btn">Change Photo</button>
                    </div>

                    <div className="container-fluid shadow-con my-3 p-4">
                        <h5 className='px-3 w-100'>Schools Report Summary</h5>
                        <Divider className='my-2' style={{ borderColor: "rgb(0 0 0 / 35%)", borderBottomWidth: "3px", borderRadius: "5px" }} />
                        <div className="info my-3">
                            <p>Schools Reported</p>
                            <LinearProgress variant="determinate" value={summary.Attendance} sx={{
                                height: "10px",
                                borderRadius: "5px",
                            }} />
                        </div>
                        <div className="info my-3">
                            <p>Meals Taken</p>
                            <LinearProgress variant="determinate" color='success' value={summary.Meals_Taken} sx={{
                                height: "10px",
                                borderRadius: "5px",
                            }} />
                        </div>
                        <div className="info my-3">
                            <p>Schools Not Reported</p>
                            <LinearProgress variant="determinate" color='secondary' value={summary.Test_Performance} sx={{
                                height: "10px",
                                borderRadius: "5px",
                            }} />
                        </div>
                    </div>


                </div>
                <div className="col-md-7 col-lg-9">
                    <div className="container-fluid shadow-con my-3 p-4 align-items-center">
                        <h5 className='px-3 w-100'>User Settings</h5>
                        <Divider className='my-2' style={{ borderColor: "rgb(0 0 0 / 35%)", borderBottomWidth: "3px", borderRadius: "5px" }} />
                        <div className="row py-3 w-100">
                            <div className="col-md-12">
                                <TextField
                                    disabled
                                    name='user_name'
                                    label="User Name"
                                    value={values.student_name}
                                    onChange={handleChange('student_name')}
                                    size="small"
                                    margin="dense"
                                    fullWidth
                                    color='success'
                                    id="outlined-basic"
                                    variant="outlined"
                                    type="text"
                                    sx={{
                                        '.css-bz6wus-MuiInputBase-root-MuiOutlinedInput-root': {
                                            borderRadius: "15px",
                                        },
                                    }}
                                />
                            </div>
                            <div className="col-md-6 my-2">
                                <TextField
                                    name='user_name'
                                    label="District Name"
                                    value={values.user_name}
                                    onChange={handleChange('user_name')}
                                    size="small"
                                    margin="dense"
                                    fullWidth
                                    color='success'
                                    id="outlined-basic"
                                    variant="outlined"
                                    type="text"
                                    sx={{
                                        '.css-bz6wus-MuiInputBase-root-MuiOutlinedInput-root': {
                                            borderRadius: "15px",
                                        },
                                    }}
                                />
                            </div>
                            <div className="col-md-6 my-2">
                                <TextField
                                    name='email'
                                    label="Email Address"
                                    value={values.email}
                                    onChange={handleChange('email')}
                                    size="small"
                                    margin="dense"
                                    fullWidth
                                    color='success'
                                    id="outlined-basic"
                                    variant="outlined"
                                    type="text"
                                    sx={{
                                        '.css-bz6wus-MuiInputBase-root-MuiOutlinedInput-root': {
                                            borderRadius: "15px",
                                        },
                                    }}
                                />
                            </div>
                        </div>
                        <div className="d-flex align-items-baseline justify-content-center">
                            <button className="green-btn">
                                Save
                            </button>
                        </div>
                    </div>
                    <div className="container-fluid shadow-con my-3 p-4">
                        <h5 className='px-3 w-100'>Contact Settings</h5>
                        <Divider className='my-2' style={{ borderColor: "rgb(0 0 0 / 35%)", borderBottomWidth: "3px", borderRadius: "5px" }} />
                        <div className="row py-3 w-100">
                            <div className="col-md-12">
                                <TextField
                                    name='address1'
                                    label="Address Lane 1"
                                    value={values.address1}
                                    onChange={handleChange('address1')}
                                    size="small"
                                    margin="dense"
                                    fullWidth
                                    color='success'
                                    id="outlined-basic"
                                    variant="outlined"
                                    type="text"
                                    sx={{
                                        '.css-bz6wus-MuiInputBase-root-MuiOutlinedInput-root': {
                                            borderRadius: "15px",
                                        },
                                    }}
                                />
                            </div>
                            <div className="col-md-12 my-2">
                                <TextField
                                    name='address2'
                                    label="Address Lane 2"
                                    value={values.address2}
                                    onChange={handleChange('address2')}
                                    size="small"
                                    margin="dense"
                                    fullWidth
                                    color='success'
                                    id="outlined-basic"
                                    variant="outlined"
                                    type="text"
                                    sx={{
                                        '.css-bz6wus-MuiInputBase-root-MuiOutlinedInput-root': {
                                            borderRadius: "15px",
                                        },
                                    }}
                                />
                            </div>
                            <div className="col-md-4 my-2">
                                <TextField
                                    name='district'
                                    label="District"
                                    value={values.district}
                                    onChange={handleChange('district')}
                                    size="small"
                                    margin="dense"
                                    fullWidth
                                    color='success'
                                    id="outlined-basic"
                                    variant="outlined"
                                    type="text"
                                    sx={{
                                        '.css-bz6wus-MuiInputBase-root-MuiOutlinedInput-root': {
                                            borderRadius: "15px",
                                        },
                                    }}
                                />
                            </div>
                            <div className="col-md-8 my-2">
                                <TextField
                                    name='state'
                                    label="State"
                                    value={values.state}
                                    onChange={handleChange('state')}
                                    size="small"
                                    margin="dense"
                                    fullWidth
                                    color='success'
                                    id="outlined-basic"
                                    variant="outlined"
                                    type="text"
                                    sx={{
                                        '.css-bz6wus-MuiInputBase-root-MuiOutlinedInput-root': {
                                            borderRadius: "15px",
                                        },
                                    }}
                                />
                            </div>
                            <div className="col-md-4 my-2">
                                <TextField
                                    name='pincode'
                                    label="Pincode"
                                    value={values.pincode}
                                    onChange={handleChange('pincode')}
                                    size="small"
                                    margin="dense"
                                    fullWidth
                                    color='success'
                                    id="outlined-basic"
                                    variant="outlined"
                                    type="tel"
                                    sx={{
                                        '.css-bz6wus-MuiInputBase-root-MuiOutlinedInput-root': {
                                            borderRadius: "15px",
                                        },
                                    }}
                                />
                            </div>
                            <div className="col-md-8 my-2">
                                <TextField
                                    disabled
                                    name='country'
                                    label="Country"
                                    value={values.country}
                                    onChange={handleChange('country')}
                                    size="small"
                                    margin="dense"
                                    fullWidth
                                    color='success'
                                    id="outlined-basic"
                                    variant="outlined"
                                    type="text"
                                    sx={{
                                        '.css-bz6wus-MuiInputBase-root-MuiOutlinedInput-root': {
                                            borderRadius: "15px",
                                        },
                                    }}
                                />
                            </div>
                        </div>
                        <div className="d-flex align-items-baseline justify-content-center">
                            <button className="green-btn">
                                Save
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default Profile