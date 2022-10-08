


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

export default {saveToken, saveUserId, getUserToken, getUserId, deleteToken}