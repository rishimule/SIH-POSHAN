import React from 'react'
import './StudentRegister.css'
import TextField from '@mui/material/TextField';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';

const StudentRegister = () => {
    const dt = new Date()
    const date = `${dt.getDate() > 9 ? dt.getDate() : '0' + dt.getDate()}`
    const month = `${dt.getMonth() > 9 ? dt.getMonth() : '0' + dt.getMonth()}`
    const year = dt.getFullYear() - 18

    const [values, setValues] = React.useState({
        school_name: "",
        user_name: "",
        uicd_no: "",
        address_1: "",
        address_2: "",
        district: "",
        state: "",
        pincode: "",
        country: "India",
        email: "",
        password: "",
        confirm_password: "",
    });

    const handleChange = (prop) => (event) => {
        setValues({ ...values, [prop]: event.target.value });
    };

    const handleClick = () => {
        console.log(values);
        setValues({ ...values, meal_name: "", image: "", calories: "", protiens: "" })
    };

    return (
        <div className='register p-2'>
            <div className="my-5">
                <h4 className='text-center'>Register School</h4>
            </div>
            <div className="container p-5">
                <div className="row w-100">
                    <div className="col-md-12 my-2">
                        <TextField
                            name='school_name'
                            label="School Name"
                            value={values.school_name}
                            onChange={handleChange('school_name')}
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
                    ``
                    <div className="col-md-6 my-2">
                        <TextField
                            name='user_name'
                            label="User Name"
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
                            name='uicd_no'
                            label="UICD No"
                            value={values.uicd_no}
                            onChange={handleChange('uicd_no')}
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
                            name='address_1'
                            label="Address Line 1"
                            value={values.address_1}
                            onChange={handleChange('address_1')}
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
                            name='address_2'
                            label="Address Line 2"
                            value={values.address_2}
                            onChange={handleChange('address_2')}
                            size="small"
                            margin="dense"
                            fullWidth
                            color='success'
                            id="outlined-basic"
                            variant="outlined"
                            type="number"
                            sx={{
                                '.css-bz6wus-MuiInputBase-root-MuiOutlinedInput-root': {
                                    borderRadius: "15px",
                                },
                            }}
                        />
                    </div>
                    <div className="col-md-6 my-2">
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
                    <div className="col-md-6 my-2">
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
                    <div className="col-md-6 my-2">
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
                    <div className="col-md-12 my-2">
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
                            type="number"
                            sx={{
                                '.css-bz6wus-MuiInputBase-root-MuiOutlinedInput-root': {
                                    borderRadius: "15px",
                                },
                            }}
                        />
                    </div>
                    <div className="col-md-6 my-2">
                        <TextField
                            name='password'
                            label="Password"
                            value={values.password}
                            onChange={handleChange('password')}
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
                            name='confirm_password'
                            label="Confirm Password"
                            value={values.confirm_password}
                            onChange={handleChange('confirm_password')}
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
                <button className="green-btn mt-4">
                    Register
                </button>
            </div>
        </div >
    )
}

export default StudentRegister