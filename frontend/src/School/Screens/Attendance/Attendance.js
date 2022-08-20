import React,{useEffect, useState} from 'react'
import TextField from '@mui/material/TextField';
import Box from '@mui/material/Box';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';
import './Attendance.css'
import axios from 'axios'



const Attendance = () => {
    const dt = new Date()
    const date = `${dt.getDate() > 9 ? dt.getDate() : '0' + dt.getDate()}`
    const month = `${dt.getMonth() > 9 ? dt.getMonth() : '0' + dt.getMonth()}`
    const year = dt.getFullYear()
    
    const [totalStudents, setTotalStudents] = useState()
    const [isLoading, setIsLoading] = useState(true)

    const [values, setValues] = React.useState({
        date: `${year}-${month}-${date}`,
        class: "",
        students: []
    });
    
    useEffect(() => {
      axios.get(
        'http://127.0.0.1:7000/schools/attendence/'
        )
        .then(res => {
             setTotalStudents(res.data.msg)
             console.log(res.data.msg);
             setIsLoading(false)
            //  console.log(totalStudents);
            })
            .catch(e => {
                console.log(e);
            })
        // console.log(totalStudents);
    }, [])
    

    const handleChange = (prop) => (event) => {
        setValues({ ...values, [prop]: event.target.value });
    };

    const handleSubmit = (event) => {
        event.preventDefault();
        console.log(values);
        axios.post(
            'http://127.0.0.1:7000/schools/attendence/',
           values
            )
            .then(res => {
                 console.log(res);
                 setValues({ ...values, name: "", meal_pic: "", calories: "", protiens: "" })
            })
            .catch(e => {
                console.log(e);
            })
    }

    const markAttendance = (id) => {
        const array = values.students
        if (array.includes(id)) {
            const index = array.indexOf(id)
            array.splice(index, 1)
        }
        else {
            array.push(id)
            array.sort()
        }
        setValues({ ...values, students: array })
    }

    return (
        <div className='attendance px-2'>
            <div className="my-5">
                <h4 className='text-center'>Attendance</h4>
                <div className="container my-5 p-4 p-md-5 d-flex align-items-center justify-content-between">
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
                                    <MenuItem value={"1"}>Class 1A</MenuItem>
                                    <MenuItem value={"1"}>Class 1B</MenuItem>
                                    <MenuItem value={"1"}>Class 1C</MenuItem>
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
                                }}
                            />
                        
                        </div>

                        {isLoading===true ? <div className="col-md-12">Loading...</div> :
                        <>   
                    {totalStudents.map((student, index) => {
                            const { first_name ,last_name, roll_no} = student
                            return (
                            <div className="col-md-6 col-lg-4 my-3 px-md-3" key={index}>
                                <button className={`w-100 attendance-btn ${values.students.includes(roll_no) ? "selected" : ""}`} onClick={() => markAttendance(roll_no)}>{first_name} {last_name}<br /> Roll No :  {roll_no}</button>
                            </div>
                            )
                        })}
                    </>
}

                    </div>
                    <button className='green-btn mt-4' onClick={handleSubmit}>Submit</button>
                </div>
            </div>
        </div >
    )
}

export default Attendance