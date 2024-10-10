// import Cookies from 'js-cookie'

const TokenKey = 'Token'

export function getToken() {
  return localStorage.getItem(TokenKey)
}

export function setToken(token) {
  return localStorage.setItem(TokenKey, token)
}

export function removeToken() {
  return localStorage.removeItem(TokenKey)
}

export function getUrl(){
  const id = localStorage.getItem('id')
  if (id === '1'){
    return '/api/v1/users/admin_info/'
  } else {
    return '/api/v1/users/' + id + '/'
  }
}
