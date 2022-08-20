import React from 'react'
import TextField from '@mui/material/TextField';
import Box from '@mui/material/Box';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';
import './Attendance.css'



const Attendance = () => {
    const dt = new Date()
    const date = `${dt.getDate() > 9 ? dt.getDate() : '0' + dt.getDate()}`
    const month = `${dt.getMonth() > 9 ? dt.getMonth() : '0' + dt.getMonth()}`
    const year = dt.getFullYear()

    const [values, setValues] = React.useState({
        date: `${year}-${month}-${date}`,
        class: "",
        names: [],
        name1: "",
        name2: "",

    });

    const handleChange = (prop) => (event) => {
        setValues({ ...values, [prop]: event.target.value });
    };

    const handleClick = () => {
        console.log(values);
        setValues({ ...values, meal_name: "", image: "", calories: "", protiens: "" })
    };

    return (
        <div className='attendance px-2'>
            <div className="my-5">
                <h4 className='text-center'>Attendance</h4>
                <div className="container my-5 p-5 d-flex align-items-center justify-content-between">
                    <div className="row w-100">
                        <div className="col-md-6">
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
                        <div className="col-md-6">
                            <TextField
                                name='date'
                                label="Date"
                                value={values.date}
                                onChange={handleChange('date')}
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
                        <div className="col-md-6">
                            <TextField
                                name='name 1'
                                label="Name 1"
                                value={values.name1}
                                onChange={handleChange('name1')}
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
                        <div className="col-md-6">
                            <TextField
                                name='name 2'
                                label="Name 2"
                                value={values.name2}
                                onChange={handleChange('name2')}
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
                        <div className="col-md-6">
                            <TextField
                                name='name 1'
                                label="Name 1"
                                value={values.name1}
                                onChange={handleChange('name1')}
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
                        <div className="col-md-6">
                            <TextField
                                name='name 2'
                                label="Name 2"
                                value={values.name2}
                                onChange={handleChange('name2')}
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
                        <div className="col-md-6">
                            <TextField
                                name='name 1'
                                label="Name 1"
                                value={values.name1}
                                onChange={handleChange('name1')}
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
                        <div className="col-md-6">
                            <TextField
                                name='name 2'
                                label="Name 2"
                                value={values.name2}
                                onChange={handleChange('name2')}
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
                        <div className="col-md-6">
                            <TextField
                                name='name 1'
                                label="Name 1"
                                value={values.name1}
                                onChange={handleChange('name1')}
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
                        <div className="col-md-6">
                            <TextField
                                name='name 2'
                                label="Name 2"
                                value={values.name2}
                                onChange={handleChange('name2')}
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
                    <button className='green-btn mt-4'>Submit</button>
                </div>
            </div>
        </div >
    )
}

export default Attendance