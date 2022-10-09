class AuthData {

    saveToken(token) {
        localStorage.setItem("userToken", token)
    }

    saveUserId(id) {
        localStorage.setItem("userId", id)
    }

    getUserToken() {
        return localStorage.getItem("userToken")
    }

    getUserId() {
        return localStorage.getItem("userId")
    }

    deleteToken() {
        localStorage.removeItem("userToken")
    }

    setCompanyId(id) {
        localStorage.setItem("company_id", id)
    }

    getCompanyId() {
        return localStorage.getItem("company_id")
    }

    setUserData(data) {
        localStorage.setItem("user_data", data)
    }

    getUserData() {
        return localStorage.getItem("user_data")
    }
}

let auth_data = new AuthData
export default auth_data