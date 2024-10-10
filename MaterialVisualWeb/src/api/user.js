import request from '@/utils/request'

export function login(data) {
  return request({
    url: '/api/login/',
    method: 'post',
    data
  })
}

export function getInfo(url) {
  return request({
    url: url,
    method: 'get'
  })
}

export function logout() {
  return request({
    url: '/api/v1',
    method: 'get'
  })
}
