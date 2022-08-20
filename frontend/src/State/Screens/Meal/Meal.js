import React, { useState } from 'react'
import TextField from '@mui/material/TextField';
import './Meal.css'

const Meal = () => {
    const dt = new Date()
    const date = `${dt.getDate() > 9 ? dt.getDate() : '0' + dt.getDate()}`
    const month = `${dt.getMonth() > 9 ? dt.getMonth() : '0' + dt.getMonth()}`
    const year = dt.getFullYear()

    const [values, setValues] = React.useState({
        date: `${year}-${month}-${date}`,
        meal_name: "",
        image: "",
        calories: "",
        protiens: ""
    });

    const [error, setError] = useState(false)

    const handleChange = (prop) => (event) => {
        setValues({ ...values, [prop]: event.target.value });
    };

    const handleClick = () => {
        console.log(values);
        setValues({ ...values, meal_name: "", image: "", calories: "", protiens: "" })
    };

    return (
        <div className='meal px-2'>
            <div className="my-5 ">
                <h4 className='text-center'>Upload Mid-day Meals Details</h4>
            </div>
            <div className="container main-form">
                <div className="d-flex align-items-center justify-content-center">
                    <p>Date</p>
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
                            maxWidth: "400px",
                            marginLeft: "4rem"
                        }}
                    />
                </div>
                <TextField
                    className='my-4'
                    name='meal_name'
                    label="Meal Name"
                    value={values.meal_name}
                    onChange={handleChange('meal_name')}
                    size="small"
                    margin="dense"
                    fullWidth
                    color='success'
                    id="outlined-basic"
                    variant="outlined"
                    sx={{
                        '.css-bz6wus-MuiInputBase-root-MuiOutlinedInput-root': {
                            borderRadius: "15px",
                        },

                    }}
                />
                <TextField
                    className='my-3'
                    name='Image'
                    label="file"
                    value={values.image}
                    onChange={handleChange('image')}
                    size="small"
                    margin="dense"
                    fullWidth
                    color='success'
                    id="outlined-basic"
                    variant="outlined"
                    type="file"
                    sx={{
                        '.css-bz6wus-MuiInputBase-root-MuiOutlinedInput-root': {
                            borderRadius: "15px",
                        },

                    }}
                />
                <button className='green-btn my-3'>Upload Image</button>
                <div className="d-flex align-items-center justify-content-center w-100">
                    <TextField
                        className='my-4 me-4'
                        name='calories'
                        label="Calories"
                        value={values.calories}
                        onChange={handleChange('calories')}
                        size="small"
                        margin="dense"
                        fullWidth
                        color='success'
                        id="outlined-basic"
                        variant="outlined"
                        sx={{
                            '.css-bz6wus-MuiInputBase-root-MuiOutlinedInput-root': {
                                borderRadius: "15px",
                            },

                        }}
                    /><TextField
                        className='my-4'
                        name='protiens'
                        label="Protiens"
                        value={values.protiens}
                        onChange={handleChange('protiens')}
                        size="small"
                        margin="dense"
                        fullWidth
                        color='success'
                        id="outlined-basic"
                        variant="outlined"
                        sx={{
                            '.css-bz6wus-MuiInputBase-root-MuiOutlinedInput-root': {
                                borderRadius: "15px",
                            },
                        }}
                    />
                </div>
                <button className='green-btn mt-3' onClick={handleClick}>Submit</button>
            </div>
        </div>
    )
}

export default Meal