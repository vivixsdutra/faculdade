import axios from 'axios'

const api = axios.create({ baseURL: '/api' })

// Filmes
export const getFilmes = (params) => api.get('/filmes/', { params })
export const getFilme = (id) => api.get(`/filmes/${id}`)
export const criarFilme = (data) => api.post('/filmes/', data)
export const atualizarFilme = (id, data) => api.put(`/filmes/${id}`, data)
export const deletarFilme = (id) => api.delete(`/filmes/${id}`)

// Gêneros
export const getGeneros = () => api.get('/generos/')
export const criarGenero = (data) => api.post('/generos/', data)
export const deletarGenero = (id) => api.delete(`/generos/${id}`)

// Avaliações
export const getAvaliacoes = (filmeId) => api.get(`/filmes/${filmeId}/avaliacoes`)
export const criarAvaliacao = (filmeId, data) => api.post(`/filmes/${filmeId}/avaliacoes`, data)
export const atualizarAvaliacao = (id, data) => api.put(`/avaliacoes/${id}`, data)
export const deletarAvaliacao = (id) => api.delete(`/avaliacoes/${id}`)
