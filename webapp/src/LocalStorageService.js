


function saveToken(token){
    localStorage.setItem("userToken", token)
}

function saveUserId(id){
    localStorage.setItem("userId", id)
}

function getUserToken(){
    return localStorage.getItem("userToken")
}

function getUserId(){
    return localStorage.getItem("userId")
}

function deleteToken(){
    localStorage.removeItem("userToken")
}

function setCompanyId(id) {
    localStorage.setItem("company_id", id)
} 

function getCompanyId() {
    return localStorage.getItem("company_id")
}
export default {saveToken, saveUserId, getUserToken, getUserId, deleteToken, setCompanyId, getCompanyId}