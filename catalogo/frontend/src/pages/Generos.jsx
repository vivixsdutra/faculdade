import { useEffect, useState } from 'react'
import { getGeneros, criarGenero, deletarGenero } from '../api'

export default function Generos() {
  const [generos, setGeneros] = useState([])
  const [nome, setNome] = useState('')
  const [erro, setErro] = useState('')

  const carregar = () => getGeneros().then(r => setGeneros(r.data))
  useEffect(() => { carregar() }, [])

  const handleCriar = async (e) => {
    e.preventDefault()
    setErro('')
    try {
      await criarGenero({ nome })
      setNome('')
      carregar()
    } catch (err) {
      setErro(err.response?.data?.detail || 'Erro')
    }
  }

  const handleDeletar = async (id) => {
    if (!confirm('Deletar gênero?')) return
    await deletarGenero(id)
    carregar()
  }

  return (
    <div className="container">
      <h1 className="page-title">Gerenciar Gêneros</h1>
      <div className="form-container" style={{marginTop:'1.5rem'}}>
        <form onSubmit={handleCriar} style={{display:'flex', gap:'1rem', alignItems:'flex-end'}}>
          <div className="form-group" style={{flex:1, marginBottom:0}}>
            <label>Novo gênero</label>
            <input value={nome} onChange={e => setNome(e.target.value)} required placeholder="ex: Ação, Drama..." />
          </div>
          <button className="btn btn-primary" type="submit">Adicionar</button>
        </form>
        {erro && <p className="error-msg" style={{marginTop:'0.5rem'}}>{erro}</p>}

        <div style={{marginTop:'1.5rem', display:'flex', flexWrap:'wrap', gap:'0.8rem'}}>
          {generos.map(g => (
            <div key={g.id} style={{display:'flex', alignItems:'center', gap:'0.5rem', background:'#222', padding:'6px 14px', borderRadius:'20px', border:'1px solid #333'}}>
              <span>{g.nome}</span>
              <button className="btn btn-danger btn-sm" style={{padding:'1px 7px', borderRadius:'50%'}} onClick={() => handleDeletar(g.id)}>×</button>
            </div>
          ))}
          {generos.length === 0 && <p style={{color:'#555'}}>Nenhum gênero cadastrado.</p>}
        </div>
      </div>
    </div>
  )
}
