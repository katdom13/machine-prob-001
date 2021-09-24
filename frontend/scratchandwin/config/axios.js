import axios from "axios"

import { apiUrl } from "./apiUrl"

const instance = axios.create({
  baseURL: apiUrl,
  timeout: 300000,
  headers: {
    "Content-Type": "application/json",
    accept: "application/json",
  },
})

const invoke = async (url, method = "get", data = {}, csrf = "") => {
  return instance({
    method: method,
    url: url,
    data: data,
    headers: {
      ...instance.defaults.headers,
      "X-CSRFToken": csrf,
    },
  })
    .then((response) => Promise.resolve(response.data))
    .catch((error) => Promise.reject(error))
}

// Promises

const submitEntry = async (code, mobile) => {
  const data = { code, mobile }
  return invoke("promo/", "post", data)
}

const verifyCaptcha = async (token) => {
  const data = { recaptcha: token }
  return invoke("recaptcha/", "post", data)
}

const uploadCouponList = async (file, is_rewrite = false, onUploadProgress) => {
  let formData = new FormData()
  formData.append("file", file)

  return instance.post(
    `coupon/upload/${is_rewrite ? "?rewrite=True" : ""}`,
    formData,
    {
      headers: {
        "Content-Type": "multipart/form-data",
      },
      onUploadProgress,
    }
  )
}

export { submitEntry, verifyCaptcha, uploadCouponList }
