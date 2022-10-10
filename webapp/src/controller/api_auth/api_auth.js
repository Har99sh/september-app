import axios from "axios";
const BASE_URL = 'http://127.0.0.1:5000/';

const api_user = JSON.parse(localStorage.getItem('j4w_user'));
export const authApi = axios.create({
  baseURL: BASE_URL,
  headers: {"Authorization" : 'Bearer ' + api_user.token}
});

export {api_user}
