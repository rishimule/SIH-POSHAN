import React from 'react'
import './Details.css'
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow'; function createData(name, rollNo, grNo, curClass) {
    return { name, rollNo, grNo, curClass };
}

const rows = [
    createData('Student 1', 1, 1423, "1A"),
    createData('Student 2', 3, 1430, "1A"),
    createData('Student 2', 3, 1430, "1A"),
    createData('Student 2', 3, 1430, "1A"),
    createData('Student 2', 3, 1430, "1A"),
    createData('Student 2', 3, 1430, "1A"),
    createData('Student 2', 3, 1430, "1A"),
    createData('Student 2', 3, 1430, "1A"),
    createData('Student 2', 3, 1430, "1A"),
    createData('Student 2', 3, 1430, "1A"),
    createData('Student 2', 3, 1430, "1A"),
    createData('Student 2', 3, 1430, "1A"),
    createData('Student 2', 3, 1430, "1A"),
    createData('Student 2', 3, 1430, "1A"),
    createData('Student 2', 3, 1430, "1A"),
    createData('Student 2', 3, 1430, "1A"),
    createData('Student 2', 3, 1430, "1A"),
    createData('Student 2', 3, 1430, "1A"),
    createData('Student 2', 3, 1430, "1A"),
    createData('Student 2', 3, 1430, "1A"),
    createData('Student 2', 3, 1430, "1A"),

];

const Details = () => {
    const dt = new Date()
    const date = `${dt.getDate() > 9 ? dt.getDate() : '0' + dt.getDate()}`
    const month = `${dt.getMonth() > 9 ? dt.getMonth() : '0' + dt.getMonth()}`
    const year = dt.getFullYear() - 18

    const [values, setValues] = React.useState({
        class: ""
    });

    const handleChange = (prop) => (event) => {
        setValues({ ...values, [prop]: event.target.value });
    };

    return (
        <div className='details p-2'>
            <div className="my-5">
                <h4 className='text-center'>Student Details</h4>
            </div>
            <div className="container p-4">
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
                            maxWidth: "150px",

                        }}
                    >
                        <MenuItem value={"1A"}>Class 1A</MenuItem>
                        <MenuItem value={"1B"}>Class 1B</MenuItem>
                        <MenuItem value={"1C"}>Class 1C</MenuItem>
                    </Select>
                </FormControl>

                <div className="container-fluid table-con my-4">
                    <TableContainer  >
                        <Table sx={{ minWidth: 380 }} aria-label="simple table">
                            <TableHead sx={{ border: "0" }}>
                                <TableRow >
                                    <TableCell>Name</TableCell>
                                    <TableCell align="right">Roll No</TableCell>
                                    <TableCell align="right">GR No</TableCell>
                                    <TableCell align="right">Class</TableCell>
                                </TableRow>
                            </TableHead>
                            <TableBody>
                                {rows.map((row) => (
                                    <TableRow
                                        key={row.name}
                                        sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
                                    >
                                        <TableCell component="th" scope="row">
                                            {row.name}
                                        </TableCell>
                                        <TableCell align="right">{row.rollNo}</TableCell>
                                        <TableCell align="right">{row.grNo}</TableCell>
                                        <TableCell align="right">{row.curClass}</TableCell>
                                    </TableRow>
                                ))}
                            </TableBody>
                        </Table>
                    </TableContainer>
                </div>

            </div>
        </div >
    )
}

export default Details