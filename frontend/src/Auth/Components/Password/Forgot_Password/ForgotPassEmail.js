import React, { useState } from 'react'
import TextField from '@mui/material/TextField';
import Snackbar from '@mui/material/Snackbar';
import MuiAlert from '@mui/material/Alert';

const Alert = React.forwardRef(function Alert(props, ref) {
    return <MuiAlert elevation={6} ref={ref} variant="filled" {...props} />;
});

const Forgot_Pass_Email = ({ setCurrPage }) => {
    const [data, setData] = useState()
    const [email, setEmail] = useState("")
    const [state, setState] = React.useState({
        open: false,
        vertical: 'top',
        horizontal: 'center',
    });

    const { vertical, horizontal, open } = state;

    const handleChange = (e) => {
        e.preventDefault()
        setEmail(e.target.value)
        setData({ [e.target.name]: e.target.value })
    }

    const handleClick = (newState) => () => {
        console.log(data);
        if (email === "") {
            alert("Please enter your email")
        } else {
            // setEmail("")
            setState({ open: true, ...newState });
            setTimeout(() => {
                setCurrPage(2)
            }, 2000)
        }
    };

    const handleClose = () => {
        setState({ ...state, open: false });
    };

    return (
        <div className='forgot-pass container-fluid d-flex align-items-center justify-content-center'>
            <div className="container bg-light">
                <h2 className='text-center'>Reset Your Password</h2>
                <p className='info'>Enter your user account's verified email address and we will send you a password reset link.</p>
                <TextField
                    name='email'
                    label="Email"
                    value={email}
                    onChange={handleChange}
                    size="small"
                    margin="dense"
                    fullWidth
                    color='success'
                    id="outlined-basic"
                    variant="outlined"
                    sx={{
                        '.css-bz6wus-MuiInputBase-root-MuiOutlinedInput-root': {
                            borderRadius: "15px",
                        }
                    }}
                />
                <button id='reset-btn' onClick={handleClick({
                    vertical: 'top',
                    horizontal: 'right',
                })}
                >Reset Password</button>
            </div>
            <Snackbar open={open} autoHideDuration={3000} onClose={handleClose} anchorOrigin={{ vertical, horizontal }}
                message="I love snacks"
                key={vertical + horizontal}>
                <Alert onClose={handleClose} severity="success" sx={{ width: '100%' }}>
                    Email Sent Successfully!
                </Alert>
            </Snackbar>
        </div>
    )
}

export default Forgot_Pass_Email