import React, { useState } from "react"

import {
  Alert,
  Box,
  Button,
  Card,
  CardActions,
  CardContent,
  Container,
  Divider,
  TextField,
  Typography,
} from "@mui/material"
import Router from "next/router"
import ReCAPTCHA from "react-google-recaptcha"

import { submitEntry, verifyCaptcha } from "../config/axios"

export default function Home() {
  const [isSubmitted, setIsSubmitted] = useState(false)
  const [isVerified, setIsVerified] = useState(false)

  const initialFormData = {
    code: "",
    mobile: "",
  }

  const [formData, setFormData] = useState(initialFormData)
  const [formErrors, setFormErrors] = useState({})

  const [alert, setAlert] = useState({
    severity: "info",
    message: "",
  })

  const handleChange = (name, value) => {
    setFormData({
      ...formData,
      [name]: value,
    })
  }

  const handleSubmit = (e) => {
    e.preventDefault()

    // Reset error and alerts
    setFormErrors({})
    setAlert({ ...alert, message: "" })

    if (isSubmitted) {
      Router.reload()
    } else {
      if (isVerified) {
        submitEntry(formData.code, formData.mobile)
          .then(() => setIsSubmitted(true))
          .catch((err) => {
            if (err && err.response) {
              if ([404, 409].includes(err.response.status)) {
                setAlert({ ...alert, message: err.response.data.error })
              }
              if (err.response.status === 429) {
                setAlert({
                  ...alert,
                  message: "You have reached your limit for today",
                })
              }
              if (err.response.status === 400) {
                setFormErrors({
                  ...formErrors,
                  ...err.response.data,
                })
              }
            }
          })
      } else {
        setAlert({
          ...alert,
          message: "Please accomplish the recaptcha first",
        })
      }
    }
  }

  const handleCaptcha = (token) => {
    verifyCaptcha(token)
      .then(() => setIsVerified(true))
      .catch((err) => {
        console.log("[RECAPTCHA ERROR]", err && err.response ? err.response : err)
        if (err.response.status === 429) {
          setAlert({
            ...alert,
            message: "You have reached your limit for today",
          })
        }
      })
  }

  return (
    <Box padding={2} margin={6}>
      <Container maxWidth="sm">
        <form onSubmit={handleSubmit}>
          <Card
            variant="outlined"
            sx={{
              borderColor: (theme) => theme.palette.grey[500],
            }}
          >
            <CardContent
              sx={{
                minHeight: 245,
              }}
            >
              <Typography variant="h4" gutterBottom>
                Scratch and Win Promo
              </Typography>
              <Divider
                variant="middle"
                sx={{
                  borderColor: (theme) => theme.palette.grey[500],
                }}
              />
              {alert && alert.message ? (
                <Box marginTop={2}>
                  <Alert severity={alert.severity} variant="outlined">
                    {alert.message}
                  </Alert>
                </Box>
              ) : null}
              {isSubmitted ? (
                <Box
                  display="flex"
                  flexDirection="column"
                  alignItems="center"
                  marginY={4}
                >
                  <Typography variant="h6" gutterBottom>
                    Thank you for your submission.
                  </Typography>
                  <Typography variant="body1" color="GrayText">
                    You will receive an SMS shortly.
                  </Typography>
                </Box>
              ) : (
                <>
                  <TextField
                    variant="filled"
                    margin="normal"
                    required
                    fullWidth
                    id="code"
                    name="code"
                    label="Coupon code"
                    autoFocus
                    value={formData.code}
                    onChange={(e) => handleChange(e.target.name, e.target.value)}
                    error={Boolean(formErrors.code)}
                    helperText={formErrors.code}
                  />

                  <TextField
                    variant="filled"
                    margin="normal"
                    required
                    fullWidth
                    id="mobile"
                    name="mobile"
                    label="Mobile number"
                    placeholder="+639174167279"
                    value={formData.mobile}
                    onChange={(e) => handleChange(e.target.name, e.target.value)}
                    error={Boolean(formErrors.mobile)}
                    helperText={formErrors.mobile}
                  />
                </>
              )}
            </CardContent>
            <CardActions sx={{ flexDirection: "row-reverse" }}>
              <Button type="submit" variant="outlined">
                {isSubmitted ? "Confirm" : "Next"}
              </Button>
            </CardActions>
          </Card>
          {isSubmitted ? null : (
            <Box display="flex" justifyContent="center" marginY={2}>
              <ReCAPTCHA
                sitekey={process.env.NEXT_PUBLIC_RECAPTCHA_SITE_KEY}
                onChange={handleCaptcha}
              />
            </Box>
          )}
        </form>
      </Container>
    </Box>
  )
}
