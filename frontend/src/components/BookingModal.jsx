import UserSelection from './UserSelection'
import Counter from './Counter'
import BookingInfo from './BookingInfo'

function BookingModal({

  users,
  selectedUser,
  setSelectedUser,

  groupSize,
  setGroupSize,

  currentUser,

  hasCompanion,
  setHasCompanion,

  allocateSeats,
  setShowBookingModal,

  selectedMovie

}) {

  return (

    <div className="modal-overlay">

      <div className="booking-modal">

        <h2>
          {selectedMovie}
        </h2>

        <h3>
          Auto Seat Allocation
        </h3>

        <UserSelection
          users={users}
          selectedUser={selectedUser}
          setSelectedUser={setSelectedUser}
        />

        <Counter
          groupSize={groupSize}
          setGroupSize={setGroupSize}
          currentUser={currentUser}
        />

        {
          currentUser?.type ===
          'disabled' && (

            <label className="companion-box">

                <input
                    type="checkbox"
                    className="companion-checkbox"
                    checked={hasCompanion}
                    onChange={(e) =>
                    setHasCompanion(
                        e.target.checked
                    )
                    }
                />

                <span>
                    Need Companion Seating
                </span>

            </label>

          )
        }

        <BookingInfo
          currentUser={currentUser}
        />

        <button
          className="confirm-booking-btn"
          onClick={allocateSeats}
        >

          Confirm Auto Allocation

        </button>

        <button
          className="close-modal"
          onClick={() =>
            setShowBookingModal(false)
          }
        >

          ✕

        </button>

      </div>

    </div>

  )

}

export default BookingModal