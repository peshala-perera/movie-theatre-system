import { useEffect, useState } from 'react'

import './styles.css'

import {
  ToastContainer,
  toast
} from 'react-toastify'

import 'react-toastify/dist/ReactToastify.css'

import SeatGrid from './components/SeatGrid'
import Controls from './components/Controls'
import Key from './components/Key'
import MovieList from './components/MovieList'
import BookingModal from './components/BookingModal'

import movies from './data/movies'
import users from './data/users'

import {
  fetchSeatsApi,
  allocateSeatsApi
} from './services/api'

function App() {

  const [seats, setSeats] = useState([])

  const [selectedMovie, setSelectedMovie] =
    useState('Moana 2')

  const [showBookingModal, setShowBookingModal] =
    useState(false)

  const [selectedUser, setSelectedUser] =
    useState('John')

  const [groupSize, setGroupSize] =
    useState(2)

  const [hasCompanion, setHasCompanion] =
    useState(false)

  useEffect(() => {

    fetchSeats()

  }, [selectedMovie])

  const fetchSeats = async () => {

    try {

      const data =
        await fetchSeatsApi(
          selectedMovie
        )

      setSeats(data)

    } catch {

      toast.error(
        'Failed to load seats.'
      )

    }

  }

  const openAutoModal = () => {

    setShowBookingModal(true)

  }

  const currentUser =
    users.find(
      u => u.name === selectedUser
    )

  const allocateSeats = async () => {

    try {

      const response =
        await allocateSeatsApi({

          movie: selectedMovie,

          no_of_seats:
            Number(groupSize),

          customer_type:
            currentUser.type,

          is_admin:
            currentUser.type === 'admin',

          is_paired:
            hasCompanion

        })

      setSeats(response.seats)

      if (response.success) {

        toast.success(
          `Allocated Seats: ${response.allocated_seats.join(', ')}`
        )

      } else {

        toast.error(
          response.message
        )

      }

      setShowBookingModal(false)

    } catch {

      toast.error(
        'Seat allocation failed.'
      )

    }

  }

  return (

    <div className="container">

      <h1>
        Movie Theatre Seating Allocation System
      </h1>

      <MovieList
        movies={movies}
        selectedMovie={selectedMovie}
        setSelectedMovie={setSelectedMovie}
      />

      <h3>

        Selected Movie:
        {' '}
        {selectedMovie}

      </h3>

      <Controls
        openAutoModal={openAutoModal}
      />

      {
        showBookingModal && (

          <BookingModal

            users={users}

            selectedUser={selectedUser}
            setSelectedUser={setSelectedUser}

            groupSize={groupSize}
            setGroupSize={setGroupSize}

            currentUser={currentUser}

            hasCompanion={hasCompanion}
            setHasCompanion={setHasCompanion}

            allocateSeats={allocateSeats}

            setShowBookingModal={
              setShowBookingModal
            }

            selectedMovie={selectedMovie}

          />

        )
      }

      <Key />

      <SeatGrid
        seats={seats}
      />

      <ToastContainer
        position="top-right"
        autoClose={3000}
        theme="colored"
      />

    </div>

  )

}

export default App