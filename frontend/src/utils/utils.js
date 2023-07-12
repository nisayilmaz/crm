import axios from 'axios';
let isDev = import.meta.env.DEV
const serverUrl = isDev ? "http://localhost:5000" : ""
console.log(isDev, serverUrl)
const axiosInstance = axios.create({
    baseURL : serverUrl + "/api",
    headers: {
        Authorization : `${localStorage.getItem("accessToken")}`
    }
})

export default axiosInstance