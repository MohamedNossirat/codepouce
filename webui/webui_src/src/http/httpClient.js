import axios from "axios";

const httpClient = axios;
httpClient.defaults.baseURL = "http://127.0.0.1:8000/";

export default httpClient;
