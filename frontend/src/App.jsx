import { useEffect, useState } from 'react'
import axios from 'axios'

import SeatGrid from './components/SeatGrid'
import Controls from './components/Controls'
import Legend from './components/Legend'

import './styles.css'

import {
  ToastContainer,
  toast
} from 'react-toastify'

import 'react-toastify/dist/ReactToastify.css'

function App() {

  const [seats, setSeats] = useState([])
  const [groupSize, setGroupSize] = useState(2)
  const [message, setMessage] = useState('')
  const [selectedSeats, setSelectedSeats] = useState([])

  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')

  const [loggedInUser, setLoggedInUser] =
    useState(localStorage.getItem('user') || '')

  const [showAuthModal, setShowAuthModal] =
    useState(false)

  const [selectedMovie, setSelectedMovie] =
    useState('Moana 2')

  const movies = [

    {
      title: 'Moana 2',
      poster:
        'https://m.media-amazon.com/images/M/MV5BZDUxNThhYTUtYjgxNy00MGQ4LTgzOTEtZjg1YTU5NTcwNThlXkEyXkFqcGc@._V1_QL75_UX380_CR0,0,380,562_.jpg'
    },

    {
      title: 'Zootopia 2',
      poster:
        'https://m.media-amazon.com/images/M/MV5BYjg1Mjc3MjQtMTZjNy00YWVlLWFhMWEtMWI3ZTgxYjJmNmRlXkEyXkFqcGc@._V1_QL75_UX380_CR0,0,380,562_.jpg'
    },

    {
      title: 'UP',
      poster:
        'https://m.media-amazon.com/images/M/MV5BMTgyMzE3Nzg2OF5BMl5BanBnXkFtZTcwMzg0Mjc4Mg@@._V1_FMjpg_UX500_.jpg'
    },

    {
      title: 'Lio & Stitch',
      poster:
        'https://m.media-amazon.com/images/M/MV5BYmFmZjM1ZTEtYzQ5ZS00MTRmLTkzMDktYWMxNTg2NGE3YjY4XkEyXkFqcGc@._V1_FMjpg_UX510_.jpg'
    },

    {
      title: 'Tangled',
      poster:
        'https://m.media-amazon.com/images/M/MV5BMTAxNDYxMjg0MjNeQTJeQWpwZ15BbWU3MDcyNTk2OTM@._V1_FMjpg_UX534_.jpg'
    }

  ]

  useEffect(() => {

    fetchSeats(selectedMovie)

  }, [selectedMovie])

  const fetchSeats = async (movieName = selectedMovie) => {

    try {

      const response = await axios.get(
        'http://127.0.0.1:5000/seats',
        {
          params: {
            movie: movieName
          }
        }
      )

      setSeats(response.data)

    } catch {

      setMessage('Failed to load seats.')

    }

  }

  const allocateSeats = async () => {

    try {

      const response = await axios.post(
        'http://127.0.0.1:5000/allocate',
        {
          group_size: groupSize,
          movie: selectedMovie
        }
      )

      setSeats(response.data.seats)

      if (response.data.success) {

        setMessage(
          `Allocated: ${response.data.allocated.join(', ')}`
        )

      } else {

        setMessage(response.data.message)

      }

    } catch {

      setMessage('Allocation failed.')

    }

  }

  const bookSelectedSeats = async () => {

    if (selectedSeats.length === 0) {

      toast.error('No seats selected for manual allocation.')

      return
    }

    try {

      const formattedSeats =
        formatSelectedSeats()

      const updatedSeats = [...seats]

      formattedSeats.forEach(seat => {

        const row =
          seat.charCodeAt(0) - 65

        const col =
          Number(seat.slice(1)) - 1

        updatedSeats[row][col] = "X"

      })

      setSeats(updatedSeats)

      toast.success(
        `Manual booking successful for seats ${formattedSeats.join(', ')}`
      )

      setSelectedSeats([])

    } catch {

      toast.error('Booking failed.')

    }
  }

  const login = async () => {

    try {

      const response = await axios.post(
        'http://127.0.0.1:5000/login',
        {
          username,
          password
        }
      )

      if (response.data.success) {

        localStorage.setItem(
          'user',
          response.data.username
        )

        setLoggedInUser(
          response.data.username
        )

        toast.success('Login successful.')

        setShowAuthModal(false)

      } else {

        toast.error(response.data.message)

      }

    } catch {

      toast.error('Login failed.')

    }

  }

  const register = async () => {

    try {

      const response = await axios.post(
        'http://127.0.0.1:5000/register',
        {
          username,
          password
        }
      )

      toast.success(response.data.message)

    } catch {

      toast.error('Registration failed.')

    }

  }

  const logout = () => {

    localStorage.removeItem('user')

    setLoggedInUser('')

    toast.success('Logged out successfully.')

  }

  const handleSeatClick = (
    rowIndex,
    colIndex,
    seat
  ) => {

    if (
      seat === "X" ||
      seat === "B"
    ) {
      return
    }

    const seatId =
      `${rowIndex}-${colIndex}`

    if (selectedSeats.includes(seatId)) {

      setSelectedSeats(
        selectedSeats.filter(
          s => s !== seatId
        )
      )

    } else {

      setSelectedSeats([
        ...selectedSeats,
        seatId
      ])

    }

  }

  const formatSelectedSeats = () => {

    const rowLabels = [
      "A",
      "B",
      "C",
      "D",
      "E",
      "F",
      "G"
    ]

    return selectedSeats.map(seat => {

      const [row, col] = seat.split('-')

      return (
        `${rowLabels[row]}${Number(col) + 1}`
      )

    })

  }

  return (

    <div className="container">

      <div className="top-bar">

        <div
          className="user-icon"
          onClick={() =>
            setShowAuthModal(true)
          }
        >
          👤
        </div>

        {
          loggedInUser && (

            <div
              className={
                loggedInUser === 'admin'
                  ? 'admin-user'
                  : 'normal-user'
              }
            >

              {loggedInUser}

            </div>

          )
        }

      </div>

      <h1>
        Movie Theatre Seating Allocation System
      </h1>

      {
        showAuthModal && (

          <div className="modal-overlay">

            <div className="auth-modal">

              <h2>
                Login / Register
              </h2>

              <input
                type="text"
                placeholder="Username"
                value={username}
                onChange={(e) =>
                  setUsername(e.target.value)
                }
              />

              <input
                type="password"
                placeholder="Password"
                value={password}
                onChange={(e) =>
                  setPassword(e.target.value)
                }
              />

              <div className="modal-buttons">

                <button onClick={login}>
                  Login
                </button>

                <button onClick={register}>
                  Register
                </button>

                {
                  loggedInUser && (

                    <button onClick={logout}>
                      Logout
                    </button>

                  )
                }

              </div>

              <button
                className="close-modal"
                onClick={() =>
                  setShowAuthModal(false)
                }
              >
                ✕
              </button>

            </div>

          </div>

        )
      }

      <h2>
        Now Showing
      </h2>

      <div className="movies">

        {movies.map((movie, index) => (

          <div
            key={index}
            className={`
              movie-card
              ${
                selectedMovie === movie.title
                  ? 'selected-movie'
                  : ''
              }
            `}
            onClick={() =>
              setSelectedMovie(movie.title)
            }
          >

            <img
              src={movie.poster}
              alt={movie.title}
            />

            <p>
              {movie.title}
            </p>

          </div>

        ))}

      </div>

      <h3>
        Selected Movie -
        {' '}
        {selectedMovie}
      </h3>

      <Controls
        groupSize={groupSize}
        setGroupSize={setGroupSize}
        allocateSeats={allocateSeats}
        bookSelectedSeats={bookSelectedSeats}
      />

      <Legend />

      {
        selectedSeats.length > 0 && (

          <div className="selected-seat-display">

            <strong>
              Selected Seats:
            </strong>

            {' '}

            {
              formatSelectedSeats().join(', ')
            }

          </div>

        )
      }

      <SeatGrid
        seats={seats}
        selectedSeats={selectedSeats}
        handleSeatClick={handleSeatClick}
      />

      <ToastContainer
        position="top-right"
        autoClose={3000}
        hideProgressBar={false}
        newestOnTop={true}
        closeOnClick
        pauseOnHover
        theme="colored"
      />

    </div>

  )

}

export default App