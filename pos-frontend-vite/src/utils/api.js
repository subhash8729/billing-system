import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:5000',
  headers: {
    'Content-Type': 'application/json',
  },
});

api.interceptors.request.use((config) => {
  const jwt = localStorage.getItem('jwt');
  const isAuthCall = config.url?.startsWith('/auth/');
  if (jwt && !isAuthCall && !config.headers.Authorization) {
    config.headers.Authorization = `Bearer ${jwt}`;
  }
  return config;
});

export default api;
