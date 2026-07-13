import { Routes, Route, Link } from 'react-router-dom'
import Home from './pages/Home'
import DetalheFilme from './pages/DetalheFilme'
import FormFilme from './pages/FormFilme'
import Generos from './pages/Generos'

export default function App() {
  return (
    <>
      <nav>
        <div className="nav-inner">
          <Link to="/" className="logo">🎬 CineLog</Link>
          <div className="nav-links">
            <Link to="/">Catálogo</Link>
            <Link to="/filmes/novo">+ Adicionar</Link>
            <Link to="/generos">Gêneros</Link>
          </div>
        </div>
      </nav>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/filmes/novo" element={<FormFilme />} />
        <Route path="/filmes/:id" element={<DetalheFilme />} />
        <Route path="/filmes/:id/editar" element={<FormFilme />} />
        <Route path="/generos" element={<Generos />} />
      </Routes>
    </>
  )
}
