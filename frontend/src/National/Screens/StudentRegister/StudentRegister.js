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
        dob: `${year}-${month}-${date}`,
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
                            value={values.first_name}
                            onChange={handleChange('first_name')}
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
                    {/* <div className="col-md-6 my-2">
                        <TextField
                            name='last_name'
                            label="Last Name"
                            value={values.last_name}
                            onChange={handleChange('last_name')}
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
                    </div> */}
                    <div className="col-md-6 my-2">
                        <TextField
                            name='user_name'
                            label="User Name"
                            value={values.mother_name}
                            onChange={handleChange('mother_name')}
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
                            value={values.father_name}
                            onChange={handleChange('father_name')}
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
                            name='gr_no'
                            label="G.R.No."
                            value={values.gr_no}
                            onChange={handleChange('gr_no')}
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
                            name='roll_no'
                            label="Roll No."
                            value={values.roll_no}
                            onChange={handleChange('roll_no')}
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
                        <h6>Date of Birth</h6>
                    </div>
                    <div className="col-md-6 my-2">
                        <TextField
                            name='Date of Birth'
                            label="Date of Birth"
                            value={values.dob}
                            onChange={handleChange('dob')}
                            size="small"
                            margin="dense"
                            fullWidth
                            color='success'
                            id="outlined-basic"
                            variant="outlined"
                            type="date"
                            sx={{
                                '.css-bz6wus-MuiInputBase-root-MuiOutlinedInput-root': {
                                    borderRadius: "15px",
                                },
                                // maxWidth: "400px",
                            }}
                        />
                    </div>
                    <div className="col-md-6 my-2">
                        <h6>Class</h6>
                    </div>
                    <div className="col-md-6 my-2">
                        <FormControl fullWidth>
                            <InputLabel >Class</InputLabel>
                            <Select
                                value={values.class}
                                label="Class"
                                onChange={handleChange('class')}
                                size="small"
                                margin="dense"
                                fullWidth
                                color='success'
                                sx={{

                                    borderRadius: "15px ",
                                    // maxWidth: "400px",

                                }}
                            >
                                <MenuItem value={"1A"}>Class 1A</MenuItem>
                                <MenuItem value={"1B"}>Class 1B</MenuItem>
                                <MenuItem value={"1C"}>Class 1C</MenuItem>
                            </Select>
                        </FormControl>
                    </div>
                    <div className="col-md-6 my-2">
                        <TextField
                            name='height'
                            label="Height"
                            value={values.height}
                            onChange={handleChange('height')}
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
                            name='weight'
                            label="Weight"
                            value={values.weight}
                            onChange={handleChange('weight')}
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