import React from "react"
import "../styles/globals.css"

import { CacheProvider } from "@emotion/react"
import CssBaseline from "@mui/material/CssBaseline"
import Head from "next/head"

import createEmotionCache from "../config/createEmotionCache"

// Client-side cache, shared for the whole session of the user in the the browser
const clientSideEmotionCache = createEmotionCache()

function MyApp(props) {
  const { Component, emotionCache = clientSideEmotionCache, pageProps } = props

  return (
    <CacheProvider value={emotionCache}>
      <Head>
        <title>Scratch and win</title>
        <meta name="viewport" content="initial-scale=1, width=device-width" />
      </Head>

      <CssBaseline />
      <Component {...pageProps} />
    </CacheProvider>
  )
}

export default MyApp
