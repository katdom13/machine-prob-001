import React, { useState } from "react"

import {
  Box,
  Button,
  Card,
  CardContent,
  Checkbox,
  Container,
  FormControlLabel,
  FormGroup,
  LinearProgress,
  Typography,
} from "@mui/material"
import Router from "next/router"

import { uploadCouponList } from "../../config/axios"

const UploadCoupon = () => {
  const [file, setFile] = useState(undefined)

  const [progress, setProgress] = useState(0)

  const [isRewrite, setIsRewrite] = useState(false)

  const [isSuccess, setIsSuccess] = useState(false)
  const [isError, setIsError] = useState(false)
  const [message, setMessage] = useState("")

  const handleSelectFile = (event) => {
    setFile(event.target.files[0])
  }

  const handleUpload = () => {
    setIsError(false)

    uploadCouponList(file, isRewrite, (event) =>
      setProgress(Math.round((100 * event.loaded) / event.total))
    )
      .then((response) => {
        setIsSuccess(true)
        setMessage(response.data.success)
      })
      .catch(() => {
        setIsError(true)
        setFile(undefined)
      })
  }

  return (
    <Box padding={2} margin={6}>
      <Container maxWidth="sm">
        <Card
          variant="outlined"
          sx={{
            borderColor: (theme) => theme.palette.grey[500],
          }}
        >
          <CardContent>
            <Typography variant="h4" gutterBottom>
              Upload Coupon List
            </Typography>

            {!file && !isSuccess && (
              <Typography variant="body1" color="text.secondary" gutterBottom>
                Upload a text file containing coupon codes, separated by newlines.
              </Typography>
            )}

            {isError && (
              <Typography variant="body2" color="red">
                Error in uploading file. Please try uploading another file.
              </Typography>
            )}

            {!file && !isSuccess && (
              <label htmlFor="btn-upload">
                <input
                  id="btn-upload"
                  name="btn-upload"
                  style={{ display: "none" }}
                  type="file"
                  onChange={handleSelectFile}
                />
                <Box marginY={2}>
                  <Button variant="contained" component="span">
                    Select file
                  </Button>
                </Box>
              </label>
            )}

            {file && (
              <Box marginY={1}>
                <LinearProgressWithLabel value={progress} />
              </Box>
            )}

            {file && !isSuccess && (
              <>
                <Typography variant="body2" color="text.secondary" gutterBottom>
                  {file.name}
                </Typography>
                <FormGroup>
                  <FormControlLabel
                    control={
                      <Checkbox
                        size="small"
                        checked={isRewrite}
                        onChange={(event) => setIsRewrite(event.target.checked)}
                      />
                    }
                    label="Rewrite all coupon in database"
                  />
                </FormGroup>
                <Box marginTop={2} display="flex" justifyContent="center">
                  <Button variant="contained" onClick={handleUpload}>
                    Upload
                  </Button>
                </Box>
              </>
            )}

            {isSuccess && (
              <>
                <Box
                  marginTop={2}
                  display="flex"
                  flexDirection="column"
                  justifyContent="center"
                  alignItems="center"
                >
                  <Box marginBottom={1}>
                    <Typography variant="h6" color="text.secondary" gutterBottom>
                      {message}
                    </Typography>
                  </Box>

                  <Button variant="contained" onClick={() => Router.reload()}>
                    Confirm
                  </Button>
                </Box>
              </>
            )}
          </CardContent>
        </Card>
      </Container>
    </Box>
  )
}

const LinearProgressWithLabel = (props) => {
  return (
    <Box
      sx={{
        display: "flex",
        alignItems: "center",
      }}
    >
      <Box
        sx={{
          width: "100%",
          mr: 1,
        }}
      >
        <LinearProgress variant="determinate" {...props} />
      </Box>
      <Box sx={{ minWidth: 35 }}>
        <Typography variant="body2" color="text.secondary">{`${Math.round(
          props.value
        )}%`}</Typography>
      </Box>
    </Box>
  )
}

export default UploadCoupon
