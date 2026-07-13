import { useEffect, useState } from 'react'
import { useParams, useNavigate } from 'react-router-dom'
import { getFilme, criarFilme, atualizarFilme, getGeneros } from '../api'

export default function FormFilme() {
  const { id } = useParams()
  const navigate = useNavigate()
  const editando = Boolean(id)
  const [generos, setGeneros] = useState([])
  const [form, setForm] = useState({
    titulo: '', tipo: 'filme', ano: '', sinopse: '',
    diretor: '', poster_url: '', duracao_min: '', genero_ids: [],
  })
  const [erro, setErro] = useState('')

  useEffect(() => {
    getGeneros().then(r => setGeneros(r.data))
    if (editando) {
      getFilme(id).then(r => {
        const f = r.data
        setForm({
          titulo: f.titulo, tipo: f.tipo, ano: f.ano || '',
          sinopse: f.sinopse || '', diretor: f.diretor || '',
          poster_url: f.poster_url || '', duracao_min: f.duracao_min || '',
          genero_ids: f.generos.map(g => g.id),
        })
      })
    }
  }, [id])

  const toggleGenero = (gid) => {
    setForm(prev => ({
      ...prev,
      genero_ids: prev.genero_ids.includes(gid)
        ? prev.genero_ids.filter(x => x !== gid)
        : [...prev.genero_ids, gid]
    }))
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    setErro('')
    try {
      const payload = { ...form, ano: form.ano ? +form.ano : null, duracao_min: form.duracao_min ? +form.duracao_min : null }
      if (editando) {
        await atualizarFilme(id, payload)
        navigate(`/filmes/${id}`)
      } else {
        const { data } = await criarFilme(payload)
        navigate(`/filmes/${data.id}`)
      }
    } catch (err) {
      setErro(err.response?.data?.detail || 'Erro ao salvar')
    }
  }

  const set = (key) => (e) => setForm(prev => ({ ...prev, [key]: e.target.value }))

  return (
    <div className="container">
      <div className="form-container">
        <h2>{editando ? 'Editar título' : 'Adicionar título'}</h2>
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label>Título *</label>
            <input value={form.titulo} onChange={set('titulo')} required />
          </div>
          <div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'1rem'}}>
            <div className="form-group">
              <label>Tipo *</label>
              <select value={form.tipo} onChange={set('tipo')}>
                <option value="filme">Filme</option>
                <option value="serie">Série</option>
              </select>
            </div>
            <div className="form-group">
              <label>Ano</label>
              <input type="number" value={form.ano} onChange={set('ano')} placeholder="ex: 2024" />
            </div>
          </div>
          <div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'1rem'}}>
            <div className="form-group">
              <label>Diretor</label>
              <input value={form.diretor} onChange={set('diretor')} />
            </div>
            <div className="form-group">
              <label>Duração (min)</label>
              <input type="number" value={form.duracao_min} onChange={set('duracao_min')} />
            </div>
          </div>
          <div className="form-group">
            <label>URL do Poster</label>
            <input value={form.poster_url} onChange={set('poster_url')} placeholder="https://..." />
          </div>
          <div className="form-group">
            <label>Sinopse</label>
            <textarea value={form.sinopse} onChange={set('sinopse')} />
          </div>
          <div className="form-group">
            <label>Gêneros</label>
            <div className="generos-check">
              {generos.map(g => (
                <label key={g.id} className="genero-check-item"
                  style={{background: form.genero_ids.includes(g.id) ? '#e50914' : '#222'}}>
                  <input type="checkbox" style={{display:'none'}}
                    checked={form.genero_ids.includes(g.id)}
                    onChange={() => toggleGenero(g.id)} />
                  {g.nome}
                </label>
              ))}
            </div>
          </div>
          {erro && <p className="error-msg">{erro}</p>}
          <div className="form-actions">
            <button type="submit" className="btn btn-primary">
              {editando ? 'Salvar alterações' : 'Cadastrar'}
            </button>
            <button type="button" className="btn btn-secondary" onClick={() => navigate(-1)}>
              Cancelar
            </button>
          </div>
        </form>
      </div>
    </div>
  )
}
