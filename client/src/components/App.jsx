import {BrowserRouter as Router, Routes, Route} from 'react-router-dom'
import NavBar from './NavBar'
import Home from './pages/Home'

function App() {


  return (
    <>
      <Router>
        <Routes>
          <Route path='/' element={<NavBar />}>
            <Route index element={<Home />}/>
          </Route>
        </Routes>
      </Router>

    </>
  )
}

export default App
