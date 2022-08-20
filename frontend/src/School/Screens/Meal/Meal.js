import React, { useState } from 'react'
import TextField from '@mui/material/TextField';
import './Meal.css'
import axios from 'axios'

const Meal = () => {
    const dt = new Date()
    const date = `${dt.getDate() > 9 ? dt.getDate() : '0' + dt.getDate()}`
    const month = `${dt.getMonth() > 9 ? dt.getMonth() : '0' + dt.getMonth()}`
    const year = dt.getFullYear()

    const [values, setValues] = React.useState({
        date: `${year}-${month}-${date}`,
        name: "",
        meal_pic: "",
        calories: "",
        protiens: ""
    });

    const [error, setError] = useState(false)

    const handleChange = (prop) => (event) => {
        setValues({ ...values, [prop]: event.target.value });
    };


    const handleClick = () => {
        var pic=values['meal_pic'].split('fakepath\\');
        values['meal_pic']=pic[1];
        console.log(values)
        axios.post(
            'http://127.0.0.1:7000/schools/meal/',
           values
            )
            .then(res => {
                 console.log(res);
                 setValues({ ...values, name: "", meal_pic: "", calories: "", protiens: "" })
            })
            .catch(e => {
                console.log(e);
            })
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
                    value={values.name}
                    onChange={handleChange('name')}
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
                    value={values.meal_pic}
                    onChange={handleChange('meal_pic')}
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
                <button className='green-btn my-3' onClick={handleClick}>Upload Image</button>
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