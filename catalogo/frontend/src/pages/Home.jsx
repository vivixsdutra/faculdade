import { useEffect, useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { getFilmes, getGeneros } from '../api'

export default function Home() {
  const [filmes, setFilmes] = useState([])
  const [generos, setGeneros] = useState([])
  const [filtroTipo, setFiltroTipo] = useState('')
  const [filtroGenero, setFiltroGenero] = useState('')
  const navigate = useNavigate()

  const carregar = async () => {
    const params = {}
    if (filtroTipo) params.tipo = filtroTipo
    if (filtroGenero) params.genero_id = filtroGenero
    const { data } = await getFilmes(params)
    setFilmes(data)
  }

  useEffect(() => {
    getGeneros().then(r => setGeneros(r.data))
  }, [])

  useEffect(() => { carregar() }, [filtroTipo, filtroGenero])

  return (
    <div className="container">
      <h1 className="page-title">Catálogo</h1>
      <div className="filtros">
        <select value={filtroTipo} onChange={e => setFiltroTipo(e.target.value)}>
          <option value="">Todos os tipos</option>
          <option value="filme">Filmes</option>
          <option value="serie">Séries</option>
        </select>
        <select value={filtroGenero} onChange={e => setFiltroGenero(e.target.value)}>
          <option value="">Todos os gêneros</option>
          {generos.map(g => <option key={g.id} value={g.id}>{g.nome}</option>)}
        </select>
        {(filtroTipo || filtroGenero) && (
          <button className="btn btn-secondary btn-sm" onClick={() => { setFiltroTipo(''); setFiltroGenero('') }}>
            Limpar filtros
          </button>
        )}
      </div>

      {filmes.length === 0 ? (
        <p className="empty-state">Nenhum filme encontrado. <a href="/filmes/novo">Adicione o primeiro!</a></p>
      ) : (
        <div className="filmes-grid">
          {filmes.map(f => (
            <div key={f.id} className="filme-card" onClick={() => navigate(`/filmes/${f.id}`)}>
              {f.poster_url
                ? <img src={f.poster_url} alt={f.titulo} onError={e => e.target.style.display='none'} />
                : <div className="poster-placeholder">{f.tipo === 'serie' ? '📺' : '🎬'}</div>
              }
              <div className="card-info">
                <div className="card-titulo">{f.titulo}</div>
                <div className="card-meta">
                  <span className={`badge ${f.tipo === 'serie' ? 'badge-serie' : ''}`}>
                    {f.tipo === 'serie' ? 'Série' : 'Filme'}
                  </span>
                  {f.ano && <span>{f.ano}</span>}
                </div>
                <div style={{marginTop: '0.4rem', display:'flex', flexWrap:'wrap', gap:'3px'}}>
                  {f.generos.slice(0,2).map(g => (
                    <span key={g.id} className="genero-tag">{g.nome}</span>
                  ))}
                </div>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  )
}
