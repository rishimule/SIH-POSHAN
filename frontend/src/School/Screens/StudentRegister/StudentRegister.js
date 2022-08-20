import React from 'react'
import './StudentRegister.css'
import TextField from '@mui/material/TextField';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';
import axios from 'axios'

const StudentRegister = () => {
    const dt = new Date()
    const date = `${dt.getDate() > 9 ? dt.getDate() : '0' + dt.getDate()}`
    const month = `${dt.getMonth() > 9 ? dt.getMonth() : '0' + dt.getMonth()}`
    const year = dt.getFullYear() - 18

    const [values, setValues] = React.useState({
        first_name: "",
        last_name: "",
        father_name: "",
        mother_name: "",
        gr_no: "",
        roll_no: "",
        dob: `${year}-${month}-${date}`,
        current_class: "",
        current_height: "",
        current_weight: "",
    });

    

    const handleChange = (prop) => (event) => {
        setValues({ ...values, [prop]: event.target.value });
    };

    const handleClick = () => {
        console.log(values)
        axios.post(
            'http://127.0.0.1:7000/schools/register_students/',
           values
            )
            .then(res => {
                 console.log(res);
                 alert('register successfully')
                //  setValues({ ...values, meal_name: "", image: "", calories: "", protiens: "" })
            })
            .catch(e => {
                console.log(e);
            })
    };

    return (
        <div className='register p-2'>
            <div className="my-5">
                <h4 className='text-center'>Register Student</h4>
            </div>
            <div className="container p-5">
                <div className="row w-100">
                    <div className="col-md-6 my-2">
                        <TextField
                            name='first_name'
                            label="First Name"
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
                    <div className="col-md-6 my-2">
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
                    </div>
                    <div className="col-md-6 my-2">
                        <TextField
                            name='mother_name'
                            label="Mother's Name"
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
                            name='father_name'
                            label="Father's Name"
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
                    <div className="col-md-6 my-2">
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
                                value={values.current_class}
                                label="Class"
                                onChange={handleChange('current_class')}
                                size="small"
                                margin="dense"
                                fullWidth
                                color='success'
                                sx={{

                                    borderRadius: "15px ",
                                    // maxWidth: "400px",

                                }}
                            >
                                <MenuItem value={"1"}>Class 1A</MenuItem>
                                <MenuItem value={"1"}>Class 1B</MenuItem>
                                <MenuItem value={"1"}>Class 1C</MenuItem>
                            </Select>
                        </FormControl>
                    </div>
                    <div className="col-md-6 my-2">
                        <TextField
                            name='height'
                            label="Height"
                            value={values.current_height}
                            onChange={handleChange('current_height')}
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
                            value={values.current_weight}
                            onChange={handleChange('current_weight')}
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
                <button className="green-btn mt-4" onClick={handleClick}>
                    Register
                </button>
            </div>
        </div >
    )
}

export default StudentRegister