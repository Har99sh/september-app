import axios from "axios";
import { useAuthStore } from "../store/auth.store";

const BASE_URL = 'http://127.0.0.1:5000/';
const authStore = new useAuthStore;
const token = authStore.getToken();
export const api_user_id = authStore.getUserId();

export const authApi = axios.create({
  baseURL: BASE_URL,
  headers: {"Authorization" : 'Bearer ' + token}
});
