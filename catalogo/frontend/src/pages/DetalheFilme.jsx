import { useEffect, useState } from 'react'
import { useParams, useNavigate } from 'react-router-dom'
import { getFilme, deletarFilme, criarAvaliacao, deletarAvaliacao } from '../api'

export default function DetalheFilme() {
  const { id } = useParams()
  const navigate = useNavigate()
  const [filme, setFilme] = useState(null)
  const [novaAv, setNovaAv] = useState({ autor: '', nota: '', comentario: '' })
  const [erro, setErro] = useState('')

  const carregar = async () => {
    const { data } = await getFilme(id)
    setFilme(data)
  }

  useEffect(() => { carregar() }, [id])

  const handleDeletar = async () => {
    if (!confirm('Deletar este título?')) return
    await deletarFilme(id)
    navigate('/')
  }

  const handleAvaliacao = async (e) => {
    e.preventDefault()
    setErro('')
    const nota = parseFloat(novaAv.nota)
    if (isNaN(nota) || nota < 0 || nota > 10) {
      setErro('Nota deve ser entre 0 e 10')
      return
    }
    await criarAvaliacao(id, { ...novaAv, nota })
    setNovaAv({ autor: '', nota: '', comentario: '' })
    carregar()
  }

  const handleDeletarAv = async (avId) => {
    await deletarAvaliacao(avId)
    carregar()
  }

  if (!filme) return <div className="container" style={{padding:'3rem'}}>Carregando...</div>

  const notaMedia = filme.avaliacoes.length
    ? (filme.avaliacoes.reduce((s, a) => s + a.nota, 0) / filme.avaliacoes.length).toFixed(1)
    : null

  return (
    <div className="container">
      <div className="detalhe-hero">
        {filme.poster_url
          ? <img src={filme.poster_url} alt={filme.titulo} />
          : <div className="poster-lg">{filme.tipo === 'serie' ? '📺' : '🎬'}</div>
        }
        <div className="detalhe-info" style={{flex:1}}>
          <h1>{filme.titulo}</h1>
          <div className="meta-row">
            <span className={`badge ${filme.tipo === 'serie' ? 'badge-serie' : ''}`}>
              {filme.tipo === 'serie' ? 'Série' : 'Filme'}
            </span>
            {filme.ano && <span style={{marginLeft:'0.5rem'}}>{filme.ano}</span>}
            {filme.duracao_min && <span style={{marginLeft:'0.5rem'}}>• {filme.duracao_min} min</span>}
            {notaMedia && <span style={{marginLeft:'0.5rem', color:'#f5c518'}}>★ {notaMedia}/10</span>}
          </div>
          {filme.diretor && <p style={{color:'#aaa', marginBottom:'0.8rem'}}>Dir: {filme.diretor}</p>}
          {filme.sinopse && <p className="sinopse">{filme.sinopse}</p>}
          <div style={{marginBottom:'1.5rem'}}>
            {filme.generos.map(g => <span key={g.id} className="genero-tag">{g.nome}</span>)}
          </div>
          <div style={{display:'flex', gap:'0.8rem'}}>
            <button className="btn btn-secondary" onClick={() => navigate(`/filmes/${id}/editar`)}>Editar</button>
            <button className="btn btn-danger" onClick={handleDeletar}>Deletar</button>
            <button className="btn btn-secondary" onClick={() => navigate('/')}>← Voltar</button>
          </div>
        </div>
      </div>

      <div className="avaliacoes-section">
        <h2>Avaliações ({filme.avaliacoes.length})</h2>
        {filme.avaliacoes.map(a => (
          <div key={a.id} className="avaliacao-card">
            <div className="avaliacao-header">
              <span className="avaliacao-autor">{a.autor}</span>
              <div style={{display:'flex', alignItems:'center', gap:'0.8rem'}}>
                <span className="avaliacao-nota">★ {a.nota}/10</span>
                <button className="btn btn-danger btn-sm" onClick={() => handleDeletarAv(a.id)}>×</button>
              </div>
            </div>
            {a.comentario && <p className="avaliacao-comentario">{a.comentario}</p>}
          </div>
        ))}

        <form onSubmit={handleAvaliacao} style={{marginTop:'1.5rem', background:'#1a1a1a', padding:'1.5rem', borderRadius:'10px', border:'1px solid #2a2a2a'}}>
          <h3 style={{marginBottom:'1rem'}}>Adicionar avaliação</h3>
          <div style={{display:'grid', gridTemplateColumns:'1fr 1fr', gap:'1rem'}}>
            <div className="form-group">
              <label>Nome</label>
              <input value={novaAv.autor} onChange={e => setNovaAv({...novaAv, autor: e.target.value})} required />
            </div>
            <div className="form-group">
              <label>Nota (0–10)</label>
              <input type="number" step="0.1" min="0" max="10" value={novaAv.nota} onChange={e => setNovaAv({...novaAv, nota: e.target.value})} required />
            </div>
          </div>
          <div className="form-group">
            <label>Comentário (opcional)</label>
            <textarea value={novaAv.comentario} onChange={e => setNovaAv({...novaAv, comentario: e.target.value})} />
          </div>
          {erro && <p className="error-msg">{erro}</p>}
          <button className="btn btn-primary" type="submit">Enviar avaliação</button>
        </form>
      </div>
    </div>
  )
}
